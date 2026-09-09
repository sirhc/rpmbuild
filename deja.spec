Name:           deja
Version:        0.4.2
Release:        1%{?dist}
Summary:        Predictive ghost-text autosuggestions for zsh

License:        MIT
URL:            https://github.com/Giammarco-Ferranti/deja
Source0:        https://github.com/Giammarco-Ferranti/deja/releases/download/v%{version}/deja_%{version}_linux_amd64.tar.gz

ExclusiveArch:  x86_64

%description
Deja is a smarter replacement for zsh-autosuggestions. Instead of only surfacing
commands that start with what you have typed, deja uses fuzzy matching, directory
awareness, and command sequence prediction to suggest what you actually want to
run, as inline ghost text, after every keystroke.

A lightweight background daemon serves all terminal windows with sub-millisecond
responses. All data stays in a local SQLite database; nothing leaves your
machine.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build

%check

%install
install -Dpm 0755 deja %{buildroot}%{_bindir}/deja

%files
%license LICENSE
%doc README.md
%{_bindir}/deja

%changelog
* Tue Sep 08 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.4.2-1
- Initial package
