from dotenv import load_dotenv
import os
_ = load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.API.Routers.JugadorRouter import jugador_router
from apps.API.Routers.CanchaRouter import cancha_router
from apps.API.Routers.ReservaRouter import reserva_router

app = FastAPI()
app.include_router(jugador_router)
app.include_router(cancha_router)
app.include_router(reserva_router)

origin = os.getenv("ALLOWED_ORIGIN")
assert origin is not None

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
