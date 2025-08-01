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
    summary="Buscar jugadores con paginación y filtros",
    description="""
    ## Buscar y filtrar jugadores
    
    Permite buscar jugadores con filtrado avanzado por múltiples criterios, ordenamiento personalizado y paginación.
    
    ### Parámetros de consulta disponibles:
    - **fields**: Campos específicos a devolver (id, nombre, apellido, telefono, email)
    - **filters**: Filtros avanzados en formato JSON
    - **orders**: Criterios de ordenamiento en formato string
    - **p**: Configuración de paginación (page_number, page_size)
    
    ### Ejemplos de filtros comunes:
    ```json
    [
        {"field": "nombre", "operator": "contains", "value": "Juan"},
        {"field": "apellido", "operator": "starts_with", "value": "Pérez"},
        {"field": "email", "operator": "not_null", "value": null}
    ]
    
    ```
    
    ### Ejemplos de ordenamiento:
    ```string
    apellido:asc,nombre:asc
    ```
    """,
    responses={
      
    }
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="Obtener jugador por ID",
    description="""
    ## Obtener un jugador específico
    
    Recupera toda la información disponible de un jugador utilizando su identificador único.
    
    ### Parámetros:
    - **id**: UUID del jugador (requerido)
    
    ### Información devuelta:
    - **id**: Identificador único del jugador
    - **nombre**: Nombre del jugador (3-100 caracteres)
    - **apellido**: Apellido del jugador (3-100 caracteres)
    - **telefono**: Número de teléfono (7-15 dígitos)
    - **email**: Dirección de email (opcional)
    
    """,
    responses={
    }
)

jugador_router.add_api_route(
    path="/",
    endpoint=JugadorCreateHandler().create,
    methods=["POST"],
    summary="Registrar nuevo jugador",
    description="""
    ## Registrar un nuevo jugador
    
    Crea un nuevo registro de jugador en el sistema con validaciones completas de datos.
    
    ### Datos requeridos:
    - **id**: UUID único para el jugador
    - **nombre**: Nombre del jugador (3-100 caracteres, se limpia automáticamente)
    - **apellido**: Apellido del jugador (3-100 caracteres, se limpia automáticamente)
    - **telefono**: Número de teléfono (7-15 dígitos, solo números)
    - **email**: Dirección de email válida (opcional)
    
    ### Validaciones automáticas:
    ✅ **Nombre y apellido**: Entre 3 y 100 caracteres, espacios eliminados automáticamente
    ✅ **Teléfono**: Solo dígitos, entre 7 y 15 caracteres
    ✅ **Email**: Formato válido cuando se proporciona
    ✅ **Contacto**: Al menos teléfono o email debe estar presente
    ✅ **ID único**: Verificación de duplicados en el sistema
    
    ### Ejemplos de datos válidos:
    ```json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "nombre": "Juan Carlos",
        "apellido": "Pérez González",
        "telefono": "1123456789",
        "email": "juan.perez@email.com"
    }
    ```
    """
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorUpdateHandler().update,
    methods=["PATCH"],
    summary="Actualizar datos del jugador",
    description="""
    ## Actualizar información de un jugador
    
    Modifica parcialmente los datos de un jugador existente. Solo se actualizan los campos enviados.
    
    ### Campos modificables:
    - **nombre**: Nuevo nombre (3-100 caracteres)
    - **apellido**: Nuevo apellido (3-100 caracteres)
    - **telefono**: Nuevo teléfono (7-15 dígitos)
    - **email**: Nueva dirección de email (puede ser null)

    ```
    """
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorDeleteHandler().delete,
    methods=["DELETE"],
    summary="Eliminar jugador del sistema",
    description="""
    ## Eliminar un jugador del sistema
    
    Elimina permanentemente un jugador del sistema.
    """
)