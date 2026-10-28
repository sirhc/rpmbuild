%global upname htmltab
%global common_sum  Command-line utility to convert HTML tables into CSV files
%global common_desc HTMLTab is a command-line utility to select a table within an HTML document and \
convert it to CSV.


Name:           python-%{upname}
Version:        0.2.0
Release:        2%{?dist}
Summary:        %{common_sum}

License:        MIT
URL:            https://github.com/flother/htmltab
Source0:        https://github.com/flother/htmltab/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python3-devel

%description
%{common_desc}


%package -n python3-%{upname}
Summary:        %{common_sum}
Provides:       %{upname} = %{version}-%{release}

%description -n python3-%{upname}
%{common_desc}


%prep
%autosetup -n %{upname}-%{version}
%{__rm} -fr *.egg-info
sed -i \
  -e 's/use_scm_version.*/version="%{version}",/' \
  -e 's/setuptools_scm/setuptools/' \
  -e 's/"lxml .*/"lxml",/' \
  -e 's/setup_requires=.*//' \
  setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%{__mkdir} -p %{buildroot}%{_mandir}/man1

%pyproject_install
%pyproject_save_files -L %{upname}
%{__mv} -f %{buildroot}%{_bindir}/%{upname} %{buildroot}%{_bindir}/python3-%{upname}
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr -s 1 -N -o %{buildroot}%{_mandir}/man1/python3-%{upname}.1 %{buildroot}%{_bindir}/python3-%{upname}
pushd  %{buildroot}%{_bindir}
ln -s python3-%{upname} %{upname}
ln -s python3-%{upname} %{name}
popd
pushd %{buildroot}%{_mandir}/man1/
ln -s python3-%{upname}.1 %{upname}.1
ln -s python3-%{upname}.1 %{name}.1
popd


%check
%pyproject_check_import


%files -n python3-%{upname} -f %{pyproject_files}
%license LICENCE
%doc README.md
%{_bindir}/python3-%{upname}
%{_bindir}/%{upname}
%{_bindir}/%{name}
%{_mandir}/man1/python3-%{upname}.1*
%{_mandir}/man1/%{upname}.1*
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Oct 28 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.2.0-2
- Switch from deprecated %%py3_build/%%py3_install to pyproject macros

* Mon Nov 25 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.2.0
- Initial package
