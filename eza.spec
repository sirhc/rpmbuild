Name:           eza
Version:        0.23.0
Release:        1%{?dist}
Summary:        A modern alternative to ls

License:        EUPL 1.2
URL:            https://github.com/eza-community/eza
Source0:        https://github.com/eza-community/eza/releases/download/v%{version}/eza_%{_arch}-unknown-linux-musl.zip
Source1:        https://raw.githubusercontent.com/eza-community/eza/refs/tags/v%{version}/LICENSE.txt

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
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 eza %{buildroot}%{_bindir}/eza

%files
%{_bindir}/eza
%license LICENSE.txt

%changelog
* Tue Aug 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.23.0-1
- Initial package
