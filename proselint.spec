Name:           proselint
Version:        0.16.0
Release:        1%{?dist}
Summary:        A linter for prose

License:        BSD-3-Clause
URL:            https://github.com/amperser/proselint
Source0:        %{pypi_source %{name}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-uv-build

Requires:       python3-google-re2

# Fedora's own proselint package lags upstream; this replaces it.
Provides:       python3-proselint = %{version}-%{release}

%description
proselint is a linter for English prose. It places the world's greatest
writers and editors by your side, where they whisper suggestions on how to
improve your writing.

%prep
%autosetup -n %{name}-%{version}
# google-re2-stubs is a type-stub-only package that is not packaged for Fedora
# and is not needed at runtime.
sed -i '/google-re2-stubs/d' pyproject.toml
# Upstream pins uv_build to <0.8.0; Fedora ships a newer, compatible uv-build.
sed -i 's/uv_build>=[^"]*/uv_build/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{name}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/proselint

%changelog
* Sun Sep 06 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.16.0-1
- Initial package
