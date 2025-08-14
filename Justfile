set shell := ["zsh", "-c"]

repo := "personal"

_default:

build spec:
  spectool --get-files --sourcedir '{{ spec }}'
  rpmbuild -ba '{{ spec }}'

publish spec:
  copr-cli build '{{ repo }}' "$( just _srcrpm '{{ spec }}' )"

clean spec:
  rm -fv "$( just _srcrpm '{{ spec }}' )" "$( just _binrpm '{{ spec }}' )"
  spectool --list-files '{{ spec }}' | awk '{ print $2 }' | sed -e 's,.*/,,' | xargs -I @ rm -fv '{{ shell("rpm --eval '%{_sourcedir}'") }}/@'

open:
  xdg-open https://copr.fedorainfracloud.org/coprs/cgrau/{{ repo }}/

others:
  #!/usr/bin/env -S zsh -e
  v_granted="$( just _latest fwdcloudsec/granted )"
  v_miller="$( just _latest johnkerl/miller )"

  sudo dnf upgrade \
    https://github.com/fwdcloudsec/granted/releases/download/$v_granted/granted_$( tr -d v <<< $v_granted)_linux_amd64.rpm \
    https://github.com/johnkerl/miller/releases/download/$v_miller/miller-$( tr -d v <<< $v_miller )-linux-amd64.rpm

_srcrpm spec:
  @rpm --eval "%{_srcrpmdir}/$( rpmspec --srpm -q --qf '%{name}-%{version}-%{release}\n' '{{ spec }}' ).src.rpm"

_binrpm spec:
  @rpm --eval "%{_rpmdir}/$( rpmspec --srpm -q --qf '%{arch}/%{name}-%{version}-%{release}.%{arch}\n' '{{ spec }}' ).rpm"

_latest repo:
  gh release list --repo '{{ repo }}' --json 'isLatest,tagName' --jq '.[] | select(.isLatest) | .tagName'
