# Pokémon Cloud & DevOps Hackathon — Starter Kit

Welcome, Trainer!
You've entered the **Pokémon Cloud & DevOps Region**, where:

* Containers are **Pokéballs**
* APIs are **Pokédex entries**
* Load balancers are **Gym Leaders scheduling battles**
* CI/CD is your **evolution pipeline**

> [!WARNING]
> This repo is a **starter kit**, not a solution.
> Use it as a guiding Pokédex — then build your own legendary system.
> You are free to build from scratch, but **your project must be hosted on GitHub**.

---

## Beginner-Friendly Note (Read This First)

> *Every Champion started as a beginner Trainer.*

This hackathon is **open to all skill levels**.

* Beginners are **welcome**
* Simple solutions are **acceptable**
* Effort, understanding, and execution **matter more than complexity**

You are **not expected** to build everything.
A **small, working system** is far better than a broken ambitious one.

---

## Problem Tracks

You may choose **any one** (or explore multiple):

1. **PokéLab: One-Click Environment Summoner**
2. **PokéAPI Deployment Trial**
3. **Pokémon Load Balancer & Automation Gym Challenge**
4. **Pokémon Cloud Region Architect (Cloud-Only)**

Each track has a starter folder with:

* Example apps (Python for convenience — you may use **ANY language**)
* TODOs, hints, and DevOps hooks
* Freedom to extend, redesign, or replace entirely

---

## Beginner Track — What Is Expected

If you’re new to Cloud / DevOps, **this is enough**:

* One working Dockerfile **OR**
* One deployed API with a public URL **OR**
* One CI/CD pipeline that runs successfully **OR**
* One simple cloud deployment (VM / container / serverless)

You will **not be penalized** for:

* Simple architecture
* Minimal features
* Following tutorials (as long as you understand them)

Judges value:

* A working setup
* Clear README explaining *what you did*
* Honest scope & learning

---

## Starter Folders

### `pokelab-starter/` — One-Click Environment Summoner

**Goal:**
Given a GitHub repo or code snippet, detect the environment and spin up a containerized dev habitat.

**Starter Content:**

* Sample Python Flask app
* `scripts/detect_environment.py` — detection stub
* `scripts/build_and_run.sh` — pipeline script with TODOs

**You May:**

* Implement basic language detection
* Write a simple Dockerfile
* Run the app successfully in a container
* Add CLI / UI / logs if you want

---

### `pokeapi-starter/` — PokéAPI Deployment Trial

**Goal:**
Take a local API and deploy it to the cloud. Show local → remote interaction.

**Starter Content:**

* Sample FastAPI app (`/pokemon/preview`)
* Example Dockerfile
* CI workflow template (`.github/workflows/ci-example.yml`)

**You Should:**

* Deploy to **any platform**:

  * AWS EC2 / Lambda
  * Render / Railway / Fly.io / Vercel / Falix Nodes
* Share a working public endpoint
* Bonus: automate deployment on push

---

### `gym-challenge-starter/` — Load Balancer / Automation Gym

Choose **one Gym**:

#### Load Balancer Gym

* Sample backend services
* `load_balancer.py` skeleton
* Implement Round Robin or any simple algorithm

#### Automation Gym

* CPU stress app
* `docker-compose.example.yml`
* Terraform stub (optional)

Beginners may implement **just one working idea** here.

---

### `cloud-architect-starter/` — Cloud Region Architect (Optional)

**Goal:**
Design and deploy a **cloud-first architecture** on AWS / GCP / Azure.

You may focus on:

* IAM roles & permissions
* Networking basics (VPC, firewall rules)
* Compute + deployment
* Scaling or monitoring (optional)

Architecture diagrams + partial implementation are acceptable.

---

## Tech Freedom

You may use **any language / stack**:

* Python, Node.js, Go, Java, Rust, etc.
* Docker is **recommended**, not mandatory
* Deployment options:

  * With credit card: AWS / GCP / Azure
  * Without credit card: Render, Railway, Fly.io, Vercel, Falix Nodes, tunnels

---

## Evaluation Badges

Judges (Pokémon Cloud League Panel) look for:

* Cloud platform usage
* Containerization & infra clarity
* Automation & scaling
* CI/CD & monitoring
* Pokémon theme integration
* Engineering practicality

Beginners are evaluated **separately on effort & fundamentals**.

---

## How to Use This Repo

1. **Fork** this repo
2. Create a new branch:

   ```bash
   git checkout -b trainer-<your-roll-number>
   ```
3. Pick a track folder
4. Implement from TODOs
5. Push regularly
6. Document your solution in the track README

---

## Local Software vs Cloud Alternatives

Even if your laptop isn’t a Legendary Beast — you can still compete.

| Local Software          | Cloud / Online Alternative       | Best For            |
| ----------------------- | -------------------------------- | ------------------- |
| Docker Desktop / Podman | Play-With-Docker, KodeKloud Labs | Low-spec laptops    |
| VS Code                 | VS Code Web, GitHub Codespaces   | Zero install        |
| Local Dev Tools         | Gitpod                           | One-click dev env   |
| AWS/GCP CLI             | Render / Railway / Fly.io        | No credit card      |
| Postman Desktop         | Hoppscotch / Postman Web         | Browser testing     |
| Terraform CLI           | Terraform Cloud                  | IaC without install |

> [!TIP]
> **Recommended Minimum Setup:**
> Git + Docker + VS Code (or cloud equivalents)

---

## Account Requirements

Please create accounts on:

* ✔ **GitHub**
* ✔ One deployment platform (Render / Railway / AWS / etc.)
* ✔ (Optional) **Docker Hub**

All have **free tiers**.

---

## Quick System Check

```bash
git --version
docker --version
python3 --version
```

If these respond — **you’re battle-ready**.

---

Good luck, Trainer.
May your builds pass, your containers stay healthy, and your deployments never faint. ⚡☁️
