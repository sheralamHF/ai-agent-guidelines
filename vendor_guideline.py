#!/usr/bin/env python3
import os
import yaml
import shutil


def init():
    """
    Initialize vendor-specific guideline files based on the list_of_guideline.yml.
    
    This function reads the guideline configuration file and formats the guidelines
    for different development tools (Cursor, Claude-CLI, and IntelliJ).
    """
    # Development tools we support
    dev_tools = ["cursor", "claude-cli", "intelij"]
    
    # Path to the guidelines configuration file
    config_path = "docs/ai-agent-guidelines/list_of_guideline.yml"
    
    # Read the configuration file
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    
    # Process each guideline for each development tool
    for guideline in config.get("list_of_guideline", []):
        title = guideline.get("title", "")
        filename = guideline.get("file", "")
        description = guideline.get("description", "")
        always_use = guideline.get("always_use", False)
        
        # Full path to the guideline file
        file_path = os.path.join("docs/ai-agent-guidelines", filename)
        
        # Read the content of the guideline file
        try:
            with open(file_path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Warning: File not found: {file_path}")
            continue
        
        # Process for each development tool
        for tool in dev_tools:
            if tool == "cursor":
                process_for_cursor(filename, content, description, always_use)
            elif tool == "claude-cli":
                process_for_claude_cli(filename, content, title, always_use)
            elif tool == "intelij":
                # To be implemented later
                print("IntelliJ implementation will be added later")


def process_for_cursor(filename, content, description, always_use):
    """Process guidelines for Cursor IDE"""
    # Create the .cursor/rules directory if it doesn't exist
    cursor_dir = os.path.join(".cursor", "rules")
    os.makedirs(cursor_dir, exist_ok=True)
    
    # Create the .mdc file with the same name
    mdc_filename = os.path.splitext(filename)[0] + ".mdc"
    mdc_path = os.path.join(cursor_dir, mdc_filename)
    
    # Prepare the template content
    template = f"""---
description: {description}
globs: "**.*"
alwaysApply: {str(always_use).lower()}
---

{content}"""
    
    # Write the content to the file
    with open(mdc_path, "w") as file:
        file.write(template)
    
    print(f"Created/Updated Cursor guideline: {mdc_path}")


def process_for_claude_cli(filename, content, title, always_use):
    """Process guidelines for Claude CLI"""
    # Create .claude/guidelines directory if it doesn't exist
    claude_dir = os.path.join(".claude", "guidelines")
    os.makedirs(claude_dir, exist_ok=True)
    
    # Create claude.md if it doesn't exist, or append to it
    claude_md_path = "claude.md"
    if not os.path.exists(claude_md_path):
        with open(claude_md_path, "w") as file:
            file.write("## Additional Instructions\n")
            file.write("- Must look for Additional Instructions @.claude/guidelines/additional_instructions.md\n")
    
    # Create additional_instructions.md if it doesn't exist
    additional_instructions_path = os.path.join(claude_dir, "additional_instructions.md")
    if not os.path.exists(additional_instructions_path):
        with open(additional_instructions_path, "w") as file:
            file.write("# Additional Instructions\n\n")
    
    # Copy the guideline file to the Claude guidelines directory
    guideline_dest_path = os.path.join(claude_dir, filename)
    with open(guideline_dest_path, "w") as file:
        file.write(content)
    
    # Determine directive based on always_use flag
    directive = "MUST USE ALWAYS" if always_use else "Use when specified in prompt"
    
    # Update the additional_instructions.md file with the new guideline reference
    with open(additional_instructions_path, "r") as file:
        existing_content = file.read()
    
    # Check if this guideline is already in the file
    new_line = f"- {directive} : {title} @{filename}"
    
    # Create a new content with updated or new guideline
    updated = False
    lines = existing_content.split("\n")
    for i, line in enumerate(lines):
        if filename in line:
            lines[i] = new_line
            updated = True
            break
    
    if not updated:
        lines.append(new_line)
    
    # Write back the updated content
    with open(additional_instructions_path, "w") as file:
        file.write("\n".join(lines))
    
    print(f"Created/Updated Claude CLI guideline: {guideline_dest_path}")


# If this script is run directly, call the init function
if __name__ == "__main__":
    init() 