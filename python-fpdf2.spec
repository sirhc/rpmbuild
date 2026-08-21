%global srcname fpdf2
%global pypi_name fpdf2
%global import_name fpdf

Name:           python3-%{srcname}
Version:        2.8.8
Release:        1%{?dist}
Summary:        Simple PDF generation for Python

License:        LGPL-3.0-only
URL:            https://py-pdf.github.io/fpdf2/
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-fonttools

Requires:       python3-defusedxml
Requires:       python3-pillow
Requires:       python3-fonttools

%description
fpdf2 is a library for PDF document generation in Python, with a focus on
ease of use. It is a fork and the successor of PyFPDF.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{import_name}

%check
%pyproject_check_import

%files -f %{pyproject_files}

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.8.8-1
- Initial package
