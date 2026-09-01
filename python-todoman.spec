%global srcname todoman

Name:           python3-%{srcname}
Version:        4.7.0
Release:        2%{?dist}
Summary:        A simple icalendar-based todo manager

License:        ISC
URL:            https://github.com/pimutils/todoman
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel

Requires:       python3-click
Requires:       python3-click-log
Requires:       python3-dateutil
Requires:       python3-humanize
Requires:       python3-icalendar
Requires:       python3-parsedatetime
Requires:       python3-pyxdg
Requires:       python3-urwid

# Needed by the bash and zsh completion scripts
Recommends:     jq

Provides:       todoman = %{version}-%{release}

%description
Todoman is a simple, standards-based, cli todo (aka: task) manager. Todos are
stored into icalendar files, which means you can sync them via CalDAV using,
for example, vdirsyncer.

%prep
%autosetup -n %{srcname}-%{version}

# Upstream omits build-backend, which makes the PEP 517 tooling fall back to the
# legacy setuptools backend and look for a non-existent setup.py.
sed -i '/^requires = /a build-backend = "setuptools.build_meta"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname}

install -Dpm 0644 contrib/completion/bash/_todo \
    %{buildroot}%{_datadir}/bash-completion/completions/todo
install -Dpm 0644 contrib/completion/zsh/_todo \
    %{buildroot}%{_datadir}/zsh/site-functions/_todo
install -Dpm 0644 contrib/completion/fish/todo.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/todo.fish

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/todo
%{_datadir}/bash-completion/completions/todo
%{_datadir}/zsh/site-functions/_todo
%{_datadir}/fish/vendor_completions.d/todo.fish

%changelog
* Tue Sep  1 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 4.7.0-2
- Add "todoman" provide so "dnf install todoman" works

* Tue Sep  1 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 4.7.0-1
- Initial package
