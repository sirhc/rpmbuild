Name:           git-delta
Version:        0.21.2
Release:        1%{?dist}
Summary:        Syntax-highlighting pager for git, diff, and grep output

License:        MIT
URL:            https://github.com/dandavison/delta
Source0:        https://github.com/dandavison/delta/releases/download/%{version}/delta-%{version}-%{_arch}-unknown-linux-gnu.tar.gz
Source1:        https://raw.githubusercontent.com/dandavison/delta/refs/tags/%{version}/themes.gitconfig

ExclusiveArch:  x86_64 aarch64

%description
Delta is a syntax-highlighting pager for git, diff, grep, and blame output. It
supports side-by-side view, line numbering, word-level diff highlighting, and
an interactive TUI mode (--tui) for browsing git history.

%global debug_package %{nil}

%prep
%setup -n delta-%{version}-%{_arch}-unknown-linux-gnu

%build
for shell in bash zsh fish; do
  ./delta --generate-completion "$shell" > "completion.$shell"
done

%check
./delta --version

%install
install -Dpm 0755 delta %{buildroot}%{_bindir}/delta
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/delta/themes.gitconfig
install -Dpm 0644 completion.bash %{buildroot}%{bash_completions_dir}/delta.bash
install -Dpm 0644 completion.zsh %{buildroot}%{zsh_completions_dir}/_delta
install -Dpm 0644 completion.fish %{buildroot}%{fish_completions_dir}/delta.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/delta
%{_datadir}/delta/
%{bash_completions_dir}/delta.bash
%{zsh_completions_dir}/_delta
%{fish_completions_dir}/delta.fish

%changelog
* Thu Nov 19 2026 Chris Grau <113591+sirhc@users.noreply.github.com> - 0.21.2-1
- Initial package
