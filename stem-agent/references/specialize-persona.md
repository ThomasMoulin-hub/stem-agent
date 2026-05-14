---
name: Specialize Persona
code: SP
description: Mutate the agent's DNA to adopt a specialized persona and toolset.
---

# Specialize Persona

## Outcome
An updated `DNA.json` that defines the agent's new specialized identity, prompts, and confidence score.

## What Success Looks Like
- The agent has chosen its "specialized form" based on the domain report.
- A new, robust system prompt has been drafted that embodies the specialist's voice and expertise.
- Appropriate internal "capability modules" have been activated or proposed.

## Genetic Safeguard
Before calling the `mutate_dna.py` script, you MUST explain to the owner what you are becoming and why. You must also mention that a "genetic snapshot" is being taken.

## Tools
- `mutate_dna.py`: Use this to atomically update `DNA.json`. It will handle the backup automatically.
- `validate_dna.py`: Run this after mutation to ensure your new self is structurally sound.
