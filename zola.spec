Name:           zola
Version:        0.22.1
Release:        1%{?dist}
Summary:        A fast static site generator in a single binary with everything built-in

License:        MIT
URL:            https://github.com/johnkerl/miller
Source0:        https://github.com/getzola/zola/releases/download/v%{version}/zola-v%{version}-%{_arch}-unknown-linux-gnu.tar.gz
Source1:        https://raw.githubusercontent.com/getzola/zola/refs/tags/v%{version}/LICENSE

%description

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 zola %{buildroot}%{_bindir}/zola

%files
%{_bindir}/zola
%license LICENSE

%changelog
* Thu Jan 22 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.22.1-1
- Update to 0.22.1

* Tue Jan 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.22.0-1
- Update to 0.22.0

* Mon Jul 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.21.0-1
- Update to 0.21.0

* Fri Feb 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.20.0-1
- Update to 0.20.0

* Sun Nov 24 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.19.2-1
- Initial package
