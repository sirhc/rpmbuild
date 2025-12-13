Name:           htmlq
Version:        0.4.0
Release:        1%{?dist}
Summary:        Like jq, but for HTML

License:        MIT
URL:            https://github.com/mgdm/htmlq
Source0:        https://github.com/mgdm/htmlq/releases/download/v%{version}/htmlq-%{_arch}-linux.tar.gz
Source1:        https://raw.githubusercontent.com/mgdm/htmlq/refs/tags/v%{version}/LICENSE.md

%description
Like jq, but for HTML. Uses CSS selectors to extract bits of content from HTML
files.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE.md

%changelog
* Fri Dec 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.4.0-1
- Initial version
