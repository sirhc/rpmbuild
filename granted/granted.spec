Name:           granted
Version:        0.2.5
Release:        1%{?dist}
Summary:        The easiest way to access your cloud

License:        MIT
URL:            https://github.com/common-fate/granted
Source0:        https://github.com/common-fate/granted/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang

%description
Granted is a command line interface (CLI) application which simplifies access
to cloud roles and allows multiple cloud accounts to be opened in your web
browser simultaneously.

%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%prep
%autosetup

%build
go build -o granted cmd/granted/main.go
go build -o assumego cmd/assume/main.go

%check

%install
install -Dpm 0755 granted %{buildroot}%{_bindir}/granted
install -Dpm 0755 assumego %{buildroot}%{_bindir}/assumego
install -Dpm 0755 scripts/assume %{buildroot}%{_bindir}/assume
install -Dpm 0755 scripts/assume.fish %{buildroot}%{_bindir}/assume.fish

%files
%{_bindir}/granted
%{_bindir}/assumego
%{_bindir}/assume
%{_bindir}/assume.fish
%license LICENCE

%changelog
* Tue Jul 19 2022 Chris Grau <chris@grau.org> - 4.26.1-1
- Initial version
