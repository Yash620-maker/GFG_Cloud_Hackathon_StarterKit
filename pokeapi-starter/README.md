# PokéAPI Deployment Trial

_"Release your local code creature into the global Pokémon Network."_

Your job: take a tiny local API and deploy it into a remote arena (cloud platform), then battle-test it from your local machine.

## Your Mission

- Build or extend the sample API
- Containerize it (optional but recommended)
- Deploy to any of:
  - AWS EC2 / Lambda
  - Render / Railway / Fly.io / Vercel / Falix Nodes
  - Or via Nginx / Cloudflare Tunnel
- Show local -> remote interaction using curl, HTTP client, or a small script

---

## What This Starter Gives You

- `sample-api/python-fastapi/main.py` — tiny Pokémon-themed API
- `Dockerfile.example` — container example
- Root `.github/workflows/ci-example.yml` — add a deploy job here

You can:
- Replace Python with your own language
- Keep the API shape similar (e.g., `/pokemon/...` routes)
- Use this folder as a template only

---

## Example Flow

1. Run the API locally:
   ```bash
   cd sample-api/python-fastapi
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

2. Deploy to cloud:

   * Use Render / Railway / Vercel if you don't have a credit card
   * Or use any cloud VM / serverless

3. From your laptop / local environment:

   ```bash
   curl https://your-api-host/pokemon/preview
   ```

4. Capture logs / screenshots for your submission.

---

## Bonus XP Ideas

* Add health checks (`/healthz`)
* Add `/metrics` endpoint or integrate Prometheus-like stats
* Implement:

  * Retries
  * Latency measurement
  * Failover between two deployments (multi-region Pokémon)

Train your API until it’s worthy of the Pokémon Cloud League 🏆