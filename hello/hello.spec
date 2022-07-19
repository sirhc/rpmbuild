Name:           hello
Version:        2.10
Release:        1%{?dist}
Summary:        Produces a familiar, friendly greeting

License:        GPLv3+
URL:            https://www.gnu.org/software/hello/
Source0:        https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints “Hello, world!” when
you run it.

https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/

%prep
%autosetup
mv THANKS THANKS.old
iconv --from-code=ISO-8859-1 --to-code=UTF-8 --output=THANKS THANKS.old

%build
%configure
%make_build

%check
make check

%install
%make_install
%find_lang %{name}
rm %{buildroot}/%{_infodir}/dir

%files -f %{name}.lang
%{_bindir}/hello
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%license COPYING

%changelog
* Tue Jul 19 2022 Chris Grau <chris@grau.org> - 2.10-1
- Initial version
