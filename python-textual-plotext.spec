%global srcname textual-plotext
%global pypi_name textual_plotext

Name:           python3-%{srcname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A Textual widget wrapper for the Plotext plotting library

License:        MIT
URL:            https://github.com/Textualize/textual-plotext
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Requires:       python3-plotext >= 5.2.8
Requires:       python3-textual >= 0.86.2

%description
textual-plotext wraps the plotext plotting library as a Textual widget, so
Plotext-based plots can be used inside Textual applications.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
%pyproject_check_import

%files -f %{pyproject_files}

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.1-1
- Initial package
