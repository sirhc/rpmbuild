%global srcname curlify

Name:           python3-%{srcname}
Version:        2.2.1
Release:        1%{?dist}
Summary:        Convert a python requests request object into a curl command

License:        MIT
URL:            https://github.com/ofw/curlify
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Requires:       python3-requests

%description
Curlify converts a python-requests request object into a curl command that
can be run from a shell.

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

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.2.1-1
- Initial package
