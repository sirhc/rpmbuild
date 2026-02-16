Name:           vibecheck
Version:        1.7.7
Release:        1%{?dist}
Summary:        AI-tool to generate meaningful and consistent Git commit messages

License:        MIT
URL:            https://github.com/rshdhere/vibecheck
Source0:        https://github.com/rshdhere/vibecheck/releases/download/v%{version}/vibecheck_Linux_%{_arch}.tar.gz

%description
A Cross-Platform Command-Line AI-tool for automating git commit messages by
outsourcing them to LLMs. Supports multiple providers including OpenAI, Gemini,
Anthropic, Groq, Grok, Kimi K2, Qwen, DeepSeek, Perplexity Sonar, and Ollama.

%global debug_package %{nil}

%prep
%setup -c %{name}-%{version}

%build

%check

%install
install -Dpm 0755 vibecheck %{buildroot}%{_bindir}/vibecheck

%files
%license LICENSE
%doc README.md
%{_bindir}/vibecheck

%changelog
* Mon Feb 16 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.7.7-1
- Update to 1.7.7

* Wed Nov 19 2025 Chris Grau <113591+sirhc@users.noreply.github.com> - 1.4.3-1
- Initial package
