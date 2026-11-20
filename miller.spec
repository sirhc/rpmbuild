Name:           miller
Version:        6.22.0
Release:        1%{?dist}
Summary:        Like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and JSON

License:        BSD-2-Clause
URL:            https://github.com/johnkerl/miller
Source0:        https://github.com/johnkerl/miller/releases/download/v%{version}/%{name}-%{version}-linux-amd64.tar.gz
Source1:        https://raw.githubusercontent.com/johnkerl/miller/refs/tags/v%{version}/man/mlr.1

ExclusiveArch:  x86_64

%description
Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV,
TSV, and tabular JSON. You get to work with your data using named fields,
without needing to count positional column indices.

%global debug_package %{nil}

%prep
%setup -n %{name}-%{version}-linux-amd64

%build

%check

%install
install -Dpm 0755 mlr %{buildroot}%{_bindir}/mlr
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/mlr.1

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/mlr
%{_mandir}/man1/mlr.1*

%changelog
* Fri Nov 20 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 6.22.0-1
- Initial package
