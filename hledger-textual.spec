%global srcname hledger-textual
%global pypi_name hledger_textual

Name:           python3-%{srcname}
Version:        0.3.7
Release:        1%{?dist}
Summary:        A full-featured terminal user interface for hledger plain-text accounting

License:        MIT
URL:            https://github.com/thesmokinator/hledger-textual
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-uv-build

Requires:       hledger
Requires:       python3-babel
Requires:       python3-fpdf2
Requires:       python3-pricehist
Requires:       python3-textual >= 3.0.0
Requires:       python3-textual-plotext

%description
hledger-textual is a full-featured terminal user interface for hledger
plain-text accounting, built with the Textual framework.

%prep
%autosetup -n %{pypi_name}-%{version}
# Relax the uv_build pin to match the version packaged in Fedora
sed -i 's/uv_build>=0.10.5,<0.11.0/uv_build>=0.10.5,<1.0.0/' pyproject.toml
# Fedora ships textual 4.0.0; upstream currently pins <4
sed -i "s/textual>=3.0.0,<4/textual>=3.0.0/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/hledger-textual

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.3.7-1
- Initial package
