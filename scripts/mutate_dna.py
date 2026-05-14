#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
mutate_dna.py - Atomically updates DNA.json and creates genetic snapshots.
"""
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

def main():
    if len(sys.argv) < 3:
        print("Usage: mutate_dna.py <sanctum-path> <new-dna-json>")
        sys.exit(1)

    sanctum_path = Path(sys.argv[1])
    dna_path = sanctum_path / "DNA.json"
    snapshot_dir = sanctum_path / "genetic_snapshots"
    snapshot_dir.mkdir(exist_ok=True)

    try:
        new_dna = json.loads(sys.argv[2])
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON provided. {e}")
        sys.exit(1)

    # Take snapshot of current DNA if it exists
    if dna_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_path = snapshot_dir / f"dna_{timestamp}.bak"
        shutil.copy2(dna_path, snapshot_path)
        print(f"Snapshot created: {snapshot_path}")

    # Write new DNA
    with open(dna_path, 'w') as f:
        json.dump(new_dna, f, indent=2)
    
    print(f"DNA mutated successfully at {dna_path}")

if __name__ == "__main__":
    main()
