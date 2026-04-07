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

# Check latest upstream release (uses gh CLI against the URL: field)
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
```

## Spec File Patterns

### Pre-built binary (most common)
Source binaries are downloaded directly from GitHub releases. The spec uses `%global debug_package %{nil}` since there's nothing to debug. The `%build` section is minimal or empty. See `eza.spec` or `oh-my-posh.spec`.

### Node.js package
Uses `%{?nodejs_find_provides_and_requires}` macro, `ExclusiveArch: %{nodejs_arches}`, and `%nodejs_symlink_deps --check` in `%check`. Node.js packages bundle their dependencies using `nodejs-packaging-bundler <npm-package-name>` to generate the bundled tarball sources before building. See `github-copilot.spec` or `gemini-cli.spec`.

### Python package
Uses `%pyproject_wheel` / `%pyproject_install` / `%pyproject_save_files` macros with `%generate_buildrequires`. See `python-beancount.spec`.

### Haskell package (cabal-rpm generated)
Uses `ghc-rpm-macros` (`%ghc_lib_build`, `%ghc_lib_install`, etc.) with subpackages for library/devel/doc/prof. See `hledger.spec`.

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
