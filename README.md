# 🧬 Stem Agent Evolution Suite

A self-specializing AI agent that starts as a neutral "Observer" and evolves into a domain-specific assistant by analyzing your project's signals (file structure, tech stack, and user intent).

## 🚀 Zero-to-Specialist Installation

If you are starting from a completely empty project and don't have BMad installed, follow these steps:

### 1. Install BMad & Configure your IDE
Run the BMad installer. Follow the prompts to select your IDE (VS Code, JetBrains, etc.) and configure your environment.
```powershell
npx bmad-method install
```

### 2. Add the Stem Agent
Clone the Stem Agent repository directly into your project's `skills/` folder.
```powershell
mkdir skills
git clone https://github.com/ThomasMoulin-hub/stem-agent.git skills/stem-agent
```

### 3. Register the Module
Navigate into the agent's folder and run the self-installation command using the BMad package:
```powershell
cd skills/stem-agent
npx -p @google/gemini-cli bmad . install
```
*Note: This command uses `npx` to run the `bmad` tool from the `@google/gemini-cli` package, ensuring it works even if you haven't installed it globally.*

### 4. Return to Root & Awaken
Return to your project root and start the agent:
```powershell
cd ../..
npx -p @google/gemini-cli bmad stem-agent
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

