%ifarch x86_64
%global go_arch amd64
%endif

%ifarch aarch64
%global go_arch arm64
%endif

Name:           humble-cli
Version:        0.23.1
Release:        1%{?dist}
Summary:        The missing CLI for downloading your Humble Bundle purchases

License:        MIT
URL:            https://github.com/smbl64/humble-cli
Source0:        https://github.com/smbl64/humble-cli/releases/download/v%{version}/%{name}-linux-%{go_arch}.tar.gz
Source1:        https://raw.githubusercontent.com/smbl64/humble-cli/refs/tags/v%{version}/LICENSE

ExclusiveArch:  x86_64 aarch64

%description
humble-cli is a command-line tool for downloading your Humble Bundle purchases
without having to navigate the web interface.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 %{name}-linux-%{go_arch} %{buildroot}%{_bindir}/%{name}

%{buildroot}%{_bindir}/%{name} completion bash | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%{buildroot}%{_bindir}/%{name} completion zsh  | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
%{buildroot}%{_bindir}/%{name} completion fish | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Sat Jul 04 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.1-1
- Update to 0.23.1

* Tue Jun  2 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.0-2
- Add shell completions for bash, zsh, and fish

* Tue Jun  2 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.0-1
- Initial package
