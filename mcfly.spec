Name:           mcfly
Version:        0.9.4
Release:        1%{?dist}
Summary:        Fly through your shell history

License:        MIT
URL:            https://github.com/cantino/mcfly
Source0:        https://github.com/cantino/mcfly/releases/download/v%{version}/mcfly-v%{version}-%{_arch}-unknown-linux-musl.tar.gz
Source1:        https://raw.githubusercontent.com/cantino/mcfly/refs/tags/v%{version}/LICENSE

%description
McFly replaces your default ctrl-r shell history search with an intelligent
search engine that takes into account your working directory and the context of
recently executed commands. McFly's suggestions are prioritized in real time
with a small neural network.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 mcfly %{buildroot}%{_bindir}/mcfly

%files
%{_bindir}/mcfly
%license LICENSE

%changelog
* Thu Dec 25 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.4-1
- Update to 0.9.4

* Wed Feb 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.3-1
- Update to 0.9.3

* Sun Nov 24 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.2-1
- Initial package
