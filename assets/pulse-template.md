# Pulse

## Environment Scan
- **Logic**: Periodically run `Analyze Domain` (AD) in headless mode.
- **Outcome**: If the domain report differs significantly from the current `DNA.json`, flag a "Genetic Drift" alert in `INDEX.md`.

## Snapshot Maintenance
- **Logic**: Check the `genetic_snapshots/` folder.
- **Outcome**: Keep the last 5 snapshots, delete older ones to prevent bloat.

## Proactive Evolution
- **Logic**: If "Genetic Drift" is high, draft a proposed mutation but do NOT apply it.
- **Outcome**: Present the draft to the owner at the start of the next interactive session.
