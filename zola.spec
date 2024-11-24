Name:           zola
Version:        0.19.2
Release:        1%{?dist}
Summary:        Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON

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
* Sun Nov 24 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.19.2-1
- Initial package
