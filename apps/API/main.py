from dotenv import load_dotenv
_ = load_dotenv()

from fastapi import FastAPI
from apps.API.Routers.JugadorRouter import jugador_router
from apps.API.Routers.CanchaRouter import cancha_router
from apps.API.Routers.ReservaRouter import reserva_router

app = FastAPI()
app.include_router(jugador_router)
app.include_router(cancha_router)
app.include_router(reserva_router)

