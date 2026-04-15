Name:           resticprofile
Version:        0.33.1
Release:        1%{?dist}
Summary:        Configuration profiles manager and scheduler for restic backup

License:        GPL-3.0-only
URL:            https://github.com/creativeprojects/resticprofile
Source0:        https://github.com/creativeprojects/resticprofile/releases/download/v%{version}/resticprofile_no_self_update_%{version}_linux_amd64.tar.gz
Source1:        https://raw.githubusercontent.com/creativeprojects/resticprofile/refs/tags/v%{version}/LICENSE

ExclusiveArch:  x86_64

%description
resticprofile is the missing link between a configuration file and restic backup.
It reads a configuration file in TOML, YAML, HCL, or JSON format and generates
the command-line parameters and environment variables for restic. It also provides
a scheduler to run backup profiles automatically.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 resticprofile %{buildroot}%{_bindir}/resticprofile

%files
%license LICENSE
%{_bindir}/resticprofile

%changelog
* Wed Apr 15 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.33.1-1
- Update to 0.33.1

* Fri Apr 10 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.33.0-1
- Initial package
