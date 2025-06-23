Name:           wd
Version:        0.10.1
Release:        1%{?dist}
Summary:        Jump to custom directories in zsh

License:        MIT
URL:            https://github.com/mfaerevaag/%{name}
Source0:        https://github.com/mfaerevaag/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gzip

%description

%global debug_package %{nil}

%prep
%autosetup

%build

%check

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/zsh/site-functions
%{__mkdir} -p %{buildroot}%{_mandir}/man1

cp wd.sh %{buildroot}%{_bindir}/wd.sh
cp _wd.sh %{buildroot}%{_datadir}/zsh/site-functions/_wd.sh
ln -s _wd.sh %{buildroot}%{_datadir}/zsh/site-functions/_wd
gzip -c wd.1 > %{buildroot}%{_mandir}/man1/wd.1.gz

%files
%{_bindir}/%{name}.sh
%{_datadir}/zsh/site-functions/_%{name}*
%{_mandir}/man1/%{name}.1*
%doc README.md tty.gif
%license LICENSE

%changelog
* Mon Jun 23 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.10.1-1
- Update to 0.10.1

* Wed Apr 23 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 29 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.3-1
- Update to 0.9.3

* Tue Nov 26 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.2-2
- Use the upstream command name (with .sh)

* Tue Nov 26 2024 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.9.2-1
- Initial package
