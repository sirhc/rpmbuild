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
- **Update a package to a new version (interactively commit, build, publish):**
  ```bash
  just update <spec-file> <version> [release]
  ```
- **Check current version in a spec file:**
  ```bash
  just current-release <spec-file>
  ```
- **Check latest upstream release (PyPI if Source0 pulls from pythonhosted.org, else GitHub):**
  ```bash
  just latest-release <spec-file>
  ```
- **Check for updates across all packages:**
  ```bash
  just update-packages
  ```
- **List upstream releases for a spec:**
  ```bash
  just list-releases <spec-file>
  ```
- **Build all specs:**
  ```bash
  just build-all
  ```
- **Publish all specs:**
  ```bash
  just publish-all
  ```
- **Install a package directly from COPR:**
  ```bash
  just install <spec-file>
  ```
- **Remove build artifacts for a spec file:**
  ```bash
  just clean <spec-file>
  ```
- **Open the COPR repo in browser:**
  ```bash
  just open
  ```
- **Show current build status for all packages in COPR:**
  ```bash
  just monitor
  ```
- **Watch in-progress COPR builds (multiple IDs or prompts with fzf):**
  ```bash
  just watch [build-id...]
  ```
- **Upgrade all COPR-managed packages via dnf:**
  ```bash
  just upgrade
  ```
- **Upgrade non-COPR managed packages (granted, miller, ticker):**
  ```bash
  just others
  ```

## Development Conventions

### Spec File Patterns

- **Pre-built binaries (Most Common):** Usually GitHub releases. Use `%global debug_package %{nil}` since there is nothing to debug. Use `ExclusiveArch: x86_64` if applicable. See `eza.spec` or `oh-my-posh.spec`.
  - **Tarball extraction:** Most pre-built binary tarballs are flat (no top-level directory), so use `%setup -c %{name}-%{version}` to wrap extraction in a named dir. If the tarball has a named top-level directory, use `%setup -n <dir-name>` instead (the dir name may include `%{_arch}` when the release asset embeds the architecture). For standard source tarballs following RPM naming conventions, use `%autosetup`.
- **Node.js packages:** Source from npmjs.org. Use `%{?nodejs_find_provides_and_requires}` or `%{?nodejs_default_filter}` and `ExclusiveArch: %{nodejs_arches}`. For pre-bundled packages, install the bundle directory directly to `%{nodejs_sitelib}/%{name}` and symlink entry points. (No example currently in the repo.)
- **Python packages:** Use `%pyproject_wheel` / `%pyproject_install` / `%pyproject_save_files` macros with `%generate_buildrequires`. Source0 pulls from `files.pythonhosted.org`. See `python-todoman.spec` or `python-fpdf2.spec`. `proselint.spec` shows `%prep` seds that patch upstream metadata.
- **Shell scripts:** Use `BuildArch: noarch`. See `wd.spec`.

### Changelog Format

Changelog entries must follow this exact format (author is always Chris Grau):
```text
* Day Mon DD YYYY Chris Grau <113591+sirhc@users.noreply.github.com> - <version>-<release>
- <description>
```
*Note: The `just update` recipe automatically generates this format and sets `Release` back to `1`. For manual packaging fixes without a version bump, edit the spec manually. Always check that the day-of-week abbreviation matches the actual date, and single-digit days are padded with a space (e.g., `Apr  7`, not `Apr 07`).*

### Upstream Update Detection

`just update-packages` walks every spec and decides the source of truth for versions:
- If `Source0` resolves to a `pythonhosted.org` URL, it queries the PyPI JSON API.
- Else if `URL:` is a github.com URL, it uses `just latest-release` (via `gh`).
- Otherwise the spec is skipped.

Version-comparison uses `sort -V`, so it also catches downgrades/mismatches, not just newer releases.

#### X-Update-Block directive

A spec may carry a comment line:

```text
# X-Update-Block: <version> <reason>
```

`update-packages` will then skip any upstream release **at or above** `<version>`. Use this when upstream ships a release the package can't take yet (e.g. `python-plotext.spec` blocks plotext 6, which breaks `python-textual-plotext`). Remove the directive once the blocker is resolved.

### Tool Requirements

Ensure the following tools are installed for full functionality:
- `rpmbuild`, `rpmdevtools` (for `spectool`, `rpmspec`)
- `copr-cli`
- `gh` (GitHub CLI)
- `jq`, `curl` (used for PyPI update checks)
- `just`
- `fd`, `fzf`, `gum`, `sponge` (from `moreutils`), `mlr` (Miller)

## Key Files

- `*.spec`: Individual RPM package definitions.
- `Justfile`: Contains all automation logic.
- `CLAUDE.md`: Additional technical guidance for AI assistants.
