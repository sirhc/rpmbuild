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

# Update a spec file to a new version and publish
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
```

## Spec File Patterns

### Pre-built binary (most common)
Source binaries are downloaded directly from GitHub releases. The spec uses `%global debug_package %{nil}` since there's nothing to debug. The `%build` section is minimal or empty. See `eza.spec` or `oh-my-posh.spec`.

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

The `just update` recipe generates this automatically using `strftime`.

## Key Tools Required

- `rpmbuild`, `spectool`, `rpmspec` — RPM build tools
- `copr-cli` — for publishing to COPR
- `gh` — GitHub CLI, used for `latest-release` lookups
- `fd`, `fzf` — used in Justfile for interactive spec selection
- `gum` — used in `just update` for interactive confirmation prompts
- `sponge` — used in `just update` for in-place file editing
