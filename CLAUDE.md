# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a collection of RPM spec files for packages published to a personal [Fedora COPR repository](https://copr.fedorainfracloud.org/coprs/cgrau/personal/). All workflows are managed via `just` (Justfile).

## Common Commands

```bash
# Build a specific spec file (prompts with fzf if omitted)
just build <spec-file>

# Build source RPM only
just build-source <spec-file>

# Publish a built source RPM to COPR
just publish <spec-file>

# Update a spec file to a new version, then interactively commit, build, and publish
just update <spec-file> <version>

# Check current version in a spec file
just current-release <spec-file>

# Check latest upstream release (uses gh CLI against the URL: field; requires a GitHub URL)
just latest-release <spec-file>

# Check for updates across all spec files and update any that are out of date
just update-packages

# List upstream releases for a spec
just list-releases <spec-file>

# Build all specs
just build-all

# Publish all specs
just publish-all

# Install a package directly from COPR
just install <spec-file>

# Clean build artifacts for a spec
just clean <spec-file>

# Open the COPR repo in browser
just open

# Show current build status for all packages in COPR
just monitor

# Watch in-progress COPR builds (prompts with fzf if omitted)
just watch [build-id...]

# Upgrade all COPR-managed packages via dnf
just upgrade

# Upgrade packages installed outside COPR (granted, miller) directly from GitHub releases
just others
```

## Spec File Patterns

### Pre-built binary (most common)
Source binaries are downloaded directly from GitHub releases. The spec uses `%global debug_package %{nil}` since there's nothing to debug. The `%build` section is minimal or empty. Use `ExclusiveArch: x86_64` when binaries are only published for that architecture. See `eza.spec` or `oh-my-posh.spec`.

**Tarball extraction:** Most pre-built binary tarballs are flat (no top-level directory), so use `%setup -c %{name}-%{version}` to wrap extraction in a named dir. If the tarball has a named top-level directory, use `%setup -n <dir-name>` instead (the dir name may include `%{_arch}` when the release asset embeds the architecture). For standard source tarballs that follow RPM naming conventions, use `%autosetup`.

### Script/noarch package
For shell scripts or other architecture-independent content, use `BuildArch: noarch` instead of `%global debug_package %{nil}`. See `wd.spec`.

### Node.js package
Source from npmjs.org. Uses `%{?nodejs_find_provides_and_requires}` or `%{?nodejs_default_filter}` macro and `ExclusiveArch: %{nodejs_arches}`. When the npm package is pre-bundled, no extra build step is needed; install the bundle dir directly into `%{nodejs_sitelib}/%{name}` and symlink the entry point into `%{_bindir}`. See `github-copilot.spec` or `gemini-cli.spec`.

### Python package
Uses `%pyproject_wheel` / `%pyproject_install` / `%pyproject_save_files` macros with `%generate_buildrequires`. See `python-beancount.spec`.

## Changelog Format

Entries must follow this exact format (author is always Chris Grau):

```
* Day Mon DD YYYY Chris Grau <113591+sirhc@users.noreply.github.com> - <version>-<release>
- <description>
```

The `just update` recipe generates this automatically using `strftime` and always sets `Release` back to `1`. To bump the release without changing the version (e.g., for a packaging fix), edit the spec manually. Always verify that the day-of-week abbreviation matches the actual date — this is a common mistake. Single-digit days are padded with a space, not a zero (e.g., `Apr  7` not `Apr 07`).

## Key Tools Required

- `rpmbuild`, `spectool`, `rpmspec` — RPM build tools
- `copr-cli` — for publishing to COPR
- `gh` — GitHub CLI, used for `latest-release` lookups
- `fd`, `fzf` — used in Justfile for interactive spec selection
- `gum` — used in `just update` for interactive confirmation prompts
- `sponge` — used in `just update` for in-place file editing
- `mlr` (Miller) — used in `just monitor` to pretty-print COPR JSON output
