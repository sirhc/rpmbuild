Name:           fx
Version:        39.2.0
Release:        1%{?dist}
Summary:        Terminal JSON viewer & processor

License:        MIT
URL:            https://github.com/antonmedv/fx
Source0:        https://github.com/antonmedv/fx/releases/download/%{version}/%{name}_linux_amd64
Source1:        https://raw.githubusercontent.com/antonmedv/fx/refs/tags/%{version}/LICENSE

%description
Fx is a dual-purpose command-line tool tailored for JSON, providing both a
terminal-based JSON viewer and a JSON processing utility. While the JSON viewer
is crafted in Go and functions without external dependencies, the JSON
processing tool is developed in JS, compatible with Node.js and Deno.

%global debug_package %{nil}

%prep

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Mon Feb 16 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 39.2.0-1
- Update to 39.2.0

* Tue Apr 15 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 35.0.0-1
- Initial package
