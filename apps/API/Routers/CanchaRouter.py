from fastapi import APIRouter

from apps.API.Controllers.Cancha.CanchaFindHandler import CanchaFindHandler
from apps.API.Controllers.Cancha.CanchaGetByIdHandler import CanchaGetByIdHandler
from apps.API.Controllers.Cancha.CanchaCreateHandler import CanchaCreateHandler
from apps.API.Controllers.Cancha.CanchaUpdateHandler import CanchaUpdateHandler
from apps.API.Controllers.Cancha.CanchaDeleteHandler import CanchaDeleteHandler

cancha_router = APIRouter(prefix="/canchas", tags=["canchas"])

cancha_router.add_api_route(
    path= "/",
    endpoint=CanchaFindHandler().find,
    methods=["GET"],
    summary="Buscar canchas con paginación y filtros",
    description="""
    ## Buscar y filtrar canchas
    
    Permite buscar canchas con opciones avanzadas de filtrado, ordenamiento y paginación.
    
    ### Parámetros de consulta:
    - **fields**: Campos específicos a devolver (opcional)
    - **filters**: Filtros avanzados en formato JSON
    - **orders**: Ordenamiento en formato string
    - **p**: Parámetros de paginación (page_number, page_size)
    
    ### Ejemplos de filtros:
    ```json
    [
        {"field": "nombre", "operator": "contains", "value": "fútbol"},
        {"field": "techada", "operator": "eq", "value": true}
    ]
    ```
    
    ### Ejemplos de ordenamiento:
    ```string
    nombre:asc
    ```
    """,
)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="Obtener cancha por ID",
    description="""
    ## Obtener una cancha específica
    
    Recupera los detalles completos de una cancha utilizando su id.
    """,
)

cancha_router.add_api_route(
    path="/",
    endpoint=CanchaCreateHandler().create,
    methods=["POST"],
    summary="Crear nueva cancha",
    description="""
    ## Crear una nueva cancha
    
    Registra una nueva cancha en el sistema con validaciones automáticas.
    
    ### Datos requeridos:
    - **id**: UUID único para la cancha
    - **nombre**: Nombre descriptivo (3-100 caracteres)
    - **techada**: Indicador si la cancha está techada
    
    ### Validaciones:
    - El ID debe ser único en el sistema
    - El nombre debe tener entre 3 y 100 caracteres
    - El nombre se limpia automáticamente de espacios
    - La cancha seleccionada no debe tener una reserva activa para la fecha y hora seleccionadas
    
    """,

)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaUpdateHandler().update,
    methods=["PATCH"],
    summary="Actualizar cancha existente",
    description="""
    ## Actualizar una cancha existente
    
    Modifica los datos de una cancha existente. Solo se actualizan los campos proporcionados.
    """,

)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaDeleteHandler().delete,
    methods=["DELETE"],
    summary="Eliminar cancha",
    description="""
    ## Eliminar una cancha del sistema
    
    Elimina permanentemente una cancha del sistema.
    
    """
) 