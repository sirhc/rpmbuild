# Ref: https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/
# Ref: https://src.fedoraproject.org/rpms/nodejs-packaging/

%global debug_package %{nil}

%{?nodejs_default_filter}

Name:           gemini-cli
Version:        0.33.0
Release:        1%{?dist}
Summary:        An open-source AI agent that brings the power of Gemini directly into your terminal
License:        Apache-2.0
URL:            https://github.com/google-gemini/gemini-cli
Source0:        https://registry.npmjs.org/@google/gemini-cli/-/gemini-cli-%{version}.tgz
Source1:        @google-gemini-cli-%{version}-nm-prod.tgz
Source2:        @google-gemini-cli-%{version}-nm-dev.tgz
Source3:        @google-gemini-cli-%{version}-bundled-licenses.txt

ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs
BuildRequires:  nodejs-devel

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini directly
into your terminal. It provides lightweight access to Gemini, giving you the
most direct path from your prompt to our model.

%prep
%setup -q -n package
cp %{SOURCE3} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr dist node_modules node_modules_prod package.json %{buildroot}%{nodejs_sitelib}/%{name}

chmod 0755 %{buildroot}%{nodejs_sitelib}/%{name}/dist/index.js

find %{buildroot} -depth -wholename '*/prebuilds/darwin-*' -delete
find %{buildroot} -depth -wholename '*/prebuilds/win32-*' -delete
%ifarch x86_64
find %{buildroot} -depth -wholename '*/prebuilds/linux-arm*' -delete
%endif
%ifarch aarch64
find %{buildroot} -depth -wholename '*/prebuilds/linux-x64' -delete
%endif

mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{name}/dist/index.js %{buildroot}%{_bindir}/gemini

%check
%nodejs_symlink_deps --check

%files
%doc README.md
%license LICENSE @google-gemini-cli-%{version}-bundled-licenses.txt
%{_bindir}/gemini
%{nodejs_sitelib}/%{name}

%changelog
* Thu Mar 12 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.33.0-1
- Initial package (with lots of help from Claude Code)
