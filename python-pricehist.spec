%global srcname pricehist

Name:           python3-%{srcname}
Version:        1.4.16
Release:        1%{?dist}
Summary:        Fetch and format historical price data

License:        MIT
URL:            https://gitlab.com/chrisberkhout/pricehist
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Requires:       python3-cssselect
Requires:       python3-curlify
Requires:       python3-lxml
Requires:       python3-requests

%description
Pricehist fetches historical price data for currencies, commodities, and
other assets from a range of sources, and formats it for import into
plain-text accounting systems such as hledger, ledger, and beancount.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/pricehist

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.4.16-1
- Initial package
