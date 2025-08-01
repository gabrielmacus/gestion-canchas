from fastapi import APIRouter, Query, Path, status
from typing import List, Optional

from apps.API.Controllers.Jugador.JugadorFindHandler import JugadorFindHandler
from apps.API.Controllers.Jugador.JugadorGetByIdHandler import JugadorGetByIdHandler
from apps.API.Controllers.Jugador.JugadorCreateHandler import JugadorCreateHandler
from apps.API.Controllers.Jugador.JugadorUpdateHandler import JugadorUpdateHandler
from apps.API.Controllers.Jugador.JugadorDeleteHandler import JugadorDeleteHandler

# Importar modelos de documentación
from apps.API.DTOs.SwaggerModels import (
    CrearJugadorRequest, EditarJugadorRequest, JugadorResponse, 
    JugadoresPaginatedResponse, ErrorResponse, ValidationErrorResponse
)

jugador_router = APIRouter(
    prefix="/jugadores", 
    tags=["👤 Jugadores"],
    responses={
        400: {"model": ErrorResponse, "description": "Error de validación o datos inválidos"},
        404: {"model": ErrorResponse, "description": "Recurso no encontrado"},
        422: {"model": ValidationErrorResponse, "description": "Error de validación de campos"},
        500: {"model": ErrorResponse, "description": "Error interno del servidor"}
    }
)

jugador_router.add_api_route(
    path="/",
    endpoint=JugadorFindHandler().find,
    methods=["GET"],
    summary="🔍 Buscar y paginar jugadores",
    description="""
    Busca jugadores con filtros avanzados, ordenamiento y paginación.

    ### Parámetros de consulta disponibles:
    
    **Filtros (`filters[]`):**
    - `field`: nombre del campo (id, nombre, apellido, telefono, email)
    - `operator`: operador de comparación (eq, neq, like, etc.)
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
    
    **Buscar por nombre:**
    ```
    GET /jugadores?filters[0][field]=nombre&filters[0][operator]=like&filters[0][value]=Carlos
    ```
    
    **Buscar por email:**
    ```
    GET /jugadores?filters[0][field]=email&filters[0][operator]=eq&filters[0][value]=carlos@email.com
    ```
    
    **Ordenar por apellido:**
    ```
    GET /jugadores?orders[0][field]=apellido&orders[0][type]=asc
    ```
    
    **Buscar jugadores sin email:**
    ```
    GET /jugadores?filters[0][field]=email&filters[0][operator]=eq&filters[0][value]=null
    ```
    """,
    response_model=JugadoresPaginatedResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Lista paginada de jugadores obtenida exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440001",
                                "nombre": "Carlos",
                                "apellido": "García",
                                "telefono": "1234567890",
                                "email": "carlos.garcia@email.com"
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440002",
                                "nombre": "María",
                                "apellido": "López",
                                "telefono": "0987654321",
                                "email": None
                            }
                        ],
                        "pagination": {
                            "page": 1,
                            "size": 10,
                            "total": 15,
                            "total_pages": 2
                        }
                    }
                }
            }
        }
    }
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="🎯 Obtener jugador por ID",
    description="""
    Obtiene los detalles de un jugador específico por su ID único.
    
    ### Parámetros:
    - **id**: ID único del jugador (formato UUID)
    
    ### Respuesta:
    Retorna los datos completos del jugador si existe, incluyendo información de contacto.
    """,
    response_model=JugadorResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Jugador encontrado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "nombre": "Carlos",
                        "apellido": "García",
                        "telefono": "1234567890",
                        "email": "carlos.garcia@email.com"
                    }
                }
            }
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID '550e8400-e29b-41d4-a716-446655440001' no encontrado"
                    }
                }
            }
        }
    }
)

jugador_router.add_api_route(
    path="/",
    endpoint=JugadorCreateHandler().create,
    methods=["POST"],
    summary="➕ Crear nuevo jugador",
    description="""
    Crea un nuevo jugador en el sistema.
    
    ### Validaciones:
    - **ID**: Debe ser único en el sistema (formato UUID recomendado)
    - **Nombre**: Entre 3 y 100 caracteres, se eliminarán espacios extra
    - **Apellido**: Entre 3 y 100 caracteres, se eliminarán espacios extra
    - **Teléfono**: Solo dígitos, entre 7 y 15 caracteres (requerido)
    - **Email**: Formato válido (opcional, pero se requiere email O teléfono)
    
    ### Reglas de contacto:
    - Debe proporcionar al menos un teléfono O un email
    - Si se proporciona email, debe tener formato válido
    - El teléfono es obligatorio si no se proporciona email
    
    ### Comportamiento:
    - Si el ID ya existe, retorna error 400
    - Los nombres se procesan eliminando espacios al inicio y final
    - El teléfono se valida que contenga solo dígitos
    """,
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Jugador creado exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Jugador creado exitosamente"}
                }
            }
        },
        400: {
            "description": "Error en los datos o ID duplicado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Ya existe un jugador con el ID especificado"
                    }
                }
            }
        },
        422: {
            "description": "Error de validación de campos",
            "content": {
                "application/json": {
                    "examples": {
                        "nombre_invalido": {
                            "summary": "Nombre inválido",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body", "nombre"],
                                        "msg": "El nombre del jugador debe tener entre 3 y 100 caracteres",
                                        "type": "value_error"
                                    }
                                ]
                            }
                        },
                        "telefono_invalido": {
                            "summary": "Teléfono inválido",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body", "telefono"],
                                        "msg": "El teléfono debe contener solo dígitos",
                                        "type": "value_error"
                                    }
                                ]
                            }
                        },
                        "contacto_faltante": {
                            "summary": "Falta información de contacto",
                            "value": {
                                "detail": [
                                    {
                                        "loc": ["body"],
                                        "msg": "Debe proporcionar al menos un email o un teléfono",
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

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorUpdateHandler().update,
    methods=["PATCH"],
    summary="✏️ Actualizar jugador",
    description="""
    Actualiza parcialmente un jugador existente.
    
    ### Parámetros:
    - **id**: ID único del jugador a actualizar
    
    ### Campos actualizables:
    - **nombre**: Nuevo nombre (3-100 caracteres)
    - **apellido**: Nuevo apellido (3-100 caracteres)
    - **telefono**: Nuevo teléfono (7-15 dígitos)
    - **email**: Nuevo email (formato válido)
    
    ### Comportamiento:
    - Solo se actualizan los campos proporcionados
    - Los campos no enviados mantienen su valor actual
    - Se aplican las mismas validaciones que en la creación
    - Se mantiene la regla de contacto (email O teléfono requerido)
    """,
    response_model=None,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Jugador actualizado exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Jugador actualizado exitosamente"}
                }
            }
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID '550e8400-e29b-41d4-a716-446655440001' no encontrado"
                    }
                }
            }
        }
    }
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorDeleteHandler().delete,
    methods=["DELETE"],
    summary="🗑️ Eliminar jugador",
    description="""
    Elimina un jugador del sistema.
    
    ### Parámetros:
    - **id**: ID único del jugador a eliminar
    
    ### Comportamiento:
    - Elimina permanentemente el jugador del sistema
    - Si el jugador tiene reservas activas, puede fallar
    - La operación no es reversible
    
    ### Nota importante:
    Asegúrate de que no hay reservas activas antes de eliminar un jugador.
    Considera desactivar el jugador en lugar de eliminarlo si hay historial de reservas.
    """,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {
            "description": "Jugador eliminado exitosamente"
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID '550e8400-e29b-41d4-a716-446655440001' no encontrado"
                    }
                }
            }
        },
        400: {
            "description": "No se puede eliminar (reservas activas u otras restricciones)",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No se puede eliminar el jugador porque tiene reservas activas"
                    }
                }
            }
        }
    }
)