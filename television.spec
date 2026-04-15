Name:           television
Version:        0.15.6
Release:        1%{?dist}
Summary:        A general purpose fuzzy finder TUI

License:        MIT
URL:            https://github.com/alexpasmantier/television
Source0:        https://github.com/alexpasmantier/television/releases/download/%{version}/tv-%{version}-x86_64-unknown-linux-gnu.tar.gz

ExclusiveArch:  x86_64

%description
Television is a blazingly fast general purpose fuzzy finder TUI written in Rust.
It uses a channel-based architecture where each channel is a different data source
(files, git log, environment variables, etc.) that can be fuzzily searched.

%global debug_package %{nil}

%prep
%setup -n tv-%{version}-x86_64-unknown-linux-gnu

%build

%check

%install
install -Dpm 0755 tv %{buildroot}%{_bindir}/tv
install -Dpm 0644 doc/tv.1 %{buildroot}%{_mandir}/man1/tv.1

%files
%license LICENSE
%doc README.md
%{_bindir}/tv
%{_mandir}/man1/tv.1*

%changelog
* Wed Apr 15 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.15.6-1
- Update to 0.15.6

* Thu Apr 09 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.15.5-1
- Update to 0.15.5

* Tue Apr 07 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.15.4-1
- Initial package
