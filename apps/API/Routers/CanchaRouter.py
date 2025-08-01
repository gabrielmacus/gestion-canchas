from fastapi import APIRouter, Query, Path, status
from typing import List, Optional

from apps.API.Controllers.Cancha.CanchaFindHandler import CanchaFindHandler
from apps.API.Controllers.Cancha.CanchaGetByIdHandler import CanchaGetByIdHandler
from apps.API.Controllers.Cancha.CanchaCreateHandler import CanchaCreateHandler
from apps.API.Controllers.Cancha.CanchaUpdateHandler import CanchaUpdateHandler
from apps.API.Controllers.Cancha.CanchaDeleteHandler import CanchaDeleteHandler

# Importar modelos de documentación
from apps.API.DTOs.SwaggerModels import (
    CrearCanchaRequest, EditarCanchaRequest, CanchaResponse, 
    CanchasPaginatedResponse, ErrorResponse, ValidationErrorResponse
)

cancha_router = APIRouter(
    prefix="/canchas", 
    tags=["🏟️ Canchas"],
    responses={
        400: {"model": ErrorResponse, "description": "Error de validación o datos inválidos"},
        404: {"model": ErrorResponse, "description": "Recurso no encontrado"},
        422: {"model": ValidationErrorResponse, "description": "Error de validación de campos"},
        500: {"model": ErrorResponse, "description": "Error interno del servidor"}
    }
)

cancha_router.add_api_route(
    path="/",
    endpoint=CanchaFindHandler().find,
    methods=["GET"],
    summary="🔍 Buscar y paginar canchas",
    description="""
    Busca canchas con filtros avanzados, ordenamiento y paginación.

    ### Parámetros de consulta disponibles:
    
    **Filtros (`filters[]`):**
    - `field`: nombre del campo (id, nombre, techada)
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
    
    **Buscar canchas techadas:**
    ```
    GET /canchas?filters[0][field]=techada&filters[0][operator]=eq&filters[0][value]=true
    ```
    
    **Buscar por nombre:**
    ```
    GET /canchas?filters[0][field]=nombre&filters[0][operator]=like&filters[0][value]=Principal
    ```
    
    **Ordenar por nombre ascendente:**
    ```
    GET /canchas?orders[0][field]=nombre&orders[0][type]=asc
    ```
    """,
    response_model=CanchasPaginatedResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Lista paginada de canchas obtenida exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "data": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "nombre": "Cancha Principal",
                                "techada": True
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440001",
                                "nombre": "Cancha Secundaria",
                                "techada": False
                            }
                        ],
                        "pagination": {
                            "page": 1,
                            "size": 10,
                            "total": 25,
                            "total_pages": 3
                        }
                    }
                }
            }
        }
    }
)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaGetByIdHandler().get_by_id,
    methods=["GET"],
    summary="🎯 Obtener cancha por ID",
    description="""
    Obtiene los detalles de una cancha específica por su ID único.
    
    ### Parámetros:
    - **id**: ID único de la cancha (formato UUID)
    
    ### Respuesta:
    Retorna los datos completos de la cancha si existe.
    """,
    response_model=CanchaResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Cancha encontrada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "nombre": "Cancha Principal",
                        "techada": True
                    }
                }
            }
        },
        404: {
            "description": "Cancha no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Cancha con ID '550e8400-e29b-41d4-a716-446655440000' no encontrada"
                    }
                }
            }
        }
    }
)

cancha_router.add_api_route(
    path="/",
    endpoint=CanchaCreateHandler().create,
    methods=["POST"],
    summary="➕ Crear nueva cancha",
    description="""
    Crea una nueva cancha en el sistema.
    
    ### Validaciones:
    - **ID**: Debe ser único en el sistema (formato UUID recomendado)
    - **Nombre**: Entre 3 y 100 caracteres, se eliminarán espacios extra
    - **Techada**: Campo booleano que indica si la cancha está cubierta
    
    ### Comportamiento:
    - Si el ID ya existe, retorna error 400
    - El nombre se procesa eliminando espacios al inicio y final
    - La respuesta incluye el estado de la operación
    """,
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Cancha creada exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Cancha creada exitosamente"}
                }
            }
        },
        400: {
            "description": "Error en los datos o ID duplicado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Ya existe una cancha con el ID especificado"
                    }
                }
            }
        },
        422: {
            "description": "Error de validación de campos",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "nombre"],
                                "msg": "El nombre de la cancha debe tener entre 3 y 100 caracteres",
                                "type": "value_error"
                            }
                        ]
                    }
                }
            }
        }
    }
)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaUpdateHandler().update,
    methods=["PATCH"],
    summary="✏️ Actualizar cancha",
    description="""
    Actualiza parcialmente una cancha existente.
    
    ### Parámetros:
    - **id**: ID único de la cancha a actualizar
    
    ### Campos actualizables:
    - **nombre**: Nuevo nombre (3-100 caracteres)
    - **techada**: Nuevo estado de techado
    
    ### Comportamiento:
    - Solo se actualizan los campos proporcionados
    - Los campos no enviados mantienen su valor actual
    - Se aplican las mismas validaciones que en la creación
    """,
    response_model=None,
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Cancha actualizada exitosamente",
            "content": {
                "application/json": {
                    "example": {"message": "Cancha actualizada exitosamente"}
                }
            }
        },
        404: {
            "description": "Cancha no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Cancha con ID '550e8400-e29b-41d4-a716-446655440000' no encontrada"
                    }
                }
            }
        }
    }
)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaDeleteHandler().delete,
    methods=["DELETE"],
    summary="🗑️ Eliminar cancha",
    description="""
    Elimina una cancha del sistema.
    
    ### Parámetros:
    - **id**: ID único de la cancha a eliminar
    
    ### Comportamiento:
    - Elimina permanentemente la cancha del sistema
    - Si la cancha tiene reservas activas, puede fallar
    - La operación no es reversible
    
    ### Nota importante:
    Asegúrate de que no hay reservas activas antes de eliminar una cancha.
    """,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {
            "description": "Cancha eliminada exitosamente"
        },
        404: {
            "description": "Cancha no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Cancha con ID '550e8400-e29b-41d4-a716-446655440000' no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "No se puede eliminar (reservas activas u otras restricciones)",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No se puede eliminar la cancha porque tiene reservas activas"
                    }
                }
            }
        }
    }
) 