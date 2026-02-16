Name:           intelli-shell
Version:        3.3.0
Release:        1%{?dist}
Summary:        Like IntelliSense, but for shells

License:        Apache-2.0
URL:            https://github.com/lasantosr/intelli-shell
Source0:        https://github.com/lasantosr/intelli-shell/releases/download/v%{version}/intelli-shell-%{_arch}-unknown-linux-musl.tar.gz
Source1:        https://raw.githubusercontent.com/lasantosr/intelli-shell/refs/tags/v%{version}/LICENSE

%description
IntelliShell is a powerful command template and snippet manager for your shell.
It goes far beyond a simple history search, transforming your terminal into a
structured, searchable, and intelligent library of your commands.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 intelli-shell %{buildroot}%{_bindir}/intelli-shell

%files
%{_bindir}/intelli-shell
%license LICENSE

%changelog
* Fri Nov  7 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 3.3.0-1
- Initial package
