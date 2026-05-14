# 🧬 Stem Agent Evolution Suite

A self-specializing AI agent that starts as a neutral "Observer" and evolves into a domain-specific assistant by analyzing your project's signals (file structure, tech stack, and user intent).

## 🚀 Installation (BMad Standard)

This agent is built using the **BMad Method**. It can be run by any BMad-compatible runner (Gemini CLI, Claude Code, etc.).

### 1. Initialize your BMad Project
If you haven't already, initialize BMad in your project root:
```powershell
npx bmad-method install
```

### 2. Add the Stem Agent
Clone the repository into your project's `skills/` folder:
```powershell
mkdir skills
git clone https://github.com/ThomasMoulin-hub/stem-agent.git skills/stem-agent
```

### 3. Register the Module (Tool-Agnostic)
Run the universal installation script. This registers the agent without needing a specific CLI tool:
```powershell
python skills/stem-agent/scripts/install_module.py
```

### 4. Awaken & Evolve
Start the agent using your preferred BMad runner:

**Using Gemini CLI:**
```powershell
bmad stem-agent
```

**Using Claude Code:**
```powershell
# Ensure you have the BMad plugin enabled, then:
cliserv stem-agent
```

## 🧬 How it Works

1. **Analysis**: The agent scans your project for "chemical signals" (file extensions, dependency manifests like `package.json`, and folder structures).
2. **Mutation**: Based on the scan, it proposes a specialized persona (e.g., "Rigorous QA Engineer", "Cloud Architect").
3. **DNA Update**: It atomically rewrites its own `DNA.json` to "lock in" the new identity and toolset.
4. **Safeguards**: It creates a genetic snapshot before every mutation. If a transformation fails sanity tests, it automatically reverts to its previous state.

## 🛠️ Autonomous Drift Detection
Once installed, the agent can run in the background. If you significantly change your project's tech stack, it will detect the "Genetic Drift" and suggest a new evolution at the start of your next session.

---
## ❓ What is BMad?

**BMad** (Benchmark-Driven, Modular, Agentic Design) is an open-source framework and methodology for building specialized AI agents and automated workflows. Unlike generic chatbots, BMad agents are **outcome-driven**, meaning they focus on achieving specific goals through a structured "Sanctum" of memory, persona, and deterministic tools.

For more information, visit the official repository:
👉 [BMad Method Repository](https://github.com/bmad-method/bmad)

