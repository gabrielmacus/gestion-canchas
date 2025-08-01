from fastapi import APIRouter, Query, Path, status
from typing import List, Optional

from apps.API.Controllers.Reserva.ReservaFindHandler import ReservaFindHandler
from apps.API.Controllers.Reserva.ReservaGetByIdHandler import ReservaGetByIdHandler
from apps.API.Controllers.Reserva.ReservaCreateHandler import ReservaCreateHandler
from apps.API.Controllers.Reserva.ReservaUpdateHandler import ReservaUpdateHandler
from apps.API.Controllers.Reserva.ReservaDeleteHandler import ReservaDeleteHandler

# Importar modelos de documentación
from apps.API.DTOs.SwaggerModels import (
    CrearReservaRequest, EditarReservaRequest, ReservaResponse, 
    ReservasPaginatedResponse, ErrorResponse, ValidationErrorResponse
)

reserva_router = APIRouter(
    prefix="/reservas", 
    tags=["📅 Reservas"],
    responses={
        400: {"model": ErrorResponse, "description": "Error de validación o datos inválidos"},
        404: {"model": ErrorResponse, "description": "Recurso no encontrado"},
        422: {"model": ValidationErrorResponse, "description": "Error de validación de campos"},
        500: {"model": ErrorResponse, "description": "Error interno del servidor"}
    }
)

reserva_router.add_api_route(
    path="/",
    endpoint=ReservaFindHandler().find,
    methods=["GET"],
    summary="🔍 Buscar y paginar reservas",
    description="""
    Busca reservas con filtros avanzados, ordenamiento y paginación.

    ### Parámetros de consulta disponibles:
    
    **Filtros (`filters[]`):**
    - `field`: nombre del campo (id, fecha_hora, duracion, cancha_id, jugador_id)
    - `operator`: operador de comparación (eq, neq, gt, gte, lt, lte, like, etc.)
    - `value`: valor a comparar
    
    **Ordenamiento (`orders[]`):**
    - `field`: campo por el que ordenar
    - `type`: asc (ascendente) o desc (descendente)
    
    **Paginación:**
    - `p.page`: número de página (por defecto: 1)
    - `p.size`: elementos por página (por defecto: 10)
    
    **Campos específicos (`fields[]`):**
    - Lista de campos específicos a incluir en la respuesta

    ### Ejemplos de uso:
    
    **Buscar reservas de una cancha específica:**
    ```
    GET /reservas?filters[0][field]=cancha_id&filters[0][operator]=eq&filters[0][value]=550e8400-e29b-41d4-a716-446655440000
    ```
    
    **Buscar reservas de un jugador:**
    ```
    GET /reservas?filters[0][field]=jugador_id&filters[0][operator]=eq&filters[0][value]=550e8400-e29b-41d4-a716-446655440001
    ```
    
    **Buscar reservas futuras:**
    ```
    GET /reservas?filters[0][field]=fecha_hora&filters[0][operator]=gt&filters[0][value]=2024-12-20T00:00:00
    ```
    
    **Buscar por duración específica:**
    ```
    GET /reservas?filters[0][field]=duracion&filters[0][operator]=eq&filters[0][value]=120
    ```
    
    **Ordenar por fecha más reciente:**
    ```
    GET /reservas?orders[0][field]=fecha_hora&orders[0][type]=desc
    ```
    """,
    response_model=ReservasPaginatedResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Lista paginada de reservas obtenida exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440002",
                                "fecha_hora": "2024-12-25T14:00:00",
                                "duracion": 120,
                                "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
                                "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440003",
                                "fecha_hora": "2024-12-25T16:00:00",
                                "duracion": 60,
                                "cancha_id": "550e8400-e29b-41d4-a716-446655440001",
                                "jugador_id": "550e8400-e29b-41d4-a716-446655440002"
                            }
                        ],
                        "pagination": {
                            "page": 1,
                            "size": 10,
                            "total": 50,
                            "total_pages": 5
                        }
                    }
                }
            }
        }
    }
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="🎯 Obtener reserva por ID",
    description="""
    Obtiene los detalles de una reserva específica por su ID único.
    
    ### Parámetros:
    - **id**: ID único de la reserva (formato UUID)
    
    ### Respuesta:
    Retorna los datos completos de la reserva si existe, incluyendo:
    - Fecha y hora de la reserva
    - Duración en minutos
    - IDs de la cancha y jugador asociados
    """,
    response_model=ReservaResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Reserva encontrada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440002",
                        "fecha_hora": "2024-12-25T14:00:00",
                        "duracion": 120,
                        "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
                        "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
                    }
                }
            }
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID '550e8400-e29b-41d4-a716-446655440002' no encontrada"
                    }
                }
            }
        }
    }
)

reserva_router.add_api_route(
    path="/",
    endpoint=ReservaCreateHandler().create,
    methods=["POST"],
    summary="➕ Crear nueva reserva",
    description="""
    Crea una nueva reserva en el sistema.
    
    ### Validaciones estrictas:
    
    **ID:**
    - Debe ser único en el sistema (formato UUID recomendado)
    
    **Fecha y hora:**
    - Debe ser mayor a la fecha/hora actual
    - No puede ser mayor a 3 meses desde ahora
    - Debe ser hora exacta (minutos y segundos deben ser 0)
    - Ejemplo válido: "2024-12-25T14:00:00"
    
    **Duración:**
    - Debe ser mayor a 0 minutos
    - Debe ser múltiplo de 60 minutos (solo horas completas)
    - Mínimo: 60 minutos (1 hora)
    - Máximo: 240 minutos (4 horas)
    - Valores válidos: 60, 120, 180, 240
    
    **Cancha y Jugador:**
    - Los IDs deben existir en el sistema
    - La cancha debe estar disponible en el horario solicitado
    
    ### Reglas de negocio:
    - No se pueden superponer reservas en la misma cancha
    - Se valida disponibilidad antes de crear la reserva
    - Si la cancha ya está reservada, retorna error específico
    """,
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Reserva creada exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Reserva creada exitosamente"}
                }
            }
        },
        400: {
            "description": "Error en los datos, ID duplicado o cancha no disponible",
            "content": {
                "application/json": {
                    "examples": {
                        "id_duplicado": {
                            "summary": "ID ya existe",
                            "value": {
                                "detail": "Ya existe una reserva con el ID especificado"
                            }
                        },
                        "cancha_reservada": {
                            "summary": "Cancha no disponible",
                            "value": {
                                "detail": "La cancha ya está reservada en el horario solicitado"
                            }
                        },
                        "cancha_no_existe": {
                            "summary": "Cancha no existe",
                            "value": {
                                "detail": "La cancha especificada no existe"
                            }
                        },
                        "jugador_no_existe": {
                            "summary": "Jugador no existe",
                            "value": {
                                "detail": "El jugador especificado no existe"
                            }
                        }
                    }
                }
            }
        },
        422: {
            "description": "Error de validación de campos",
            "content": {
                "application/json": {
                    "examples": {
                        "fecha_pasada": {
                            "summary": "Fecha en el pasado",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body", "fecha_hora"],
                                        "msg": "La fecha de la reserva no puede ser menor a la fecha actual",
                                        "type": "value_error"
                                    }
                                ]
                            }
                        },
                        "hora_inexacta": {
                            "summary": "Hora no exacta",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body", "fecha_hora"],
                                        "msg": "La hora de reserva debe ser exacta (minutos y segundos deben ser 0)",
                                        "type": "value_error"
                                    }
                                ]
                            }
                        },
                        "duracion_invalida": {
                            "summary": "Duración inválida",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body", "duracion"],
                                        "msg": "La duración de la reserva debe ser múltiplo de 60 minutos",
                                        "type": "value_error"
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaUpdateHandler().update,
    methods=["PATCH"],
    summary="✏️ Actualizar reserva",
    description="""
    Actualiza parcialmente una reserva existente.
    
    ### Parámetros:
    - **id**: ID único de la reserva a actualizar
    
    ### Campos actualizables:
    - **fecha_hora**: Nueva fecha y hora (mismas validaciones que creación)
    - **duracion**: Nueva duración en minutos (múltiplo de 60, 60-240)
    - **cancha_id**: Nuevo ID de cancha (debe existir y estar disponible)
    - **jugador_id**: Nuevo ID de jugador (debe existir)
    
    ### Comportamiento:
    - Solo se actualizan los campos proporcionados
    - Los campos no enviados mantienen su valor actual
    - Se aplican las mismas validaciones que en la creación
    - Se verifica disponibilidad de cancha si se cambia fecha/hora/cancha
    - No se pueden actualizar reservas del pasado
    
    ### Restricciones:
    - La reserva debe existir y no estar expirada
    - Si se cambia la cancha o fecha/hora, se valida disponibilidad
    - Se mantienen todas las reglas de negocio de creación
    """,
    response_model=None,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Reserva actualizada exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Reserva actualizada exitosamente"}
                }
            }
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID '550e8400-e29b-41d4-a716-446655440002' no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "Error de validación o conflicto de disponibilidad",
            "content": {
                "application/json": {
                    "examples": {
                        "reserva_expirada": {
                            "summary": "Reserva expirada",
                            "value": {
                                "detail": "No se puede actualizar una reserva expirada"
                            }
                        },
                        "conflicto_horario": {
                            "summary": "Conflicto de horario",
                            "value": {
                                "detail": "La cancha ya está reservada en el nuevo horario"
                            }
                        }
                    }
                }
            }
        }
    }
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaDeleteHandler().delete,
    methods=["DELETE"],
    summary="🗑️ Cancelar reserva",
    description="""
    Cancela (elimina) una reserva del sistema.
    
    ### Parámetros:
    - **id**: ID único de la reserva a cancelar
    
    ### Comportamiento:
    - Elimina permanentemente la reserva del sistema
    - Libera el horario para nuevas reservas
    - La operación no es reversible
    
    ### Restricciones:
    - La reserva debe existir
    - Dependiendo de las políticas, puede haber restricciones de tiempo
    - Algunos sistemas permiten cancelación solo con cierta antelación
    
    ### Nota importante:
    Esta operación libera inmediatamente el horario de la cancha.
    Considera implementar políticas de cancelación según las reglas de negocio.
    """,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {
            "description": "Reserva cancelada exitosamente"
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID '550e8400-e29b-41d4-a716-446655440002' no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "No se puede cancelar (políticas de cancelación)",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No se puede cancelar la reserva con menos de 2 horas de antelación"
                    }
                }
            }
        }
    }
) 