Name:           jbig2enc
Version:        0.31
Release:        1%{?dist}
Summary:        JBIG2 encoder

License:        Apache-2.0
URL:            https://github.com/agl/jbig2enc
Source0:        https://github.com/agl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  leptonica-devel

%description
jbig2enc encodes bi-level (1 bpp) images using JBIG2 compression, which
provides better compression than G4/TIFF. It supports symbol extraction,
classification, text region coding, and refinement coding. Output can be
used standalone or embedded in PDFs.

%prep
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install
rm -f %{buildroot}/usr/lib/liblibjbig2enc.a %{buildroot}%{_includedir}/jbig2enc.h
chmod 0755 %{buildroot}%{_bindir}/jbig2topdf.py

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/jbig2
%{_bindir}/jbig2topdf.py

%changelog
* Sun May 17 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.31-1
- Initial package
