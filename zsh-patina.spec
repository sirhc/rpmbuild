Name:           zsh-patina
Version:        1.5.0
Release:        1%{?dist}
Summary:        A blazingly fast Zsh syntax highlighter

License:        MIT
URL:            https://github.com/michel-kraemer/zsh-patina
Source0:        https://github.com/michel-kraemer/zsh-patina/releases/download/%{version}/zsh-patina-v%{version}-%{_arch}-unknown-linux-musl.tar.gz

%description
zsh-patina is a blazingly fast syntax highlighter for Zsh. It highlights
commands as you type, giving you instant visual feedback about the validity
of your input.

%global debug_package %{nil}

%prep
%setup -n zsh-patina-v%{version}-%{_arch}-unknown-linux-musl

%build

%check

%install
install -Dpm 0755 zsh-patina %{buildroot}%{_bindir}/zsh-patina
install -dm 0755 %{buildroot}%{_datadir}/zsh/site-functions
./zsh-patina completion > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%{_bindir}/zsh-patina
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sat Apr 18 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.5.0-1
- Update to 1.5.0

* Sat Apr 11 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.4.0-1
- Update to 1.4.0
- Add zsh completion file

* Wed Apr 08 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.3.1-1
- Initial package
