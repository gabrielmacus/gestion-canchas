from fastapi import APIRouter, Query, Path, status
from typing import Optional

from apps.API.Controllers.Cancha.CanchaFindHandler import CanchaFindHandler
from apps.API.Controllers.Cancha.CanchaGetByIdHandler import CanchaGetByIdHandler
from apps.API.Controllers.Cancha.CanchaCreateHandler import CanchaCreateHandler
from apps.API.Controllers.Cancha.CanchaUpdateHandler import CanchaUpdateHandler
from apps.API.Controllers.Cancha.CanchaDeleteHandler import CanchaDeleteHandler

cancha_router = APIRouter(prefix="/canchas", tags=["canchas"])

cancha_router.add_api_route(
    path="/",
    endpoint=CanchaFindHandler().find,
    methods=["GET"],
    summary="Buscar canchas con paginación y filtros",
    description="""
    ## Buscar y filtrar canchas
    
    Permite buscar canchas con opciones avanzadas de filtrado, ordenamiento y paginación.
    
    ### Parámetros de consulta:
    - **fields**: Campos específicos a devolver (opcional)
    - **filters**: Filtros avanzados en formato JSON
    - **orders**: Ordenamiento en formato JSON  
    - **p**: Parámetros de paginación (page_number, page_size)
    
    ### Ejemplos de filtros:
    ```json
    [
        {"field": "nombre", "operator": "CONTAINS", "value": "fútbol"},
        {"field": "techada", "operator": "EQUAL", "value": true}
    ]
    ```
    
    ### Ejemplos de ordenamiento:
    ```json
    [
        {"orderBy": "nombre", "orderType": "ASC"},
        {"orderBy": "techada", "orderType": "DESC"}
    ]
    ```
    """,
    responses={
        200: {
            "description": "Lista paginada de canchas encontradas",
            "content": {
                "application/json": {
                    "example": {
                        "items": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "nombre": "Cancha de Fútbol 5 Techada",
                                "techada": True
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440001", 
                                "nombre": "Cancha de Fútbol 7",
                                "techada": False
                            }
                        ],
                        "total": 25,
                        "page_size": 10,
                        "page_number": 1
                    }
                }
            }
        },
        400: {
            "description": "Error en parámetros de consulta",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Formato de filtro inválido"
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
    summary="Obtener cancha por ID",
    description="""
    ## Obtener una cancha específica
    
    Recupera los detalles completos de una cancha utilizando su identificador único.
    
    ### Parámetros:
    - **id**: UUID de la cancha (requerido)
    
    ### Respuesta:
    Devuelve todos los datos de la cancha incluyendo:
    - ID único
    - Nombre de la cancha
    - Estado (techada/no techada)
    """,
    responses={
        200: {
            "description": "Cancha encontrada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "nombre": "Cancha de Fútbol 5 Techada",
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
                        "detail": "Cancha con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "ID inválido",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "El ID proporcionado no es un UUID válido"
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
    
    ### Ejemplos de uso:
    - Canchas de fútbol 5, 7 u 11
    - Canchas de básquet, tenis, etc.
    - Especificación de techadas para clima
    """,
    responses={
        201: {
            "description": "Cancha creada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Cancha creada exitosamente",
                        "id": "550e8400-e29b-41d4-a716-446655440000"
                    }
                }
            }
        },
        400: {
            "description": "Error de validación o ID duplicado",
            "content": {
                "application/json": {
                    "examples": {
                        "validation_error": {
                            "summary": "Error de validación",
                            "value": {
                                "detail": "El nombre de la cancha debe tener entre 3 y 100 caracteres"
                            }
                        },
                        "duplicate_id": {
                            "summary": "ID duplicado",
                            "value": {
                                "detail": "Ya existe una cancha con ese ID"
                            }
                        }
                    }
                }
            }
        },
        422: {
            "description": "Datos de entrada inválidos",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "nombre"],
                                "msg": "field required",
                                "type": "value_error.missing"
                            }
                        ]
                    }
                }
            }
        }
    },
    status_code=status.HTTP_201_CREATED
)

cancha_router.add_api_route(
    path="/{id}",
    endpoint=CanchaUpdateHandler().update,
    methods=["PATCH"],
    summary="Actualizar cancha existente",
    description="""
    ## Actualizar una cancha existente
    
    Modifica los datos de una cancha existente. Solo se actualizan los campos proporcionados.
    
    ### Características:
    - Actualización parcial (PATCH)
    - Solo los campos enviados se modifican
    - Validaciones automáticas en campos modificados
    - Mantiene datos no modificados intactos
    
    ### Campos modificables:
    - **nombre**: Nuevo nombre (3-100 caracteres)
    - **techada**: Cambiar estado de techada
    
    ### Casos de uso:
    - Corrección de nombres con errores tipográficos
    - Cambios por remodelaciones (techada/descubierta)
    - Actualizaciones de información
    """,
    responses={
        200: {
            "description": "Cancha actualizada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Cancha actualizada exitosamente",
                        "id": "550e8400-e29b-41d4-a716-446655440000"
                    }
                }
            }
        },
        404: {
            "description": "Cancha no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Cancha con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "Error de validación",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "El nombre de la cancha debe tener entre 3 y 100 caracteres"
                    }
                }
            }
        },
        422: {
            "description": "Datos de entrada inválidos",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "techada"],
                                "msg": "value could not be parsed to a boolean",
                                "type": "type_error.bool"
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
    endpoint=CanchaDeleteHandler().delete,
    methods=["DELETE"],
    summary="Eliminar cancha",
    description="""
    ## Eliminar una cancha del sistema
    
    Elimina permanentemente una cancha del sistema.
    
    ### ⚠️ Advertencias importantes:
    - **Esta operación es irreversible**
    - Se verificará que no existan reservas activas
    - Se cancelarán reservas futuras automáticamente
    - Los datos históricos se mantienen para auditoría
    
    ### Proceso de eliminación:
    1. Verificación de existencia de la cancha
    2. Cancelación de reservas futuras
    3. Eliminación del registro de la cancha
    4. Notificación a jugadores con reservas canceladas
    
    ### Casos de uso:
    - Canchas fuera de servicio permanentemente
    - Errores en el registro de canchas
    - Reestructuración de instalaciones
    """,
    responses={
        204: {
            "description": "Cancha eliminada exitosamente (sin contenido)"
        },
        404: {
            "description": "Cancha no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Cancha con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
                    }
                }
            }
        },
        409: {
            "description": "No se puede eliminar por reservas activas",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No se puede eliminar la cancha porque tiene reservas activas"
                    }
                }
            }
        },
        400: {
            "description": "ID inválido",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "El ID proporcionado no es un UUID válido"
                    }
                }
            }
        }
    },
    status_code=status.HTTP_204_NO_CONTENT
) 