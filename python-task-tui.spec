%global srcname task-tui
%global pypi_name task_tui

Name:           python-%{srcname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A TUI frontend for Taskwarrior

License:        Unknown
URL:            https://github.com/lbesnard/task-tui
Source0:        https://github.com/lbesnard/task-tui/releases/download/v%{version}/%{pypi_name}-%{version}-py3-none-any.whl

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-textual

Provides:       task-tui = %{version}-%{release}

Requires:       task
Requires:       python3-textual >= 0.85.0

%description
task-tui is a terminal user interface (TUI) for Taskwarrior, built with the
Textual framework.

%prep
mkdir -p %{_pyproject_wheeldir}
cp %{SOURCE0} %{_pyproject_wheeldir}/

%build

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_bindir}/task-tui

%changelog
* Fri Mar 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.0.1-1
- Initial package
