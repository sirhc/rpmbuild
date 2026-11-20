Name:           granted
Version:        0.40.0
Release:        1%{?dist}
Summary:        The easiest way to access AWS

License:        MIT
URL:            https://github.com/fwdcloudsec/granted
Source0:        https://github.com/fwdcloudsec/granted/releases/download/v%{version}/%{name}_%{version}_linux_x86_64.tar.gz
Source1:        https://raw.githubusercontent.com/fwdcloudsec/granted/refs/tags/v%{version}/LICENCE

ExclusiveArch:  x86_64

%description
Granted is a command line interface (CLI) application which simplifies access
to cloud roles and allows multiple cloud accounts to be opened in your web
browser simultaneously.

The assume command must be sourced by the shell to export credentials; add
alias assume=". assume" (bash/zsh) or source assume.fish (fish).

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 granted %{buildroot}%{_bindir}/granted
install -Dpm 0755 assumego %{buildroot}%{_bindir}/assumego
install -Dpm 0755 assume %{buildroot}%{_bindir}/assume
install -Dpm 0644 assume.fish %{buildroot}%{_bindir}/assume.fish

%files
%license LICENCE
%{_bindir}/granted
%{_bindir}/assumego
%{_bindir}/assume
%{_bindir}/assume.fish

%changelog
* Fri Nov 20 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.40.0-1
- Initial package
