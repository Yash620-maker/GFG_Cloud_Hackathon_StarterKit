# Load Balancer Gym

_"Distribute incoming battles between Pokémon like a true Gym Leader."_

You will build a custom **load balancer** that routes requests to multiple backend services (Pokémon) based on your chosen strategy.

---

## Your Mission

- Implement a load balancer in **any language**
- Use one or more algorithms:
  - Round Robin
  - Least Connections
  - IP Hash
  - Your own (Speed stat / HP / custom scoring)
- Perform health checks and failover
- (Optional) Expose metrics / dashboard

This folder gives you a **Python example**, but you can ignore it and build your own in Node/Go/Rust/etc.

---

## Starter Contents

- `backend_service.py` — simple backend Pokémon service with random speed
- `load_balancer.py` — skeleton for a reverse proxy + strategy implementation
- `requirements.txt` — for Python example

You can:
- Run multiple backend instances on different ports
- Let `load_balancer.py` forward requests to them

---

## Example Flow (Python version)

In three terminals:

```bash
# Terminal 1
python backend_service.py 9001 --name Pikachu

# Terminal 2
python backend_service.py 9002 --name Bulbasaur

# Terminal 3
python load_balancer.py 8000 http://localhost:9001 http://localhost:9002
```

Then call:

```bash
curl http://localhost:8000/battle
```

Your implementation should distribute these "battles" among the backends.

---

## Bonus XP Ideas

* Add health checks so a "fainted" backend is removed
* Implement metrics (`/metrics`) endpoint on the LB
* Visualize stats in a dashboard or CLI TUI