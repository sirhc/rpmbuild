%global srcname beancount

%bcond check 1

Name:           python-%{srcname}
Version:        3.2.0
Release:        1%{?dist}
Summary:        Double-Entry Accounting from Text Files

License:        GPL-2.0-only
URL:            https://beancount.github.io/docs/
Source:         %{pypi_source beancount}

BuildRequires:  python3-devel
BuildRequires:  bison
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  sed

%if %{with check}
BuildRequires:  gpg
BuildRequires:  make
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Beancount is double-entry bookkeeping computer language that lets you define
financial transaction records in a text file, read them in memory, generate a
variety of reports from them, and provides a web interface.}

%description %_description

%package -n     %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}
Suggests:       %{srcname}-doc = %{version}-%{release}

%description -n %{srcname} %_description

%package -n     %{srcname}-doc
Summary:        Documentation and examples for Beancount
Requires:       python3-%{srcname} = %{version}-%{release}
BuildArch:      noarch

%description -n %{srcname}-doc %_description

This package provides additional documentation and examples for Beancount.

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

This package provides the Python libraries for Beancount.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Remove useless files
find examples/ -type f -name .keep -delete

# Fix end of line encoding
sed -i 's/\r$//' examples/tutorial/holdings-csv.output

# Drop shebang as bean-web no longer exists
sed -e "\|#!/usr/bin/env bean-web|d" -i examples/simple/starter.beancount
chmod -x examples/simple/starter.beancount

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

%check
%if %{with check}
# We need to resetup meson here to actually build the parser tests
meson setup --reconfigure -Dtests=enabled build/ && meson test -C build/
ln -s \
  %{buildroot}%{python3_sitearch}/beancount/parser/_parser%{python3_ext_suffix} \
  beancount/parser/
# Disable broken tests in Python 3.14
%pytest -v \
  --deselect beancount/parser/lexer_test.py::TestLexer::test_bad_date \
  --deselect beancount/parser/parser_test.py::TestReferenceCounting::test_parser_lex \
  --deselect beancount/parser/parser_test.py::TestReferenceCounting::test_parser_lex_filename \
  --deselect beancount/parser/parser_test.py::TestReferenceCounting::test_parser_lex_multi \
  --deselect beancount/parser/parser_test.py::TestReferenceCounting::test_parser_parse \
  %{nil}

%else
%pyproject_check_import
%endif

%files -n %{srcname}
%doc README.rst
%{_bindir}/bean-check
%{_bindir}/bean-doctor
%{_bindir}/bean-example
%{_bindir}/bean-format
%{_bindir}/treeify

%files -n %{srcname}-doc
%license COPYING
%doc CHANGES CREDITS TODO
%doc examples/

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING

%changelog
* Mon Feb 16 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 3.2.0-1
- Update to 3.2.0 for my personal repo

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 3.1.0-4
- Disable broken tests in Python 3.14; Fixes: RHBZ#2359530

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.14

* Thu Mar 20 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 3.1.0-1
- Initial import; Fixes: RHBZ#2251448
