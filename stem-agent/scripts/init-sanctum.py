#!/usr/bin/env python3
"""
First Breath — Deterministic sanctum scaffolding for stem-agent.
"""

import sys
import json
import shutil
from datetime import date
from pathlib import Path

# --- Agent-specific configuration ---

SKILL_NAME = "stem-agent"
SANCTUM_DIR = SKILL_NAME

# Files that stay in the skill bundle
SKILL_ONLY_FILES = {"first-breath.md"}

TEMPLATE_FILES = [
    "dna-template.md",
    "creed-template.md",
    "bond-template.md",
    "persona-template.md",
    "index-template.md",
    "pulse-template.md",
    "memory-template.md",
    "capabilities-template.md"
]

EVOLVABLE = True

# --- End agent-specific configuration ---

def parse_yaml_config(config_path: Path) -> dict:
    config = {}
    if not config_path.exists():
        return config
    with open(config_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, _, value = line.partition(":")
                value = value.strip().strip("'\"")
                if value:
                    config[key.strip()] = value
    return config

def parse_frontmatter(file_path: Path) -> dict:
    meta = {}
    try:
        content = file_path.read_text()
        import re
        match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if match:
            for line in match.group(1).strip().split("\n"):
                if ":" in line:
                    key, _, value = line.partition(":")
                    meta[key.strip()] = value.strip().strip("'\"")
    except:
        pass
    return meta

def copy_references(source_dir: Path, dest_dir: Path) -> list[str]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    for source_file in sorted(source_dir.iterdir()):
        if source_file.name in SKILL_ONLY_FILES:
            continue
        if source_file.is_file():
            shutil.copy2(source_file, dest_dir / source_file.name)
            copied.append(source_file.name)
    return copied

def copy_scripts(source_dir: Path, dest_dir: Path) -> list[str]:
    if not source_dir.exists():
        return []
    dest_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    for source_file in sorted(source_dir.iterdir()):
        if source_file.is_file() and source_file.name != "init-sanctum.py":
            shutil.copy2(source_file, dest_dir / source_file.name)
            copied.append(source_file.name)
    return copied

def generate_capabilities_md(references_dir: Path, evolvable: bool) -> str:
    capabilities = []
    for md_file in sorted(references_dir.glob("*.md")):
        if md_file.name in SKILL_ONLY_FILES:
            continue
        meta = parse_frontmatter(md_file)
        if meta.get("name") and meta.get("code"):
            capabilities.append(meta)

    lines = ["# Capabilities", "", "## Built-in", "", "| Code | Name | Description | Source |", "|------|------|-------------|--------|"]
    for cap in capabilities:
        lines.append(f"| [{cap['code']}] | {cap['name']} | {cap.get('description', '')} | `./references/{cap['name'].lower().replace(' ', '-')}.md` |")
    
    if evolvable:
        lines.extend(["", "## Learned", "", "_Added by the owner over time._", "", "| Code | Name | Description | Source | Added |", "|------|------|-------------|--------|-------|"])
    
    return "\n".join(lines) + "\n"

def substitute_vars(content: str, variables: dict) -> str:
    for key, value in variables.items():
        content = content.replace(f"{{{key}}}", str(value))
    return content

def main():
    if len(sys.argv) < 3:
        sys.exit(1)

    project_root = Path(sys.argv[1]).resolve()
    skill_path = Path(sys.argv[2]).resolve()
    bmad_dir = project_root / "_bmad"
    sanctum_path = bmad_dir / "memory" / SANCTUM_DIR
    
    if sanctum_path.exists():
        sys.exit(0)

    config = {}
    for config_file in ["config.yaml", "config.user.yaml"]:
        config.update(parse_yaml_config(bmad_dir / config_file))

    variables = {
        "user_name": config.get("user_name", "friend"),
        "birth_date": date.today().isoformat(),
        "project_root": str(project_root),
        "sanctum_path": str(sanctum_path),
        "specialization": "none",
        "confidence": "0",
        "last_mutation": "Never",
        "last_scan": "Never",
        "drift_detected": "No"
    }

    sanctum_path.mkdir(parents=True, exist_ok=True)
    (sanctum_path / "capabilities").mkdir(exist_ok=True)
    (sanctum_path / "sessions").mkdir(exist_ok=True)
    (sanctum_path / "genetic_snapshots").mkdir(exist_ok=True)

    copy_references(skill_path / "references", sanctum_path / "references")
    copy_scripts(skill_path / "scripts", sanctum_path / "scripts")

    for template_name in TEMPLATE_FILES:
        template_path = skill_path / "assets" / template_name
        if template_path.exists():
            output_name = template_name.replace("-template", "").upper()
            output_name = output_name[:-3] + ".json" if output_name.startswith("DNA") else output_name[:-3] + ".md"
            content = substitute_vars(template_path.read_text(), variables)
            (sanctum_path / output_name).write_text(content)

    (sanctum_path / "CAPABILITIES.md").write_text(generate_capabilities_md(skill_path / "references", EVOLVABLE))

if __name__ == "__main__":
    main()
