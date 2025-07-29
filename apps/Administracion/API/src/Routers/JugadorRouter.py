from fastapi import APIRouter
from Controllers.JugadorController import JugadorController

jugador_router = APIRouter(prefix="/jugadores", tags=["jugadores"])
jugador_controller = JugadorController()
jugador_router.add_api_route(
    path="/",
    endpoint=JugadorController.find,
    methods=["GET"]
)