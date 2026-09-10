Name:           mdcat
Version:        2.16.1
Release:        1%{?dist}
Summary:        cat for markdown, with syntax highlighting

License:        MPL-2.0
URL:            https://github.com/BIRSAx2/mdcat
Source0:        https://github.com/BIRSAx2/mdcat/releases/download/%{name}-%{version}/%{name}-%{version}-x86_64-unknown-linux-gnu.tar.gz

ExclusiveArch:  x86_64

%description
mdcat renders Markdown on text terminals, with support for inline images,
syntax highlighting, and Mermaid diagrams on suitable terminals. It also
provides mdless, which pages its output, and mdpick, which fuzzy-finds a
Markdown file to render via fzf.

%global debug_package %{nil}

%prep
%setup -n %{name}-%{version}-x86_64-unknown-linux-gnu

%build

%check

%install
install -Dpm 0755 mdcat %{buildroot}%{_bindir}/mdcat
ln -s mdcat %{buildroot}%{_bindir}/mdless
ln -s mdcat %{buildroot}%{_bindir}/mdpick

install -Dpm 0644 mdcat.1/mdcat.1 %{buildroot}%{_mandir}/man1/mdcat.1
ln -s mdcat.1.gz %{buildroot}%{_mandir}/man1/mdless.1.gz
ln -s mdcat.1.gz %{buildroot}%{_mandir}/man1/mdpick.1.gz

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/mdcat
%{_bindir}/mdless
%{_bindir}/mdpick
%{_mandir}/man1/mdcat.1*
%{_mandir}/man1/mdless.1*
%{_mandir}/man1/mdpick.1*

%changelog
* Thu Sep 10 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.16.1-1
- Update to 2.16.1

* Wed Sep 09 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.16.0-1
- Update to 2.16.0

* Fri Sep  4 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 2.15.0-1
- Initial package
