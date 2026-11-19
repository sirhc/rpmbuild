%ifarch x86_64
%global go_arch amd64
%endif

%ifarch aarch64
%global go_arch arm64
%endif

Name:           nogon
Version:        0.22.0
Release:        1%{?dist}
Summary:        Your own search engine

License:        AGPL-3.0-only
URL:            https://github.com/asciimoo/nogon
Source0:        https://github.com/asciimoo/nogon/releases/download/v%{version}/%{name}_%{version}_linux_%{go_arch}
Source1:        https://raw.githubusercontent.com/asciimoo/nogon/refs/tags/v%{version}/LICENSE

# Upstream renamed hister to nogon in 0.22.0
Provides:       hister = %{version}-%{release}
Obsoletes:      hister < 0.22.0-1

ExclusiveArch:  x86_64 aarch64

BuildRequires:  systemd-rpm-macros

%description
Nogon (formerly Hister) is a search server and terminal client for indexing
and searching your own content.

%global debug_package %{nil}

%prep

%build
cp %{SOURCE1} .

cat > %{name}.service <<'EOF'
[Unit]
Description=Nogon web history service
After=network.target

[Service]
Type=simple
ExecStart=%{_bindir}/nogon listen
Restart=on-failure
# Keep the pre-rename data directory so existing data stays put
StateDirectory=hister
Environment=NOGON_DATA_DIR=%%S/hister
EnvironmentFile=-%%h/.config/hister/hister.env
EnvironmentFile=-%%h/.config/nogon/nogon.env

[Install]
WantedBy=default.target
EOF

%check

%install
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service
ln -s %{name} %{buildroot}%{_bindir}/hister

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/hister
%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service

%changelog
* Thu Nov 19 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.22.0-1
- Update to 0.22.0
- Rename from hister to nogon to follow upstream

* Wed Oct 28 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.21.0-1
- Update to 0.21.0

* Fri Sep 25 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.20.0-1
- Update to 0.20.0

* Fri Sep 04 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.19.0-1
- Update to 0.19.0

* Sun Aug 23 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.18.0-1
- Update to 0.18.0

* Mon Aug  3 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.17.0-2
- Add systemd service

* Mon Aug  3 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.17.0-1
- Initial package
