%global debug_package %{nil}

%{?nodejs_find_provides_and_requires}

Name:           github-copilot
Version:        0.0.405
Release:        1%{?dist}
Summary:        GitHub Copilot CLI
License:        https://docs.github.com/en/site-policy/github-terms/github-pre-release-license-terms
URL:            https://github.com/github/copilot-cli
Source0:        https://registry.npmjs.org/@github/copilot/-/copilot-%{version}.tgz

ExclusiveArch:  %{nodejs_arches}

Requires:       nodejs
BuildRequires:  nodejs-devel

%description
GitHub Copilot CLI brings AI-powered coding assistance directly to your command
line, enabling you to build, debug, and understand code through natural language
conversations. Powered by the same agentic harness as GitHub's Copilot coding
agent, it provides intelligent assistance while staying deeply integrated with
your GitHub workflow.

%prep
%setup -q -n package

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr \
  index.js \
  package.json \
  prebuilds/ \
  sdk/ \
  sharp/ \
  tree-sitter-bash.wasm \
  tree-sitter-powershell.wasm \
  tree-sitter.wasm \
  worker/ \
  %{buildroot}%{nodejs_sitelib}/%{name}

find %{buildroot} -depth -wholename '*/*darwin-*' -delete
find %{buildroot} -depth -wholename '*/*linux-arm*' -delete
find %{buildroot} -depth -wholename '*/*linux-ia32*' -delete
find %{buildroot} -depth -wholename '*/*linuxmusl*' -delete
find %{buildroot} -depth -wholename '*/*win32-*' -delete

mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{name}/index.js %{buildroot}%{_bindir}/copilot

%check
%nodejs_symlink_deps --check

%files
%doc README.md
%license LICENSE.md
%{_bindir}/copilot
%{nodejs_sitelib}/%{name}

%changelog
* Fri Feb 06 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.405-1
- Update to 0.0.405

* Thu Feb 05 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.403-1
- Update to 0.0.403

* Wed Feb 04 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.402-1
- Update to 0.0.402

* Tue Feb 03 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.401-1
- Update to 0.0.401

* Fri Jan 30 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.400-1
- Update to 0.0.400

* Wed Jan 28 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.398-1
- Update to 0.0.398

* Wed Jan 28 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.397-1
- Update to 0.0.397

* Wed Jan 28 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.396-1
- Update to 0.0.396

* Tue Jan 27 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.395-1
- Update to 0.0.395

* Sun Jan 25 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.394-1
- Update to 0.0.394

* Fri Jan 23 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.393-1
- Update to 0.0.393

* Thu Jan 22 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.389-1
- Update to 0.0.389

* Tue Jan 20 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.388-1
- Update to 0.0.388

* Fri Jan 16 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.384-1
- Update to 0.0.384

* Wed Jan 14 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.382-1
- Update to 0.0.382

* Tue Jan 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.381-1
- Update to 0.0.381

* Tue Jan 13 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.380-1
- Update to 0.0.380

* Tue Dec 30 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.373-1
- Update to 0.0.373

* Fri Dec 19 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.371-1
- Update to 0.0.371

* Thu Dec 18 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.370-1
- Update to 0.0.370

* Fri Dec 12 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.369-1
- Update to 0.0.369

* Thu Dec 11 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.368-1
- Update to 0.0.368

* Sun Dec  7 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.367-1
- Update to 0.0.367

* Thu Dec  4 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.366-2
- Don't use available artifacts from GitHub

* Thu Dec  4 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.366-1
- Update to 0.0.366
- Use available artifacts from GitHub

* Wed Nov 26 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.365-1
- Update to 0.0.365

* Tue Nov 25 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.363-1
- Update to 0.0.363

* Fri Nov 21 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.362-1
- Update to 0.0.362

* Tue Nov 18 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.360-1
- Update to 0.0.360

* Fri Nov 14 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.358-1
- Update to 0.0.358

* Thu Nov  6 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.0.354-1
- Initial package
