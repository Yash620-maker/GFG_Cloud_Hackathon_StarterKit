# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(
#     title="PokéAPI Deployment Trial",
#     description="Sample API for the Pokémon Cloud/DevOps hackathon.",
# )

# class Pokemon(BaseModel):
#     name: str
#     type: List[str]
#     level: int

# @app.get("/pokemon/preview", response_model=Pokemon)
# def get_sample_pokemon():
#     return Pokemon(
#         name="Charmander",
#         type=["Fire"],
#         level=5,
#     )

# @app.get("/healthz")
# def health_check():
#     return {"status": "ok", "message": "PokéAPI is alive and ready!"}