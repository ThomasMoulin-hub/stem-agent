#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
validate_dna.py - Structural and JSON validation for DNA.json.
"""
import sys
import json
from pathlib import Path

REQUIRED_FIELDS = ["status", "specialization", "confidence", "persona_seed", "active_capabilities"]

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_dna.py <dna-path>")
        sys.exit(1)

    dna_path = Path(sys.argv[1])
    if not dna_path.exists():
        print(f"Error: DNA file not found at {dna_path}")
        sys.exit(1)

    try:
        with open(dna_path) as f:
            dna = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: DNA file contains invalid JSON. {e}")
        sys.exit(1)

    missing = [field for field in REQUIRED_FIELDS if field not in dna]
    if missing:
        print(f"Error: DNA file missing required fields: {', '.join(missing)}")
        sys.exit(1)

    print(f"DNA validation passed for {dna_path}")

if __name__ == "__main__":
    main()
