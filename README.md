# AI Agent Guidelines

A framework for managing and distributing AI agent guidelines across multiple development tools and environments. This project helps standardize AI behavior across different platforms by maintaining a single source of truth for guidelines and automatically formatting them for each target environment.

## Overview

AI Agent Guidelines provides a centralized system for defining behavioral rules and guidelines that AI agents should follow. It supports multiple development environments including Cursor IDE, Claude CLI, and IntelliJ (planned), ensuring consistent AI behavior across different platforms.

## Features

- **Centralized Guidelines Management**: Store all guidelines in a single location
- **Multi-Platform Support**: Format and distribute guidelines for different development tools
  - [x] Cursor IDE support
  - [x] Claude CLI support
  - [ ] IntelliJ support (coming soon)
- **Declarative Configuration**: Simple YAML-based configuration of guidelines
- **Automatic Formatting**: Converts guidelines to the correct format for each target platform
- **Simple CLI Interface**: Easy to use command-line tools for managing guidelines

## Guidelines Included

The project currently includes the following guidelines:

- **UNIX Style Commit Message Rule**: Enforces consistent commit message formatting
- **Typo Checking**: Ensures code changes are free of typos
- **Grammar Checking**: Verifies proper grammar in code comments and documentation

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/ai-agent-guidelines.git
cd ai-agent-guidelines
```

Install dependencies:

```bash
make install-deps
```

## Usage

### Initialize Guidelines for All Supported Tools

```bash
make init
```

This command reads the guidelines from `docs/ai-agent-guidelines/` and formats them for each supported tool:

- Cursor IDE: Creates `.mdc` files in `.cursor/rules/`
- Claude CLI: Creates guidelines in `.claude/guidelines/` and sets up `claude.md`

### Clean Generated Files

```bash
make clean
```

This command removes all generated guideline files.

## How It Works

The system uses a simple workflow:

1. Guidelines are defined as Markdown files in `docs/ai-agent-guidelines/`
2. Configuration metadata is stored in `list_of_guideline.yml`
3. The `vendor_guideline.py` script processes each guideline and creates tool-specific formats
4. Each development tool reads guidelines from its specific location

### Configuration Format

Guidelines are configured in `docs/ai-agent-guidelines/list_of_guideline.yml`:

```yaml
list_of_guideline:
  - title: Unix style commit message 
    file: use_case_commit_message_unix_style-agent.md
    description: Description of the guideline
    always_use: true
```

Each guideline specifies:
- **title**: Short name of the guideline
- **file**: Markdown file containing the guideline content
- **description**: Detailed explanation of the guideline
- **always_use**: Whether the guideline should always be applied or only when requested

### Tool-Specific Formats

#### Cursor IDE

Guidelines for Cursor are formatted as `.mdc` files with metadata in a YAML frontmatter:

```
---
description: Description of the guideline
globs: *.*
alwaysApply: true
---

# Guideline Content
...
```

#### Claude CLI

Guidelines for Claude CLI are referenced in `.claude/guidelines/additional_instructions.md`:

```
## Additional Instructions

- MUST USE ALWAYS : Unix style commit message @use_case_commit_message_unix_style-agent.md
```

## Extending

To add a new guideline:

1. Create a markdown file in `docs/ai-agent-guidelines/`
2. Add its metadata to `list_of_guideline.yml`
3. Run `make init` to distribute it to all supported tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.