Name:           yq
Version:        4.26.1
Release:        1%{?dist}
Summary:        Portable command-line YAML, JSON and XML processor

License:        MIT
URL:            https://github.com/mikefarah/yq
Source0:        https://github.com/mikefarah/yq/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang
BuildRequires:  pandoc

%description
A lightweight and portable command-line YAML, JSON and XML processor. yq uses
jq like syntax but works with yaml files as well as json and xml. It doesn't
yet support everything jq does - but it does support the most common
operations and functions, and more is being added continuously.

%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

%prep
%autosetup

%build
go build -v -o %{name}
scripts/generate-man-page-md.sh
scripts/generate-man-page.sh
ls -l

%check

%install
install -Dpm 0755 yq %{buildroot}%{_bindir}/yq
install -Dpm 0644 yq.1 %{buildroot}%{_mandir}/man1/yq.1

%files
%{_bindir}/yq
%{_mandir}/man1/yq.1.*
%doc release_notes.txt
%license LICENSE

%changelog
* Tue Jul 19 2022 Chris Grau <chris@grau.org> - 4.26.1-1
- Initial version
