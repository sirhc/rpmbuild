%global upname htmltab
%global common_sum  Command-line utility to convert HTML tables into CSV files
%global common_desc HTMLTab is a command-line utility to select a table within an HTML document and \
convert it to CSV.


Name:           python-%{upname}
Version:        0.2.0
Release:        1%{?dist}
Summary:        %{common_sum}

License:        MIT
URL:            https://flother.github.io/%{upname}
Source0:        https://github.com/flother/%{upname}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
# BuildRequires:  python3-pytest

%description
%{common_desc}


%package -n python3-%{upname}
Summary:        %{common_sum}
Provides:       %{upname} = %{version}-%{release}
Obsoletes:      python2-%{upname} <= %{version}-%{release}
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}


%prep
%autosetup -n %{upname}-%{version}
%{__rm} -fr *.egg-info
sed -i \
  -e 's/use_scm_version.*/version="%{version}",/' \
  -e 's/setuptools_scm/setuptools/' \
  -e 's/"lxml .*/"lxml",/' \
  setup.py


%build
%py3_build


%install
%{__mkdir} -p %{buildroot}%{_mandir}/man1

%py3_install
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
#{__python3} -m pytest


%files -n python3-%{upname}
%license LICENCE
%doc README.md
%{_bindir}/python3-%{upname}
%{_bindir}/%{upname}
%{_bindir}/%{name}
%{_mandir}/man1/python3-%{upname}.1*
%{_mandir}/man1/%{upname}.1*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{upname}
%{python3_sitelib}/%{upname}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Nov 25 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.2.0
- Initial package
