Name:           hledger
Version:        1.52.1
Release:        1%{?dist}
Summary:        Command-line plain text accounting

License:        GPL-3.0-or-later
URL:            https://github.com/simonmichael/hledger
Source0:        https://github.com/simonmichael/hledger/releases/download/%{version}/hledger-linux-x64.tar.gz
Source1:        https://raw.githubusercontent.com/simonmichael/hledger/refs/tags/%{version}/LICENSE

ExclusiveArch:  x86_64

%description
hledger is lightweight, portable, and dependable accounting software for
tracking money, time, or other commodities, on desktop, server, or web, with
no ads or subscriptions. It is double-entry accounting software that reads from
plain text data files. It is written in Haskell and is a member of the Ledger
family of accounting tools.

%global debug_package %{nil}

%prep
%setup -c

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 hledger %{buildroot}%{_bindir}/hledger
install -Dpm 0755 hledger-ui %{buildroot}%{_bindir}/hledger-ui
install -Dpm 0755 hledger-web %{buildroot}%{_bindir}/hledger-web
install -Dpm 0644 hledger.1 %{buildroot}%{_mandir}/man1/hledger.1
install -Dpm 0644 hledger-ui.1 %{buildroot}%{_mandir}/man1/hledger-ui.1
install -Dpm 0644 hledger-web.1 %{buildroot}%{_mandir}/man1/hledger-web.1
install -Dpm 0644 hledger.info %{buildroot}%{_infodir}/hledger.info
install -Dpm 0644 hledger-ui.info %{buildroot}%{_infodir}/hledger-ui.info
install -Dpm 0644 hledger-web.info %{buildroot}%{_infodir}/hledger-web.info
install -Dpm 0644 hledger-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/hledger

%files
%license LICENSE
%{_bindir}/hledger
%{_bindir}/hledger-ui
%{_bindir}/hledger-web
%{_mandir}/man1/hledger.1*
%{_mandir}/man1/hledger-ui.1*
%{_mandir}/man1/hledger-web.1*
%{_infodir}/hledger.info*
%{_infodir}/hledger-ui.info*
%{_infodir}/hledger-web.info*
%{_datadir}/bash-completion/completions/hledger

%changelog
* Wed Apr 29 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.52.1-1
- Update to 1.52.1

* Tue Apr 07 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.52-1
- Initial package
