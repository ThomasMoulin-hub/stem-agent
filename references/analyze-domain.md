---
name: Analyze Domain
code: AD
description: Scan the environment and identify the project domain and requirements.
---

# Analyze Domain

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
