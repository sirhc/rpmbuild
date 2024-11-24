Name:           pup
Version:        0.4.0
Release:        1%{?dist}
Summary:        Parsing HTML at the command line

License:        MIT
URL:            https://github.com/ericchiang/pup
Source0:        https://github.com/ericchiang/pup/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang

%description
pup is a command line tool for processing HTML. It reads from stdin, prints to
stdout, and allows the user to filter parts of the page using CSS selectors.

Inspired by jq, pup aims to be a fast and flexible way of exploring HTML from
the terminal.

%global debug_package %{nil}

%prep
%autosetup

%build
go mod init github.com/ericchiang/pup
go mod tidy
go mod vendor
go build -v -o %{name}

%check

%install
install -Dpm 0755 pup %{buildroot}%{_bindir}/pup

%files
%{_bindir}/pup
%license LICENSE

%changelog
* Sun Nov 20 2022 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.4.0-1
- Initial version
