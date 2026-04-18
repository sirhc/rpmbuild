# Ref: https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/
# Ref: https://src.fedoraproject.org/rpms/nodejs-packaging/

%global debug_package %{nil}

%{?nodejs_default_filter}

Name:           gemini-cli
Version:        0.38.2
Release:        1%{?dist}
Summary:        An open-source AI agent that brings the power of Gemini directly into your terminal
License:        Apache-2.0
URL:            https://github.com/google-gemini/gemini-cli
Source0:        https://registry.npmjs.org/@google/gemini-cli/-/gemini-cli-%{version}.tgz

ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs >= 20
BuildRequires:  nodejs-devel

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini directly
into your terminal. It provides lightweight access to Gemini, giving you the
most direct path from your prompt to our model.

%prep
%setup -q -n package

%build
# Package is pre-bundled; no build step needed

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr bundle package.json %{buildroot}%{nodejs_sitelib}/%{name}

chmod 0755 %{buildroot}%{nodejs_sitelib}/%{name}/bundle/gemini.js

mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{name}/bundle/gemini.js %{buildroot}%{_bindir}/gemini

%files
%doc README.md
%license LICENSE bundle/bundled/third_party/THIRD_PARTY_NOTICES
%{_bindir}/gemini
%{nodejs_sitelib}/%{name}

%changelog
* Sat Apr 18 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.38.2-1
- Update to 0.38.2

* Wed Apr 15 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.38.1-1
- Update to 0.38.1

* Thu Apr 09 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.37.1-1
- Update to 0.37.1

* Wed Apr 08 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.37.0-1
- Update to 0.37.0; package is now pre-bundled (no nodejs-packaging-bundler needed)

* Thu Mar 12 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.33.0-1
- Initial package (with lots of help from Claude Code)
