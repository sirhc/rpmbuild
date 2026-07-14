# Ref: https://antigravity.google

%global debug_package %{nil}

Name:           antigravity-cli
Version:        1.1.2
Release:        1%{?dist}
Summary:        Google Antigravity CLI - Terminal-first surface for Antigravity agents
License:        Proprietary
URL:            https://github.com/google-antigravity/antigravity-cli
Source0:        https://github.com/google-antigravity/antigravity-cli/releases/download/%{version}/agy_cli_linux_x64.tar.gz

ExclusiveArch:  x86_64

Requires:       glibc >= 2.28
Requires:       libstdc++ >= 3.4.25

%description
Antigravity CLI brings the reasoning, execution, and orchestration 
capabilities of the Antigravity agent harness directly into your terminal.

%prep
%autosetup -c

%build
# Package is pre-compiled; no build step needed

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 antigravity %{buildroot}%{_bindir}/antigravity

%files
%{_bindir}/antigravity

%changelog
* Tue Jul 14 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.1.2-1
- Update to 1.1.2

* Sat Jul 11 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.1.1-1
- Update to 1.1.1

* Wed Jul 08 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.1.0-1
- Initial antigravity-cli package replacing legacy gemini-cli
