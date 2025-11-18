Name:           eza
Version:        0.23.4
Release:        2%{?dist}
Summary:        A modern alternative to ls

License:        EUPL 1.2
URL:            https://github.com/eza-community/eza
Source0:        https://github.com/eza-community/eza/releases/download/v%{version}/eza_%{_arch}-unknown-linux-musl.zip
Source1:        https://raw.githubusercontent.com/eza-community/eza/refs/tags/v%{version}/LICENSE.txt
Source2:        https://raw.githubusercontent.com/eza-community/eza/refs/tags/v%{version}/man/eza.1.md
Source3:        https://raw.githubusercontent.com/eza-community/eza/refs/tags/v%{version}/man/eza_colors.5.md
Source4:        https://raw.githubusercontent.com/eza-community/eza/refs/tags/v%{version}/man/eza_colors-explanation.5.md

BuildRequires:  pandoc

%description
eza is a modern alternative for the venerable file-listing command-line program
ls that ships with Unix and Linux operating systems, giving it more features and
better defaults. It uses colours to distinguish file types and metadata. It
knows about symlinks, extended attributes, and Git. And it’s small, fast, and
just one single binary.

By deliberately making some decisions differently, eza attempts to be a more
featureful, more user-friendly version of ls.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

for page in eza.1 eza_colors.5 eza_colors-explanation.5; do
  sed 's/\$version/v%{version}/g' "${page}.md" | pandoc --standalone -f markdown -t man > "$page"
done

%check

%install
install -Dpm 0755 eza %{buildroot}%{_bindir}/eza
install -Dpm 0644 eza.1 %{buildroot}%{_mandir}/man1/eza.1
install -Dpm 0644 eza_colors.5 %{buildroot}%{_mandir}/man5/eza_colors.5
install -Dpm 0644 eza_colors-explanation.5 %{buildroot}%{_mandir}/man5/eza_colors-explanation.5

%files
%license LICENSE.txt
%{_bindir}/eza
%{_mandir}/man1/eza.1*
%{_mandir}/man5/eza_colors.5*
%{_mandir}/man5/eza_colors-explanation.5*

%changelog
* Mon Nov 17 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.4-2
- Add man pages

* Fri Oct  3 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.4-1
- Update to 0.23.4

* Sun Sep 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.3-1
- Update to 0.23.3

* Sat Sep  6 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.2-1
- Update to 0.23.2

* Sun Aug 31 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.1-1
- Update to 0.23.1

* Tue Aug 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.0-1
- Initial package
