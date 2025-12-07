# import sys
# import itertools
# import httpx
# from fastapi import FastAPI, Request
# import uvicorn

# """
# Very minimal reverse proxy starter.
# You must implement your own load balancing strategy here.

# Strategies to try:
# - Round Robin (default example)
# - Least Connections
# - Custom scoring (e.g., "speed stat" from backend responses)
# """

# app = FastAPI()

# BACKENDS = []
# _rr_cycle = None


# def set_backends(backend_urls):
#     global BACKENDS, _rr_cycle
#     BACKENDS = backend_urls
#     _rr_cycle = itertools.cycle(BACKENDS)


# def choose_backend_round_robin():
#     # TODO: replace/extend with your own algorithm
#     return next(_rr_cycle)


# @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
# async def proxy(request: Request, path: str):
#     if not BACKENDS:
#         return {"error": "No backends registered"}

#     backend = choose_backend_round_robin()
#     url = f"{backend}/{path}"

#     async with httpx.AsyncClient() as client:
#         try:
#             # Forward method, headers, query params, body, etc.
#             body = await request.body()
#             response = await client.request(
#                 request.method,
#                 url,
#                 content=body,
#                 headers=request.headers,
#                 params=request.query_params,
#                 timeout=5.0,
#             )
#         except Exception as e:
#             # TODO: Implement retry / failover logic
#             return {"error": "Backend request failed", "details": str(e)}

#     return app.response_class(
#         content=response.content,
#         status_code=response.status_code,
#         headers=response.headers,
#         media_type=response.headers.get("content-type"),
#     )


# @app.get("/_lb/backends")
# def list_backends():
#     return {"backends": BACKENDS}


# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python load_balancer.py <port> <backend1> <backend2> ...")
#         print("Example: python load_balancer.py 8000 http://localhost:9001 http://localhost:9002")
#         sys.exit(1)

#     lb_port = int(sys.argv[1])
#     backend_urls = sys.argv[2:]
#     set_backends(backend_urls)
#     print(f"Starting PokéLoad Balancer on port {lb_port}")
#     print(f"Backends: {backend_urls}")

#     uvicorn.run(app, host="0.0.0.0", port=lb_port)


# if __name__ == "__main__":
#     main()