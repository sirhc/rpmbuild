set shell := ['zsh', '-cu']

copr := 'copr:copr.fedorainfracloud.org:cgrau:' + repo
repo := 'personal'

_default:

build spec_file=shell('ls -1 *.spec | xargs -I % basename % .spec | fzf'):
  spectool --get-files --sourcedir {{ spec_file }}
  rpmbuild -ba {{ spec_file }}

build-source spec_file=shell('ls -1 *.spec | xargs -I % basename % .spec | fzf'):
  spectool --get-files --sourcedir {{ spec_file }}
  rpmbuild -bs {{ spec_file }}

build-all:
  ls -1 *.spec | xargs -I % basename % .spec | xargs -I % just build %

publish spec_file=shell('ls -1 *.spec | xargs -I % basename % .spec | fzf'):
  copr-cli build {{ repo }} $( just _srcrpm {{ spec_file }} )

publish-all:
  ls -1 *.spec | xargs -I % basename % .spec | grep -v eza | xargs -I % just publish %

clean spec_file=shell('ls -1 *.spec | xargs -I % basename % .spec | fzf'):
  rm -fv $( just _srcrpm {{ spec_file }} ) $( just _binrpm {{ spec_file }} )
  spectool --list-files {{ spec_file }} | awk '{ print $2 }' | sed -e 's,.*/,,' | xargs -I @ rm -fv '{{ shell("rpm --eval '%{_sourcedir}'") }}/@'

install package=shell('ls -1 *.spec | xargs -I % basename % .spec | fzf'):
  sudo dnf install --disablerepo='*' --enablerepo={{ copr }} --refresh {{ file_stem(package) }}

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

_srcrpm spec_file:
  @rpm --eval "%{_srcrpmdir}/$( rpmspec --srpm -q --qf '%{name}-%{version}-%{release}\n' {{ spec_file }} ).src.rpm"

_binrpm spec_file:
  @rpm --eval "%{_rpmdir}/$( rpmspec --srpm -q --qf '%{arch}/%{name}-%{version}-%{release}.%{arch}\n' {{ spec_file }} ).rpm"

_latest repo:
  gh release list --repo {{ repo }} --json 'isLatest,tagName' --jq '.[] | select(.isLatest) | .tagName'
