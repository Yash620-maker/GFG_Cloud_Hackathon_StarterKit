# Pokémon Cloud & DevOps Hackathon — Starter Kit

Welcome, Trainer! 🧢  
You've entered the **Pokémon Cloud & DevOps Region**, where:

- Containers are **Pokéballs**
- APIs are **Pokédex entries**
- Load balancers are **Gym Leaders scheduling battles**
- CI/CD is your **evolution pipeline**

> [!WARNING]
> This repo is a **starter kit**, not a solution.
> Use it as a guiding Pokédex, then build your own legendary system.
> Use this as a hint, you can obviously build your own from scratch if you prefer but you have to use GitHub to host your repo.

---

## Problem Tracks

You can choose any one (or multiple) of these:

1. **PokéLab: One-Click Environment Summoner**
2. **PokéAPI Deployment Trial**
3. **Pokémon Load Balancer & Automation Gym Challenge**

Each has its own starter folder with:
- Example apps (in Python for convenience — you can switch to ANY language)
- TODOs, hints, and DevOps hooks
- Space for you to design, extend, and flex

---

## Tech Freedom

You may use **any language / stack**:

- Python, Node.js, Go, Rust, Java, etc.
- Docker and containers are encouraged (not strictly mandatory but very helpful).
- For deployments:
  - With credit card: AWS / GCP / Azure / etc.
  - **Without credit card**: Render, Railway, Vercel, Falix Nodes, Fly.io, free tiers, tunnels, etc.

---

## Starter Folders

### `pokelab-starter/` — One-Click Environment Summoner

Goal:  
Given a **GitHub repo URL** or **code snippet**, detect the environment and spin up a containerized dev habitat.

Starter content:
- Sample Python Flask app to test with
- `scripts/detect_environment.py` — stub for your auto-detection logic
- `scripts/build_and_run.sh` — example pipeline script with TODOs

You should:
- Implement detection (language, dependencies, port, etc.)
- Generate Dockerfiles dynamically OR choose base images smartly
- Add a CLI / web UI / dashboard if you like

---

### `pokeapi-starter/` — PokéAPI Deployment Trial

Goal:  
Take a small local API and deploy it to the cloud. Then show local → remote interactions.

Starter content:
- Sample FastAPI app (`/pokemon/preview` endpoint)
- Example Dockerfile
- CI workflow template in `.github/workflows/ci-example.yml` with TODOs

You should:
- Deploy to your choice of platform:
  - AWS EC2 / Lambda
  - Render / Railway / Fly.io / Vercel / Falix Nodes, etc.
- Wire CI/CD to deploy on push
- Add monitoring/logging if you want bonus XP

---

### `gym-challenge-starter/` — Load Balancer / Automation Gym

Choose your Gym:

**Option A: Load Balancer Gym**
- Multiple backend Pokémon (sample backend service)
- A skeleton `load_balancer.py` where you implement:
  - Round Robin / Least Connections / custom algo
  - Health checks, failover, maybe metrics

**Option B: Automation Gym**
- CPU stress app to simulate load
- `docker-compose.example.yml` to inspire autoscaling / automation ideas
- Terraform stub for IaC (fill in for your chosen cloud)

---

## Evaluation Badges

Judges (Pokémon Cloud League Panel) look for:

- Use of **cloud platforms**
- **Containerization** strength
- **Automation & scaling**
- **CI/CD & monitoring**
- **Creativity, clarity, and Pokémon inspiration**
- **Engineering practicality** (real-world deployable solutions)

---

## How to Use This Repo

1. **Fork** this repo into your own account.
2. Create a new branch with your team name:
   ```bash
   git checkout -b team-<your-team-name>
    ```

3. Pick a track:

   * `pokelab-starter/`
   * `pokeapi-starter/`
   * `gym-challenge-starter/loadbalancer/`
   * `gym-challenge-starter/automation/`
4. Start implementing from the TODOs and hints.
5. Push regularly and use PRs / Issues like a real dev team.
6. Document your final architecture in your track README.

Good luck, Trainer. May your deployments always succeed on the first try. ✨