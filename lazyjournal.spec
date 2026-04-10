Name:           lazyjournal
Version:        0.8.6
Release:        1%{?dist}
Summary:        TUI for viewing logs from journald, Docker/Podman, and Kubernetes

License:        MIT
URL:            https://github.com/Lifailon/lazyjournal
Source0:        https://github.com/Lifailon/lazyjournal/releases/download/%{version}/lazyjournal-%{version}-linux-amd64
Source1:        https://raw.githubusercontent.com/Lifailon/lazyjournal/refs/tags/%{version}/LICENSE

ExclusiveArch:  x86_64

%description
lazyjournal is a TUI for viewing logs from journald, auditd, file system,
Docker and Podman containers, Compose stacks, and Kubernetes pods with
support for log highlighting and several filtering modes.

%global debug_package %{nil}

%prep

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/lazyjournal

%files
%license LICENSE
%{_bindir}/lazyjournal

%changelog
* Fri Apr 10 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.8.6-1
- Initial package
