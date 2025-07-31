from fastapi import APIRouter

from apps.API.Controllers.Cancha.CanchaFindHandler import CanchaFindHandler
from apps.API.Controllers.Cancha.CanchaCreateHandler import CanchaCreateHandler
from apps.API.Controllers.Cancha.CanchaUpdateHandler import CanchaUpdateHandler
from apps.API.Controllers.Cancha.CanchaDeleteHandler import CanchaDeleteHandler

cancha_router = APIRouter(prefix="/canchas", tags=["canchas"])
cancha_router.add_api_route(
    path="/",
    endpoint=CanchaFindHandler().find,
    methods=["GET"],
)
cancha_router.add_api_route(
    path="/",
    endpoint=CanchaCreateHandler().create,
    methods=["POST"]
)
cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaUpdateHandler().update,
    methods=["PATCH"]
)
cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaDeleteHandler().delete,
    methods=["DELETE"]
) 