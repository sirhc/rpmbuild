set shell := ['zsh', '-cu']

copr := 'copr:copr.fedorainfracloud.org:cgrau:' + repo
repo := 'personal'

_default:

# Download sources and build binary and source RPMs
build spec_file=shell('fd -g "*.spec" | fzf'):
  spectool --get-files --sourcedir {{ spec_file }}
  rpmbuild -ba {{ spec_file }}

# Download sources and build source RPM only
build-source spec_file=shell('fd -g "*.spec" | fzf'):
  spectool --get-files --sourcedir {{ spec_file }}
  rpmbuild -bs {{ spec_file }}

# Build all spec files
build-all:
  fd -g '*.spec' | xargs -I % just build %

# Upload a built source RPM to COPR
publish spec_file=shell('fd -g "*.spec" | fzf'):
  copr-cli build --nowait {{ repo }} $( just _srcrpm {{ spec_file }} )

# Publish all spec files to COPR
publish-all:
  fd -g '*.spec' | xargs -I % just publish %

# Show current build status for all packages in COPR
monitor:
  copr-cli monitor {{ repo }} | mlr --j2p cat

# Watch in-progress COPR builds (select with fzf)
watch:
  # I don't actually know what the status of in-progress builds is yet.
  copr-cli watch-build $( copr-cli list-builds {{ repo }} | awk '$3 == "..."' | fzf --multi | awk '{ print $1 }' )

# Remove build artifacts for a spec file
clean spec_file=shell('fd -g "*.spec" | fzf'):
  rm -fv $( just _srcrpm {{ spec_file }} ) $( just _binrpm {{ spec_file }} )
  spectool --list-files {{ spec_file }} | awk '{ print $2 }' | sed -e 's,.*/,,' | xargs -I @ rm -fv '{{ shell("rpm --eval '%{_sourcedir}'") }}/@'

# Install a package directly from COPR
install package=shell('fd -g "*.spec" | fzf'):
  sudo dnf install --disablerepo='*' --enablerepo={{ copr }} --refresh {{ file_stem(package) }}

# Check all spec files for upstream updates and update any that are out of date
update-packages:
  #!/usr/bin/env -S zsh -e

  for spec in *.spec; do
    if [[ -n "$( git status --porcelain $spec )"  ]]; then
      print "Changes detected in $spec, skipping update"
      continue
    fi

    current="$( just current-release $spec )"
    latest="$( just latest-release $spec )"

    if [[ -z "$latest" ]]; then
      print "No releases found for $spec, skipping update"
      continue
    fi

    if [[ "$current" == "$latest" || "v$current" == "$latest" ]]; then
      print "Current release $current is up to date for $spec, skipping update"
      continue
    fi

    just update $spec ${latest#v}
  done

# Update a spec file to a new version, commit, build, and publish
update spec version release='1':
  #!/usr/bin/env -S zsh -e
  sed -e '/^Version:/s/ [^ ]*$/ {{ version }}/' -e '/^Release:/s/ [^ ]*$/ {{ release }}%{?dist}/' {{ spec }} |
    awk '
      { print }

      $1 == "%changelog" {
        print "* " strftime("%a %b %d %Y") " Chris Grau <113591+sirhc@users.noreply.github.com> - {{ version }}-{{ release }}"
        print "- Update to {{ version }}"
        print ""
      }
    ' |
    sponge {{ spec }}

  git diff {{ spec }}
  gum confirm 'Commit changes to {{ spec }}?'
  git commit -m 'Update {{ file_stem(spec) }} to {{ version }}' {{ spec }}

  gum confirm 'Build and publish {{ spec }}?'
  just build-source {{ spec }}
  just publish {{ spec }}
  just clean {{ spec }}

# Upgrade all COPR-managed packages via dnf
upgrade:
  sudo dnf upgrade --disablerepo='*' --enablerepo={{ copr }} --refresh

# Open the COPR repository in a browser
open:
  xdg-open https://copr.fedorainfracloud.org/coprs/cgrau/{{ repo }}/

# Upgrade packages not managed by COPR (granted, miller)
others:
  #!/usr/bin/env -S zsh -e
  v_granted=$( just _latest fwdcloudsec/granted )
  v_miller=$( just _latest johnkerl/miller )

  sudo dnf upgrade \
    https://github.com/fwdcloudsec/granted/releases/download/$v_granted/granted_$( tr -d v <<< $v_granted )_linux_amd64.rpm \
    https://github.com/johnkerl/miller/releases/download/$v_miller/miller-$( tr -d v <<< $v_miller )-linux-amd64.rpm

# Print the current version from a spec file
current-release spec_file=shell('fd -g "*.spec" | fzf'):
  @awk '$1 == "Version:" { print $2 }' {{ spec_file }}

# Print the latest upstream release tag from GitHub
latest-release spec_file=shell('fd -g "*.spec" | fzf'):
  @awk '$1 == "URL:" { print $2 }' {{ spec_file }} | xargs gh release list --jq 'map(select(.isLatest))[].tagName' --json isLatest,tagName --repo

# List upstream releases for a spec file
list-releases spec_file=shell('fd -g "*.spec" | fzf'):
  spectool --source 0 {{ spec_file }} | cut -d / -f 4,5 | xargs gh release list --repo

_srcrpm spec_file:
  @rpm --eval "%{_srcrpmdir}/$( rpmspec --srpm -q --qf '%{name}-%{version}-%{release}\n' {{ spec_file }} ).src.rpm"

_binrpm spec_file:
  @rpm --eval "%{_rpmdir}/$( rpmspec --srpm -q --qf '%{arch}/%{name}-%{version}-%{release}.%{arch}\n' {{ spec_file }} ).rpm"

_latest repo:
  gh release list --repo {{ repo }} --json 'isLatest,tagName' --jq '.[] | select(.isLatest) | .tagName'
