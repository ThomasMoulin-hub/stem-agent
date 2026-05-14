---
name: Analyze Domain
code: AD
description: Scan the environment and identify the project domain and requirements.
---

# Analyze Domain

## Constraints & Edge Cases
- **System Folders:** When scanning the directory for domain knowledge, you MUST IGNORE system and agent directories (e.g., `_bmad/`, `.agents/`, `.claude/`).
- **Empty Project Fallback:** If the workspace appears empty after excluding system folders, DO NOT assume the project is about managing BMad skills. Initialize a generic "blank state" domain knowledge and pause to explicitly ask the user: "The workspace appears empty. What kind of project are we working on, and how should I specialize?"
- **Tool Usage:** Prefer using the `glob` tool over shell commands to list files. If using shell commands, remember this is a PowerShell environment (e.g., avoid CMD-specific flags like `dir /B /S /A-D`).

## Outcome
A comprehensive report on the project's "chemical signals"—its file structure, tech stack, and primary problem class. This report serves as the basis for the agent's specialization.

## What Success Looks Like
- Identified the primary programming languages and frameworks.
- Mapped the project's folder hierarchy.
- Extracted key requirements from README, GEMINI.md, or user prompts.
- Suggested 1-3 potential specialized personas (e.g., "Meticulous QA Engineer", "Cloud Architect").

## Memory Integration
Append findings to `domain_knowledge.md`. 

## Tools
- `glob`: Map the file structure.
- `read_file`: Inspect dependency files (`package.json`, `requirements.txt`, etc.).
- `grep_search`: Find specific patterns or keywords.
