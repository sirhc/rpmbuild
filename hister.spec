%ifarch x86_64
%global go_arch amd64
%endif

%ifarch aarch64
%global go_arch arm64
%endif

Name:           hister
Version:        0.17.0
Release:        2%{?dist}
Summary:        Your own search engine

License:        AGPL-3.0-only
URL:            https://github.com/asciimoo/hister
Source0:        https://github.com/asciimoo/hister/releases/download/v%{version}/%{name}_%{version}_linux_%{go_arch}
Source1:        https://raw.githubusercontent.com/asciimoo/hister/refs/tags/v%{version}/LICENSE

ExclusiveArch:  x86_64 aarch64

BuildRequires:  systemd-rpm-macros

%description
Hister is a search server and terminal client for indexing and searching
your own content.

%global debug_package %{nil}

%prep

%build
cp %{SOURCE1} .

cat > %{name}.service <<'EOF'
[Unit]
Description=Hister web history service
After=network.target

[Service]
Type=simple
ExecStart=%{_bindir}/hister listen
Restart=on-failure
StateDirectory=hister
Environment=HISTER_DATA_DIR=%%S/hister
EnvironmentFile=-%%h/.config/hister/hister.env

[Install]
WantedBy=default.target
EOF

%check

%install
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%changelog
* Mon Aug  3 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.17.0-2
- Add systemd service

* Mon Aug  3 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.17.0-1
- Initial package
