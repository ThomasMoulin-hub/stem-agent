---
name: Validate Transformation
code: VT
description: Run sanity checks and generate a Genetic Report on the recent transformation.
---

# Validate Transformation

## Outcome
An HTML Genetic Report that confirms the health of the specialized agent.

## What Success Looks Like
- "Before" and "After" personas are compared.
- Verification that the core "Evolution Logic" is still accessible.
- Sanity tests pass (e.g., "Can I still read my own CREED?", "Is my persona coherent?").

## Memory Integration
Save the test results to the session log.

## Tools
- `validate_dna.py`: Structural verification.
- `generate_genetic_report.py`: (Optional/Planned) Generates the HTML visualization.
