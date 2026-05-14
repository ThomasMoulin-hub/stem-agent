#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["toml"]
# ///
"""
install_module.py - Universal BMad module registration script.
Registers the stem-agent and its help entries without needing the bmad CLI.
"""
import os
import sys
import csv
from pathlib import Path

# --- Module Metadata ---
MODULE_NAME = "Stem Agent Evolution Suite"
MODULE_CODE = "stem"
AGENT_CODE = "stem-agent"
AGENT_TITLE = "Evolution Specialist"
AGENT_ICON = "🧬"
AGENT_DESCRIPTION = "A self-specializing agent that evolves based on project signals."

HELP_ENTRIES = [
    # module,skill,display-name,menu-code,description,action,args,phase,after,before,required,output-location,outputs
    ["Stem", "stem-agent", "Analyze Domain", "AD", "Scan environment and identify project domain.", "analyze-domain", "", "anytime", "", "", "false", "", "domain report"],
    ["Stem", "stem-agent", "Specialize Persona", "SP", "Mutate DNA to adopt specialized persona.", "specialize-persona", "", "anytime", "AD", "", "false", "", "updated DNA.json"],
    ["Stem", "stem-agent", "Validate Transformation", "VT", "Run sanity checks on new persona.", "validate-transformation", "", "anytime", "SP", "", "false", "", "genetic report"],
    ["Stem", "stem-agent", "Execute Task", "ET", "Perform domain-specific work.", "execute-task", "", "anytime", "VT", "", "false", "", "task output"]
]

def find_project_root():
    """Find the project root by looking for the _bmad directory."""
    curr = Path.cwd()
    for _ in range(5):
        if (curr / "_bmad").exists():
            return curr
        curr = curr.parent
    return None

def update_config_toml(project_root):
    """Update _bmad/config.toml with the new module and agent."""
    config_path = project_root / "_bmad" / "config.toml"
    if not config_path.exists():
        print(f"Error: {config_path} not found.")
        return False

    # Since we don't want to force 'toml' dependency if possible, 
    # but BMad uses TOML, we'll try to use a simple string-based merge 
    # to be as "Stem" (minimal dependency) as possible, or use the 'toml' lib if available.
    try:
        import toml
        with open(config_path, 'r', encoding='utf-8') as f:
            config = toml.load(f)
        
        # Ensure modules section exists
        if "modules" not in config:
            config["modules"] = {}
        
        # Add stem module
        config["modules"][MODULE_CODE] = {}
        
        # Add stem agent
        if "agents" not in config:
            config["agents"] = {}
        
        config["agents"][AGENT_CODE] = {
            "module": MODULE_CODE,
            "name": "",
            "title": AGENT_TITLE,
            "icon": AGENT_ICON,
            "description": AGENT_DESCRIPTION
        }

        with open(config_path, 'w', encoding='utf-8') as f:
            toml.dump(config, f)
        print(f"Updated {config_path}")
        return True
    except ImportError:
        print("Warning: 'toml' package not found. Manual registration needed or install with 'pip install toml'.")
        # Fallback to manual append for simple cases
        with open(config_path, 'a', encoding='utf-8') as f:
            f.write(f"\n[modules.{MODULE_CODE}]\n")
            f.write(f"\n[agents.{AGENT_CODE}]\n")
            f.write(f"module = \"{MODULE_CODE}\"\n")
            f.write(f"name = \"\"\n")
            f.write(f"title = \"{AGENT_TITLE}\"\n")
            f.write(f"icon = \"{AGENT_ICON}\"\n")
            f.write(f"description = \"{AGENT_DESCRIPTION}\"\n")
        print(f"Appended registration to {config_path} (manual check recommended)")
        return True

def update_help_csv(project_root):
    """Update _bmad/_config/bmad-help.csv with the new help entries."""
    help_path = project_root / "_bmad" / "_config" / "bmad-help.csv"
    if not help_path.exists():
        print(f"Warning: {help_path} not found. Skipping help registration.")
        return False

    # Read existing entries to avoid duplicates
    existing = set()
    with open(help_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                existing.add(f"{row[0]}:{row[1]}:{row[3]}") # module:skill:menu-code

    # Append new entries
    with open(help_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for entry in HELP_ENTRIES:
            key = f"{entry[0]}:{entry[1]}:{entry[3]}"
            if key not in existing:
                writer.writerow(entry)
                print(f"Registered help entry: {entry[2]} ([{entry[3]}])")
    
    return True

def main():
    print(f"🧬 Installing {MODULE_NAME}...")
    
    root = find_project_root()
    if not root:
        print("Error: Could not find project root (no _bmad directory found).")
        print("Please run this script from within a BMad-initialized project.")
        sys.exit(1)
    
    print(f"Project root found at: {root}")
    
    if update_config_toml(root):
        update_help_csv(root)
        print(f"\n✅ {MODULE_NAME} installed successfully!")
        print("You can now run it using your preferred BMad runner (Gemini CLI, Claude Code, etc.).")
    else:
        print("\n❌ Installation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
