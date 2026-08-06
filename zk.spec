Name:           zk
Version:        0.15.6
Release:        1%{?dist}
Summary:        A plain text note-taking assistant

License:        GPL-3.0
URL:            https://github.com/zk-org/zk
Source0:        https://github.com/zk-org/zk/releases/download/v%{version}/zk-v%{version}-linux-amd64.tar.gz
Source1:        https://raw.githubusercontent.com/zk-org/zk/refs/tags/v%{version}/LICENSE

ExclusiveArch:  x86_64

%description
zk is a plain text note-taking assistant. It is primarily designed for
Markdown notes, but you could use it with any type of text-based content.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build
cp %{SOURCE1} .

%check

%install
install -Dpm 0755 zk %{buildroot}%{_bindir}/zk

%files
%license LICENSE
%{_bindir}/zk

%changelog
* Thu Aug 06 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.15.6-1
- Initial package
