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
    summary="Buscar reservas con filtros avanzados",
    description="""
    ## Buscar y filtrar reservas del sistema
    
    Permite buscar reservas con filtrado avanzado por múltiples criterios, incluyendo fechas, canchas y jugadores.
    
    ### Parámetros de consulta disponibles:
    - **fields**: Campos específicos a devolver (id, fecha_hora, duracion, cancha_id, jugador_id)
    - **filters**: Filtros avanzados en formato JSON
    - **orders**: Criterios de ordenamiento en formato string
    - **p**: Configuración de paginación (page_number, page_size)
    
    ### Filtros comunes para reservas:
    ```json
    [
        {"field": "fecha_hora", "operator": "gt", "value": "2024-01-15T10:00:00"},
        {"field": "cancha_id", "operator": "eq", "value": "550e8400-e29b-41d4-a716-446655440000"},
        {"field": "duracion", "operator": "gte", "value": 120}
    ]
    ```
    
    ### Ejemplos de ordenamiento:
    ```string
    fecha_hora:asc,duracion:desc
    ```
    """,
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="Obtener reserva específica por ID",
    description="""
    ## Obtener detalles completos de una reserva
    
    Recupera toda la información de una reserva específica incluyendo datos relacionados.
    
    ### Parámetros:
    - **id**: UUID de la reserva (requerido)
    
    ### Información devuelta:
    - **id**: Identificador único de la reserva
    - **fecha_hora**: Fecha y hora de inicio (formato ISO 8601)
    - **duracion**: Duración en minutos (múltiplos de 60)
    - **cancha_id**: ID de la cancha reservada
    - **jugador_id**: ID del jugador que hizo la reserva
    

    """,
)

reserva_router.add_api_route(
    path="/",
    endpoint=ReservaCreateHandler().create,
    methods=["POST"],
    summary="Crear nueva reserva de cancha",
    description="""
    ## Crear una nueva reserva de cancha
    
    Registra una nueva reserva en el sistema con validaciones automáticas de disponibilidad y conflictos.
    
    ### Datos requeridos:
    - **id**: UUID único para la reserva
    - **fecha_hora**: Fecha y hora de inicio (debe ser hora exacta, ej: 14:00:00)
    - **duracion**: Duración en minutos (múltiplos de 60, entre 60-240 min)
    - **cancha_id**: UUID de la cancha a reservar
    - **jugador_id**: UUID del jugador que realiza la reserva
    
    ### Validaciones automáticas del sistema:
    ✅ **Fecha futura**: No se permiten reservas en el pasado
    ✅ **Límite temporal**: Máximo 3 meses de anticipación
    ✅ **Hora exacta**: Solo horas completas (minutos y segundos en 0)
    ✅ **Duración válida**: Entre 1-4 horas, múltiplos de 60 minutos
    ✅ **Disponibilidad**: Verificación de conflictos con otras reservas
    ✅ **Existencia**: Validación de cancha y jugador existentes
    ✅ **ID único**: Verificación de duplicados
    
    ### Reglas de negocio:
    - **Horarios**: Solo se permiten reservas en horas exactas
    - **Duración mínima**: 1 hora (60 minutos)
    - **Duración máxima**: 4 horas (240 minutos)
    - **Anticipación máxima**: 3 meses desde la fecha actual
    - **Conflictos**: No se permiten superposiciones de horarios
    
    ### Ejemplo de reserva válida:
    ```json
    {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "fecha_hora": "2024-01-15T14:00:00",
        "duracion": 120,
        "cancha_id": "550e8400-e29b-41d4-a716-446655441111",
        "jugador_id": "550e8400-e29b-41d4-a716-446655442222"
    }
    ```
    """,
  
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaUpdateHandler().update,
    methods=["PATCH"],
    summary="Modificar reserva existente",
    description="""
    ## Modificar una reserva existente
    
    Actualiza parcialmente los datos de una reserva con validaciones automáticas de conflictos.
    
    ### Campos modificables:
    - **fecha_hora**: Nueva fecha/hora (debe cumplir todas las validaciones)
    - **duracion**: Nueva duración (60-240 minutos, múltiplos de 60)
    - **cancha_id**: Cambio de cancha (verificación de disponibilidad)
    - **jugador_id**: Transferir reserva a otro jugador
    

    
    ### Ejemplo de modificación:
    ```json
    {
        "fecha_hora": "2024-01-15T16:00:00",
        "duracion": 180
    }
    ```
    """,
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaDeleteHandler().delete,
    methods=["DELETE"],
    summary="Elminar reserva",
    description="""
    ## Cancelar una reserva existente
    
    Elimina una reserva existente del sistema.
    
    """,
) 