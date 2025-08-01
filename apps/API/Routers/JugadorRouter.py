from fastapi import APIRouter, Query, Path, status
from typing import Optional

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
    - **orders**: Criterios de ordenamiento en formato JSON
    - **p**: Configuración de paginación (page_number, page_size)
    
    ### Ejemplos de filtros comunes:
    ```json
    [
        {"field": "nombre", "operator": "CONTAINS", "value": "Juan"},
        {"field": "apellido", "operator": "STARTS_WITH", "value": "Pérez"},
        {"field": "email", "operator": "NOT_NULL", "value": null}
    ]
    ```
    
    ### Ejemplos de ordenamiento:
    ```json
    [
        {"orderBy": "apellido", "orderType": "ASC"},
        {"orderBy": "nombre", "orderType": "ASC"}
    ]
    ```
    
    ### Casos de uso:
    - Búsqueda de jugadores por nombre o apellido
    - Listado de jugadores con email registrado
    - Ordenamiento alfabético para reportes
    """,
    responses={
        200: {
            "description": "Lista paginada de jugadores encontrados",
            "content": {
                "application/json": {
                    "example": {
                        "items": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "nombre": "Juan Carlos",
                                "apellido": "Pérez González",
                                "telefono": "1123456789",
                                "email": "juan.perez@email.com"
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440001",
                                "nombre": "María Elena",
                                "apellido": "Rodriguez",
                                "telefono": "1187654321", 
                                "email": null
                            }
                        ],
                        "total": 150,
                        "page_size": 20,
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
                        "detail": "Formato de filtro inválido o parámetro de paginación incorrecto"
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
    
    ### Casos de uso:
    - Verificación de datos antes de crear reservas
    - Actualización de información de contacto
    - Consulta de historial de reservas
    """,
    responses={
        200: {
            "description": "Jugador encontrado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "nombre": "Juan Carlos",
                        "apellido": "Pérez González", 
                        "telefono": "1123456789",
                        "email": "juan.perez@email.com"
                    }
                }
            }
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID 550e8400-e29b-41d4-a716-446655440000 no encontrado"
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
    """,
    responses={
        201: {
            "description": "Jugador registrado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Jugador registrado exitosamente",
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
                        "validation_nombre": {
                            "summary": "Error en nombre",
                            "value": {
                                "detail": "El nombre del jugador debe tener entre 3 y 100 caracteres"
                            }
                        },
                        "validation_telefono": {
                            "summary": "Error en teléfono",
                            "value": {
                                "detail": "El teléfono debe contener solo dígitos"
                            }
                        },
                        "validation_contacto": {
                            "summary": "Falta información de contacto",
                            "value": {
                                "detail": "Debe proporcionar al menos un email o un teléfono"
                            }
                        },
                        "duplicate_id": {
                            "summary": "ID duplicado",
                            "value": {
                                "detail": "Ya existe un jugador con ese ID"
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
                                "loc": ["body", "email"],
                                "msg": "value is not a valid email address",
                                "type": "value_error.email"
                            }
                        ]
                    }
                }
            }
        }
    },
    status_code=status.HTTP_201_CREATED
)

jugador_router.add_api_route(
    path="/{id}",
    endpoint=JugadorUpdateHandler().update,
    methods=["PATCH"],
    summary="Actualizar datos del jugador",
    description="""
    ## Actualizar información de un jugador
    
    Modifica parcialmente los datos de un jugador existente. Solo se actualizan los campos enviados.
    
    ### Características de la actualización:
    - **Parcial (PATCH)**: Solo envía los campos que deseas modificar
    - **Validaciones**: Se aplican las mismas reglas de validación que en la creación
    - **Preservación**: Los campos no enviados mantienen sus valores actuales
    - **Atomicidad**: La operación es completamente exitosa o falla sin cambios
    
    ### Campos modificables:
    - **nombre**: Nuevo nombre (3-100 caracteres)
    - **apellido**: Nuevo apellido (3-100 caracteres)
    - **telefono**: Nuevo teléfono (7-15 dígitos)
    - **email**: Nueva dirección de email (puede ser null)
    
    ### Casos de uso comunes:
    - Corrección de datos con errores tipográficos
    - Actualización de número de teléfono
    - Agregado o modificación de email
    - Cambios por matrimonio (apellido)
    
    ### Ejemplo de actualización parcial:
    ```json
    {
        "telefono": "1198765432",
        "email": "nuevo.email@gmail.com"
    }
    ```
    """,
    responses={
        200: {
            "description": "Jugador actualizado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Jugador actualizado exitosamente",
                        "id": "550e8400-e29b-41d4-a716-446655440000"
                    }
                }
            }
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID 550e8400-e29b-41d4-a716-446655440000 no encontrado"
                    }
                }
            }
        },
        400: {
            "description": "Error de validación",
            "content": {
                "application/json": {
                    "examples": {
                        "validation_apellido": {
                            "summary": "Error en apellido",
                            "value": {
                                "detail": "El apellido del jugador debe tener entre 3 y 100 caracteres"
                            }
                        },
                        "validation_telefono_length": {
                            "summary": "Error en longitud de teléfono",
                            "value": {
                                "detail": "El teléfono debe tener entre 7 y 15 dígitos"
                            }
                        },
                        "validation_email": {
                            "summary": "Error en formato de email",
                            "value": {
                                "detail": "El email no es válido"
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
                                "loc": ["body", "telefono"],
                                "msg": "ensure this value has at least 7 characters",
                                "type": "value_error.any_str.min_length"
                            }
                        ]
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
    summary="Eliminar jugador del sistema",
    description="""
    ## Eliminar un jugador del sistema
    
    Elimina permanentemente un jugador del sistema con verificaciones de seguridad.
    
    ### ⚠️ Advertencias importantes:
    - **Operación irreversible**: No se puede deshacer
    - **Verificación de reservas**: Se cancelan automáticamente las reservas futuras
    - **Historial**: Los datos históricos se preservan para auditoría
    - **Notificaciones**: Se notifica automáticamente sobre cancelaciones
    
    ### Proceso de eliminación:
    1. **Verificación**: Confirma que el jugador existe
    2. **Reservas activas**: Identifica reservas futuras del jugador
    3. **Cancelación**: Cancela automáticamente reservas pendientes
    4. **Notificación**: Envía avisos sobre las cancelaciones
    5. **Eliminación**: Remueve el registro del jugador
    6. **Auditoría**: Registra la operación para seguimiento
    
    ### Casos de uso:
    - Jugadores que se dan de baja del servicio
    - Registros duplicados por error
    - Solicitudes de eliminación de datos personales (GDPR)
    - Jugadores sancionados permanentemente
    
    ### Impacto en reservas:
    - ✅ **Reservas pasadas**: Se mantienen para historial
    - ❌ **Reservas futuras**: Se cancelan automáticamente
    - 📧 **Notificaciones**: Se envían a otros jugadores afectados
    """,
    responses={
        204: {
            "description": "Jugador eliminado exitosamente (sin contenido)"
        },
        404: {
            "description": "Jugador no encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Jugador con ID 550e8400-e29b-41d4-a716-446655440000 no encontrado"
                    }
                }
            }
        },
        409: {
            "description": "No se puede eliminar por restricciones del sistema",
            "content": {
                "application/json": {
                    "examples": {
                        "active_reservations": {
                            "summary": "Reservas activas",
                            "value": {
                                "detail": "El jugador tiene reservas activas que no pueden cancelarse automáticamente"
                            }
                        },
                        "admin_restriction": {
                            "summary": "Restricción administrativa",
                            "value": {
                                "detail": "No se puede eliminar este jugador por restricciones administrativas"
                            }
                        }
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