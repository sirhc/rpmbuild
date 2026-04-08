Name:           zsh-patina
Version:        1.3.1
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

%files
%license LICENSE
%{_bindir}/zsh-patina

%changelog
* Wed Apr 08 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.3.1-1
- Initial package
