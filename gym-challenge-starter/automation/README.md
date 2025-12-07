# PokéCloud Automation Gym

_"Automate an entire tech region like a Rotom taking over a Power Plant."_

In this gym, you design an **automation system** for cloud resources.

---

## Your Mission

Pick one (or more) of these:

- Auto-scale containers based on CPU load
- Event-driven CI/CD triggered by repo updates
- Automated backups & notifications for an app
- Or your own Cloud/DevOps automation idea

---

## Starter Contents

- `cpu_stress_app.py` — simple app to simulate CPU load
- `docker-compose.example.yml` — hint for multi-service setups

You can:
- Run the stress app in containers
- Feed metrics into your autoscaler or scripts
- Use GitHub Actions + webhooks to trigger deployments

---

## Example Idea (Not mandatory)

1. Run `cpu_stress_app.py` in container(s).
2. Collect CPU usage using:
   - Docker stats
   - Cloud metrics
3. Have a script:
   - Scale services up/down (e.g., `docker compose up --scale app=3`)
   - Or update replicas in Kubernetes / ECS / etc.
4. Alert Trainer (email/Discord/Slack) when load crosses threshold.

---

## Bonus XP Ideas

- Represent scaling events as "Pokémon evolving" in logs
- Use Terraform to:
  - Create infrastructure on any cloud
  - Destroy it cleanly when done
- Add a dashboard (web or CLI) to show the region's health