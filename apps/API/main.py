from dotenv import load_dotenv
_ = load_dotenv()

from fastapi import FastAPI
from apps.API.Routers.JugadorRouter import jugador_router

app = FastAPI()
app.include_router(jugador_router)