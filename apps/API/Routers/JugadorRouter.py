from fastapi import APIRouter
from apps.API.Controllers.JugadorController import JugadorController

jugador_router = APIRouter(prefix="/jugadores", tags=["jugadores"])
jugador_controller = JugadorController()
jugador_router.add_api_route(
    path="/",
    endpoint=jugador_controller.find,
    methods=["GET"]
)
jugador_router.add_api_route(
    path="/",
    endpoint=jugador_controller.create,
    methods=["POST"]
)