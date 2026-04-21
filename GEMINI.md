# Gemini CLI Context: RPM Spec Files for COPR

This repository contains a collection of RPM spec files for packages published to the [cgrau/personal Fedora COPR repository](https://copr.fedorainfracloud.org/coprs/cgrau/personal/).

## Project Overview

- **Purpose:** Automate the building, updating, and publishing of various software packages (mostly CLI tools) to COPR.
- **Main Technologies:** RPM (`rpmbuild`, `spectool`), Fedora COPR (`copr-cli`), and GitHub CLI (`gh`).
- **Task Management:** Workflows are orchestrated using `just` (see `Justfile`).

## Building and Running

The project uses `just` to handle common packaging tasks. Many commands will prompt for a spec file using `fzf` if one is not provided.

### Common Commands

- **Build a package locally:**
  ```bash
  just build <spec-file>
  ```
- **Build source RPM only (SRPM):**
  ```bash
  just build-source <spec-file>
  ```
- **Publish to COPR:**
  ```bash
  just publish <spec-file>
  ```
- **Update a package to a new version:**
  This command updates the version, generates a changelog entry, commits the change, builds the SRPM, and publishes to COPR.
  ```bash
  just update <spec-file> <version>
  ```
- **Check for updates across all packages:**
  ```bash
  just update-packages
  ```
- **Monitor COPR build status:**
  ```bash
  just monitor
  ```

## Development Conventions

### Spec File Patterns

- **Pre-built binaries (Most Common):** Usually GitHub releases. Use `%global debug_package %{nil}` and `ExclusiveArch: x86_64` if applicable.
- **Node.js packages:** Source from npmjs.org. Use `%{?nodejs_default_filter}` and `ExclusiveArch: %{nodejs_arches}`.
- **Python packages:** Use `%pyproject_*` macros.
- **Shell scripts:** Use `BuildArch: noarch`.

### Changelog Format

Changelog entries must follow this exact format:
```text
* Day Mon DD YYYY Chris Grau <113591+sirhc@users.noreply.github.com> - <version>-<release>
- <description>
```
*Note: Single-digit days are padded with a space (e.g., `Apr  7` not `Apr 07`). The `just update` command handles this automatically.*

### Tool Requirements

Ensure the following tools are installed for full functionality:
- `rpm-build`, `rpmdevtools` (for `spectool`, `rpmspec`)
- `copr-cli`
- `gh` (GitHub CLI)
- `just`
- `fd`, `fzf`, `gum`, `sponge` (from `moreutils`), `mlr` (Miller)

## Key Files

- `*.spec`: Individual RPM package definitions.
- `Justfile`: Contains all automation logic.
- `CLAUDE.md`: Additional technical guidance for AI assistants.
