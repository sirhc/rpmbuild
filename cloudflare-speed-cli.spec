Name:           cloudflare-speed-cli
Version:        1.0.6
Release:        1%{?dist}
Summary:        CLI for internet speed test via Cloudflare

License:        GPL-3.0-only
URL:            https://github.com/kavehtehrani/cloudflare-speed-cli
Source0:        https://github.com/kavehtehrani/cloudflare-speed-cli/releases/download/v%{version}/cloudflare-speed-cli-%{_arch}-unknown-linux-musl.tar.xz

ExclusiveArch:  x86_64 aarch64

%description
A command-line tool for running internet speed tests via Cloudflare's speed
test infrastructure.

%global debug_package %{nil}

%prep
%setup -n %{name}-%{_arch}-unknown-linux-musl

%build

%install
install -Dpm 0755 cloudflare-speed-cli %{buildroot}%{_bindir}/cloudflare-speed-cli

%files
%license LICENSE
%{_bindir}/cloudflare-speed-cli

%changelog
* Fri Jun 19 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.6-1
- Update to 1.0.6

* Fri Jun 12 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.5-1
- Update to 1.0.5

* Wed May 27 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.1-1
- Update to 1.0.1

* Mon May 25 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.0-1
- Initial package
