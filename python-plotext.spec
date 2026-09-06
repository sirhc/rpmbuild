%global srcname plotext

# X-Update-Block: 6.0.0 upstream beta rewrite; drops the flat 5.x API and
# plotext._dict/_utility, which breaks python-textual-plotext (and hledger-textual).
# Also no longer noarch (compiles a C++ kernel). Revisit when 6.x is final and
# textual-plotext supports it.

Name:           python3-%{srcname}
Version:        5.3.2
Release:        1%{?dist}
Summary:        Plotting library for terminal output

License:        MIT
URL:            https://github.com/piccolomo/plotext
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

%description
Plotext plots directly on terminal, exploiting and extending the
capabilities of the print function.

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
%{_bindir}/plotext

%changelog
* Fri Aug 21 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 5.3.2-1
- Initial package
