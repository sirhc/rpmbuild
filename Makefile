SPEC    = $(error SPEC is not set)
REPO    = personal

ARCH    = $(shell rpm --eval '%{_arch}')
NAME    = $(shell rpmspec --srpm -q --qf '%{name}\n' $(SPEC))
RELEASE = $(shell rpmspec --srpm -q --qf '%{release}\n' $(SPEC))
RPM     = $(shell rpm --eval '%{_rpmdir}')/$(ARCH)/$(NAME)-$(VERSION)-$(RELEASE).$(ARCH).rpm
SRCRPM  = $(shell rpm --eval '%{_srcrpmdir}')/$(NAME)-$(VERSION)-$(RELEASE).src.rpm
VERSION = $(shell rpmspec --srpm -q --qf '%{version}\n' $(SPEC))

build: $(SRCRPM)

clean:
	rm -f $(SRCRPM) $(RPM)
	spectool --list-files $(SPEC) | awk '{ print $$2 }' | sed -e 's,.*/,,' | xargs -I {} rm -f $(shell rpm --eval '%{_sourcedir}')/{}

publish: $(SRCRPM)
	copr-cli build $(REPO) $(SRCRPM)

$(SRCRPM): $(SPEC)
	spectool --get-files --sourcedir $(SPEC)
	rpmbuild -ba $(SPEC)
