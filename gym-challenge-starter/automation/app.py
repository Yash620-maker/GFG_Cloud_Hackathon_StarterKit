# import math
# import time
# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# @app.get("/")
# def index():
#     return {"message": "PokéCloud Automation Gym — CPU Stress App"}

# @app.get("/stress")
# def stress(seconds: int = 5):
#     """
#     Perform some useless CPU work for N seconds to simulate load.
#     """
#     end = time.time() + seconds
#     ops = 0
#     while time.time() < end:
#         math.sqrt(ops * ops + 1)
#         ops += 1
#     return {
#         "stressed_for_seconds": seconds,
#         "operations": ops,
#         "message": "Load simulated. Use me to test auto-scaling!"
#     }

# def main():
#     uvicorn.run(app, host="0.0.0.0", port=7000)

# if __name__ == "__main__":
#     main()