Name:           ticker
Version:        5.3.0
Release:        1%{?dist}
Summary:        Terminal stock ticker with live updates and position tracking

License:        GPL-3.0-only
URL:            https://github.com/achannarasappa/ticker
Source0:        https://github.com/achannarasappa/ticker/releases/download/v%{version}/%{name}-%{version}-linux-amd64.tar.gz

ExclusiveArch:  x86_64

%description
Track stocks, crypto, and derivatives prices and positions in real time from
your terminal.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build

%check

%install
install -Dpm 0755 ticker %{buildroot}%{_bindir}/ticker

%files
%license LICENSE
%doc README.md
%{_bindir}/ticker

%changelog
* Fri Nov 20 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 5.3.0-1
- Initial package
