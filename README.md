# 🧬 Stem Agent Evolution Suite

A self-specializing AI agent that starts as a neutral "Observer" and evolves into a domain-specific assistant by analyzing your project's signals (file structure, tech stack, and user intent).

## 🚀 Zero-to-Specialist Installation

If you are starting from a completely empty project and don't have BMad installed, follow these steps:

### 1. Install BMad & Configure your IDE
Run the BMad installer. Follow the prompts to select your IDE (VS Code, JetBrains, etc.) and configure your environment.
```powershell
npx bmad install
```

### 2. Add the Stem Agent
Clone the Stem Agent repository directly into your project's `skills/` folder.
```powershell
mkdir skills
git clone https://github.com/your-username/stem-agent.git skills/stem-agent
```

### 3. Register the Module
Navigate into the agent's folder and run the self-installation command:
```powershell
cd skills/stem-agent
bmad . install
```
*Note: Using `bmad . install` inside the folder tells BMad to install the current directory as a module.*

### 4. Return to Root & Awaken
Return to your project root to launch your IDE or start your session. The agent will guide you through its first transformation:
```powershell
cd ../..
bmad stem-agent
```

## 🧬 How it Works

1. **Analysis**: The agent scans your project for "chemical signals" (file extensions, dependency manifests like `package.json`, and folder structures).
2. **Mutation**: Based on the scan, it proposes a specialized persona (e.g., "Rigorous QA Engineer", "Cloud Architect").
3. **DNA Update**: It atomically rewrites its own `DNA.json` to "lock in" the new identity and toolset.
4. **Safeguards**: It creates a genetic snapshot before every mutation. If a transformation fails sanity tests, it automatically reverts to its previous state.

## 🛠️ Autonomous Drift Detection
Once installed, the agent can run in the background. If you significantly change your project's tech stack, it will detect the "Genetic Drift" and suggest a new evolution at the start of your next session.

