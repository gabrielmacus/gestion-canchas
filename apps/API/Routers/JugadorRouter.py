from fastapi import APIRouter

from apps.API.Controllers.Jugador.JugadorFindHandler import JugadorFindHandler
from apps.API.Controllers.Jugador.JugadorGetByIdHandler import JugadorGetByIdHandler
from apps.API.Controllers.Jugador.JugadorCreateHandler import JugadorCreateHandler
from apps.API.Controllers.Jugador.JugadorUpdateHandler import JugadorUpdateHandler
from apps.API.Controllers.Jugador.JugadorDeleteHandler import JugadorDeleteHandler

jugador_router = APIRouter(prefix="/jugadores", tags=["jugadores"])
jugador_router.add_api_route(
    path="/",
    endpoint=JugadorFindHandler().find,
    methods=["GET"],
)
jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorGetByIdHandler().get_by_id,
    methods=["GET"]
)
jugador_router.add_api_route(
    path="/",
    endpoint=JugadorCreateHandler().create,
    methods=["POST"]
)
jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorUpdateHandler().update,
    methods=["PATCH"]
)
jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorDeleteHandler().delete,
    methods=["DELETE"]
)