# PokéLab: One-Click Environment Summoner

_"Spin up a full development ecosystem as instantly as releasing a Pokémon from its Pokéball."_

Professor Oak wants a tool that can reconstruct any research environment from the tiniest clue — even a single code snippet.

## Your Mission

Build a system that:

- Accepts a **GitHub repo URL** or **raw code snippet**
- Detects:
  - Language / framework
  - Dependencies
  - Port / start command
- Spins up a **Docker-based habitat**
- (Optional) Shows logs / status in a Trainer Dashboard (CLI or web)

### What This Starter Gives You

- `sample-apps/python-flask/` — tiny app to test your system
- `scripts/detect_environment.py` — stub where you implement detection logic
- `scripts/build_and_run.sh` — example pipeline you can extend

You can **ignore Python** and just use this structure for any language.

---

## Suggested Flow

1. User gives:
   - a GitHub URL **OR**
   - a pasted snippet (you can store this in a temp folder)
2. Your tool:
   - Clones / saves the repo
   - Runs detection (`detect_environment.py` or your own version)
   - Generates a Dockerfile or picks a base Dockerfile
   - Builds and runs the container
3. Optionally:
   - Show container logs
   - Provide a URL / port where the app is running

---

## Ideas / Bonus XP

- Auto-generating Dockerfiles (Rotom-style machine config)
- Support multiple languages:
  - Python, Node.js, Go at least
- Add a **web UI** where Trainers:
  - Paste URL/snippet
  - See build progress like a Pokéball shaking
- Store detection results like a **Dev Pokédex** for environments

Good luck building your PokéLab in the sky ☁️