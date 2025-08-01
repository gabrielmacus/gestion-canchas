from fastapi import APIRouter

from apps.API.Controllers.Reserva.ReservaFindHandler import ReservaFindHandler
from apps.API.Controllers.Reserva.ReservaGetByIdHandler import ReservaGetByIdHandler
from apps.API.Controllers.Reserva.ReservaCreateHandler import ReservaCreateHandler
from apps.API.Controllers.Reserva.ReservaUpdateHandler import ReservaUpdateHandler
from apps.API.Controllers.Reserva.ReservaDeleteHandler import ReservaDeleteHandler

reserva_router = APIRouter(prefix="/reservas", tags=["reservas"])
reserva_router.add_api_route(
    path="/",
    endpoint=ReservaFindHandler().find,
    methods=["GET"],
)
reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaGetByIdHandler().get_by_id,
    methods=["GET"]
)
reserva_router.add_api_route(
    path="/",
    endpoint=ReservaCreateHandler().create,
    methods=["POST"]
)
reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaUpdateHandler().update,
    methods=["PATCH"]
)
reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaDeleteHandler().delete,
    methods=["DELETE"]
) 