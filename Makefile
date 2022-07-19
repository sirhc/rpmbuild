TOPDIR = $(shell pwd)
OUTDIR = /var/www/vhosts/sirhc.us/html/rpm

all:
	find . -type f -name '*.spec' -execdir $(MAKE) -f '$(TOPDIR)/Makefile' build \;

build:
	spectool -g *.spec
	source /etc/os-release && \
		fedpkg --release `echo $$PLATFORM_ID | cut -d: -f2` mockbuild --enable-network

install:
	mkdir -p '$(OUTDIR)'
	find */results_* -type f -name '*.rpm' -exec install -m 0644 -v '{}' '$(OUTDIR)' \;
	createrepo '$(OUTDIR)'
