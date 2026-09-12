%global srcname linecast

Name:           python3-%{srcname}
Version:        2.4.0
Release:        2%{?dist}
Summary:        Weather, tides, the sun, the moon, and maps, drawn for the terminal

License:        MIT
URL:            https://github.com/ashuttl/linecast
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip

Provides:       linecast = %{version}-%{release}

%description
linecast turns free public data into six live, mouse-friendly terminal apps
for weather, sunshine, the moon, tides, radar, and maps. It is pure Python
with no dependencies, takes its colors from your terminal theme, and needs no
accounts or API keys.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/linecast completion bash \
    | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/bash-completion/completions/linecast
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/linecast completion zsh \
    | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/zsh/site-functions/_linecast
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/linecast completion fish \
    | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/fish/vendor_completions.d/linecast.fish

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/linecast
%{_datadir}/bash-completion/completions/linecast
%{_datadir}/zsh/site-functions/_linecast
%{_datadir}/fish/vendor_completions.d/linecast.fish

%changelog
* Sat Sep 12 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.4.0-2
- Add bash, zsh, and fish shell completions

* Thu Sep 10 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.4.0-1
- Update to 2.4.0

* Wed Sep 09 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.3.3-1
- Update to 2.3.3

* Sun Sep  6 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.3.2-1
- Initial package
