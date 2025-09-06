set shell := ['zsh', '-cu']

copr := 'copr:copr.fedorainfracloud.org:cgrau:' + repo
repo := 'personal'

_default:

build package:
  spectool --get-files --sourcedir {{ package }}.spec
  rpmbuild -ba {{ package }}.spec

publish package:
  copr-cli build {{ repo }} $( just _srcrpm {{ package }} )

clean package:
  rm -fv $( just _srcrpm {{ package }} ) $( just _binrpm {{ package }} )
  spectool --list-files {{ package }}.spec | awk '{ print $2 }' | sed -e 's,.*/,,' | xargs -I @ rm -fv '{{ shell("rpm --eval '%{_sourcedir}'") }}/@'

install package:
  sudo dnf install --disablerepo='*' --enablerepo={{ copr }} --refresh {{ package }}

upgrade:
  sudo dnf upgrade --disablerepo='*' --enablerepo={{ copr }} --refresh
  
update: upgrade

open:
  xdg-open https://copr.fedorainfracloud.org/coprs/cgrau/{{ repo }}/

others:
  #!/usr/bin/env -S zsh -e
  v_granted=$( just _latest fwdcloudsec/granted )
  v_miller=$( just _latest johnkerl/miller )

  sudo dnf upgrade \
    https://github.com/fwdcloudsec/granted/releases/download/$v_granted/granted_$( tr -d v <<< $v_granted)_linux_amd64.rpm \
    https://github.com/johnkerl/miller/releases/download/$v_miller/miller-$( tr -d v <<< $v_miller )-linux-amd64.rpm

_srcrpm package:
  @rpm --eval "%{_srcrpmdir}/$( rpmspec --srpm -q --qf '%{name}-%{version}-%{release}\n' {{ package }}.spec ).src.rpm"

_binrpm package:
  @rpm --eval "%{_rpmdir}/$( rpmspec --srpm -q --qf '%{arch}/%{name}-%{version}-%{release}.%{arch}\n' {{ package }}.spec ).rpm"

_latest repo:
  gh release list --repo {{ repo }} --json 'isLatest,tagName' --jq '.[] | select(.isLatest) | .tagName'
