Name:           oh-my-posh
Version:        29.1.0
Release:        1%{?dist}
Summary:        The most customisable and low-latency cross platform/shell prompt renderer

License:        MIT
URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source0:        https://github.com/JanDeDobbeleer/oh-my-posh/releases/download/v%{version}/posh-linux-amd64
Source1:        https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/refs/tags/v%{version}/COPYING

%description
%{summary}.

%global debug_package %{nil}

%prep

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/oh-my-posh

%files
%{_bindir}/oh-my-posh
%license COPYING

%changelog
* Sun Jan 25 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 29.1.0-1
- Update to 29.1.0

* Tue Jan 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 29.0.2-1
- Update to 29.0.2

* Wed Dec 31 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.9.0-1
- Update to 28.9.0

* Sun Dec 28 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.7.0-1
- Update to 28.7.0

* Tue Dec 23 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.5.1-1
- Update to 28.5.1

* Mon Dec 22 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.5.0-1
- Update to 28.5.0

* Thu Dec 18 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.3.1-1
- Update to 28.3.1

* Mon Dec 15 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.3.0-1
- Update to 28.3.0

* Sun Dec 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.2.2-2
- Fix source file (caching left the old file in the source package)

* Sun Dec 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.2.2-1
- Update to 28.2.2

* Fri Dec 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 28.2.1-1
- Initial package
- Created only to give me 28.x while Fedora is on 26.x
