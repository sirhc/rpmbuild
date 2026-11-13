Name:           typst
Version:        0.15.1
Release:        1%{?dist}
Summary:        A markup-based typesetting system

License:        Apache-2.0
URL:            https://github.com/typst/typst
Source0:        https://github.com/typst/typst/releases/download/v%{version}/typst-%{_arch}-unknown-linux-musl.tar.xz

ExclusiveArch:  x86_64 aarch64

%description
Typst is a new markup-based typesetting system that is designed to be as
powerful as LaTeX while being much easier to learn and use. It has built-in
markup for common formatting tasks, flexible functions for everything else, an
integrated scripting system, math typesetting, bibliography management, and
fast compile times thanks to incremental compilation.

%global debug_package %{nil}

%prep
%setup -n typst-%{_arch}-unknown-linux-musl

%build

%check

%install
install -Dpm 0755 typst %{buildroot}%{_bindir}/typst

%{buildroot}%{_bindir}/typst completions bash | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/bash-completion/completions/typst
%{buildroot}%{_bindir}/typst completions zsh  | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/zsh/site-functions/_typst
%{buildroot}%{_bindir}/typst completions fish | install -Dpm 0644 /dev/stdin %{buildroot}%{_datadir}/fish/vendor_completions.d/typst.fish

%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/typst
%{_datadir}/bash-completion/completions/typst
%{_datadir}/zsh/site-functions/_typst
%{_datadir}/fish/vendor_completions.d/typst.fish

%changelog
* Fri Nov 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.15.1-1
- Initial package
