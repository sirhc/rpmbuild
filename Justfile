set shell := ["zsh", "-c"]

repo := "personal"

_all:
  @just --list

build spec:
  spectool --get-files --sourcedir '{{ spec }}'
  rpmbuild -ba '{{ spec }}'

publish spec:
  copr-cli build '{{ repo }}' "$( just _srcrpm '{{ spec }}' )"

clean spec:
  rm -fv "$( just _srcrpm '{{ spec }}' )" "$( just _binrpm '{{ spec }}' )"
  spectool --list-files '{{ spec }}' | awk '{ print $2 }' | sed -e 's,.*/,,' | xargs -I @ rm -fv '{{ shell("rpm --eval '%{_sourcedir}'") }}/@'

@latest:
  just _latest common-fate/granted
  just _latest johnkerl/miller

_latest repo:
  gh release list --repo '{{ repo }}' --json 'isLatest,tagName' --jq '.[] | select(.isLatest) | .tagName'

_srcrpm spec:
  @rpm --eval "%{_srcrpmdir}/$( rpmspec --srpm -q --qf '%{name}-%{version}-%{release}\n' '{{ spec }}' ).src.rpm"

_binrpm spec:
  @rpm --eval "%{_rpmdir}/$( rpmspec --srpm -q --qf '%{arch}/%{name}-%{version}-%{release}.%{arch}\n' '{{ spec }}' ).rpm"
