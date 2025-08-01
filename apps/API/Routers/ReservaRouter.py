from fastapi import APIRouter, Query, Path, status
from typing import Optional

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
    - **orders**: Criterios de ordenamiento en formato JSON
    - **p**: Configuración de paginación (page_number, page_size)
    
    ### Filtros comunes para reservas:
    ```json
    [
        {"field": "fecha_hora", "operator": "GREATER_THAN", "value": "2024-01-15T10:00:00"},
        {"field": "cancha_id", "operator": "EQUAL", "value": "550e8400-e29b-41d4-a716-446655440000"},
        {"field": "duracion", "operator": "GREATER_EQUAL", "value": 120}
    ]
    ```
    
    ### Ejemplos de ordenamiento:
    ```json
    [
        {"orderBy": "fecha_hora", "orderType": "ASC"},
        {"orderBy": "duracion", "orderType": "DESC"}
    ]
    ```
    
    ### Casos de uso específicos:
    - **Consulta de disponibilidad**: Filtrar por cancha y rango de fechas
    - **Reservas por jugador**: Filtrar por jugador_id para historial
    - **Reservas del día**: Filtrar por fecha específica
    - **Próximas reservas**: Filtrar reservas futuras
    - **Reservas largas**: Filtrar por duración mínima
    """,
    responses={
        200: {
            "description": "Lista paginada de reservas encontradas",
            "content": {
                "application/json": {
                    "example": {
                        "items": [
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440000",
                                "fecha_hora": "2024-01-15T14:00:00",
                                "duracion": 120,
                                "cancha_id": "550e8400-e29b-41d4-a716-446655441111",
                                "jugador_id": "550e8400-e29b-41d4-a716-446655442222"
                            },
                            {
                                "id": "550e8400-e29b-41d4-a716-446655440001",
                                "fecha_hora": "2024-01-15T16:00:00",
                                "duracion": 60,
                                "cancha_id": "550e8400-e29b-41d4-a716-446655441111",
                                "jugador_id": "550e8400-e29b-41d4-a716-446655442223"
                            }
                        ],
                        "total": 89,
                        "page_size": 15,
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
                        "detail": "Formato de filtro de fecha inválido o parámetro de paginación incorrecto"
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
    
    ### Casos de uso:
    - **Confirmación de reserva**: Verificar detalles antes del partido
    - **Modificación**: Consultar datos actuales antes de cambios
    - **Facturación**: Obtener información para cobros
    - **Reporte de uso**: Análisis de utilización de canchas
    - **Verificación de conflictos**: Validar superposiciones
    """,
    responses={
        200: {
            "description": "Reserva encontrada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "fecha_hora": "2024-01-15T14:00:00",
                        "duracion": 120,
                        "cancha_id": "550e8400-e29b-41d4-a716-446655441111",
                        "jugador_id": "550e8400-e29b-41d4-a716-446655442222"
                    }
                }
            }
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
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
    responses={
        201: {
            "description": "Reserva creada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Reserva creada exitosamente",
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "fecha_hora": "2024-01-15T14:00:00",
                        "duracion": 120
                    }
                }
            }
        },
        400: {
            "description": "Error de validación o reglas de negocio",
            "content": {
                "application/json": {
                    "examples": {
                        "fecha_pasada": {
                            "summary": "Fecha en el pasado",
                            "value": {
                                "detail": "La fecha de la reserva no puede ser menor a la fecha actual"
                            }
                        },
                        "fecha_muy_futura": {
                            "summary": "Fecha muy lejana",
                            "value": {
                                "detail": "La fecha no puede ser mayor a 3 meses desde la fecha actual"
                            }
                        },
                        "hora_inexacta": {
                            "summary": "Hora no exacta",
                            "value": {
                                "detail": "La hora de reserva debe ser exacta (minutos y segundos deben ser 0)"
                            }
                        },
                        "duracion_invalida": {
                            "summary": "Duración inválida",
                            "value": {
                                "detail": "La duración de la reserva debe ser múltiplo de 60 minutos"
                            }
                        },
                        "cancha_ocupada": {
                            "summary": "Cancha ya reservada",
                            "value": {
                                "detail": "La cancha ya está reservada en ese horario"
                            }
                        },
                        "duplicate_id": {
                            "summary": "ID duplicado",
                            "value": {
                                "detail": "Ya existe una reserva con ese ID"
                            }
                        }
                    }
                }
            }
        },
        404: {
            "description": "Cancha o jugador no encontrado",
            "content": {
                "application/json": {
                    "examples": {
                        "cancha_not_found": {
                            "summary": "Cancha no existe",
                            "value": {
                                "detail": "La cancha especificada no existe"
                            }
                        },
                        "jugador_not_found": {
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
            "description": "Datos de entrada inválidos",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "fecha_hora"],
                                "msg": "invalid datetime format",
                                "type": "value_error.datetime"
                            }
                        ]
                    }
                }
            }
        }
    },
    status_code=status.HTTP_201_CREATED
)

reserva_router.add_api_route(
    path="/{id}",
    endpoint=ReservaUpdateHandler().update,
    methods=["PATCH"],
    summary="Modificar reserva existente",
    description="""
    ## Modificar una reserva existente
    
    Actualiza parcialmente los datos de una reserva con validaciones automáticas de conflictos.
    
    ### Características de la modificación:
    - **Parcial (PATCH)**: Solo envía los campos que deseas modificar
    - **Validaciones**: Se aplican todas las reglas de validación
    - **Verificación de conflictos**: Re-validación de disponibilidad
    - **Atomicidad**: La operación es completamente exitosa o falla sin cambios
    
    ### Campos modificables:
    - **fecha_hora**: Nueva fecha/hora (debe cumplir todas las validaciones)
    - **duracion**: Nueva duración (60-240 minutos, múltiplos de 60)
    - **cancha_id**: Cambio de cancha (verificación de disponibilidad)
    - **jugador_id**: Transferir reserva a otro jugador
    
    ### Restricciones importantes:
    ⚠️ **Reservas en curso**: No se pueden modificar reservas que ya comenzaron
    ⚠️ **Tiempo límite**: Modificaciones hasta 2 horas antes del inicio
    ⚠️ **Disponibilidad**: La nueva configuración debe estar disponible
    ⚠️ **Políticas**: Cumplir con todas las reglas de reserva
    
    ### Casos de uso comunes:
    - **Cambio de horario**: Mover reserva a otra hora del mismo día
    - **Extensión**: Aumentar duración si hay disponibilidad
    - **Cambio de cancha**: Mover a cancha diferente
    - **Transferencia**: Cambiar el jugador responsable
    - **Ajustes de último momento**: Modificaciones urgentes
    
    ### Ejemplo de modificación:
    ```json
    {
        "fecha_hora": "2024-01-15T16:00:00",
        "duracion": 180
    }
    ```
    """,
    responses={
        200: {
            "description": "Reserva modificada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "message": "Reserva modificada exitosamente",
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "cambios_aplicados": ["fecha_hora", "duracion"]
                    }
                }
            }
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "Error de validación o restricciones",
            "content": {
                "application/json": {
                    "examples": {
                        "reserva_en_curso": {
                            "summary": "Reserva ya comenzó",
                            "value": {
                                "detail": "No se puede modificar una reserva que ya comenzó"
                            }
                        },
                        "tiempo_limite": {
                            "summary": "Muy cerca del inicio",
                            "value": {
                                "detail": "No se pueden hacer cambios con menos de 2 horas de anticipación"
                            }
                        },
                        "conflicto_horario": {
                            "summary": "Nuevo horario ocupado",
                            "value": {
                                "detail": "El nuevo horario solicitado ya está ocupado"
                            }
                        },
                        "duracion_invalida": {
                            "summary": "Duración no válida",
                            "value": {
                                "detail": "La nueva duración debe ser múltiplo de 60 minutos"
                            }
                        }
                    }
                }
            }
        },
        409: {
            "description": "Conflicto con otras reservas",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "La modificación genera conflicto con otra reserva existente"
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
                                "loc": ["body", "duracion"],
                                "msg": "ensure this value is greater than 59",
                                "type": "value_error.number.not_gt"
                            }
                        ]
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
    summary="Cancelar reserva",
    description="""
    ## Cancelar una reserva existente
    
    Cancela una reserva con verificaciones de políticas de cancelación y notificaciones automáticas.
    
    ### ⚠️ Políticas de cancelación:
    - **Reservas futuras**: Se pueden cancelar hasta 2 horas antes
    - **Reservas en curso**: No se pueden cancelar una vez iniciadas
    - **Reservas pasadas**: No se pueden cancelar (solo para auditoría)
    - **Reembolsos**: Según política comercial del establecimiento
    
    ### Proceso de cancelación:
    1. **Verificación**: Confirma que la reserva existe y es cancelable
    2. **Validación temporal**: Verifica que está dentro del tiempo permitido
    3. **Notificaciones**: Envía confirmación de cancelación al jugador
    4. **Liberación**: Marca el horario como disponible nuevamente
    5. **Auditoría**: Registra la cancelación para seguimiento
    6. **Reembolso**: Activa proceso de reembolso si aplica
    
    ### Estados de cancelación:
    - ✅ **Cancelable**: Reserva futura con más de 2 horas de anticipación
    - ⏰ **Tiempo límite**: Menos de 2 horas antes del inicio
    - 🏃 **En curso**: Reserva que ya comenzó
    - 📚 **Histórica**: Reserva ya finalizada
    
    ### Casos de uso:
    - **Cancelación voluntaria**: Jugador no puede asistir
    - **Cambios de plan**: Reagendamiento por otros compromisos
    - **Emergencias**: Situaciones imprevistas
    - **Problemas climáticos**: Canchas descubiertas en mal clima
    - **Mantenimiento**: Cancelación por problemas técnicos
    
    ### Efectos de la cancelación:
    - 🕐 **Disponibilidad**: El horario queda libre inmediatamente
    - 💰 **Facturación**: Se procesa según políticas de reembolso
    - 📧 **Notificaciones**: Se envía confirmación automática
    - 📊 **Estadísticas**: Se actualiza en reportes de uso
    """,
    responses={
        204: {
            "description": "Reserva cancelada exitosamente (sin contenido)"
        },
        404: {
            "description": "Reserva no encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Reserva con ID 550e8400-e29b-41d4-a716-446655440000 no encontrada"
                    }
                }
            }
        },
        400: {
            "description": "No se puede cancelar por restricciones",
            "content": {
                "application/json": {
                    "examples": {
                        "reserva_en_curso": {
                            "summary": "Reserva ya comenzó",
                            "value": {
                                "detail": "No se puede cancelar una reserva que ya comenzó"
                            }
                        },
                        "tiempo_limite": {
                            "summary": "Fuera del tiempo permitido",
                            "value": {
                                "detail": "No se pueden cancelar reservas con menos de 2 horas de anticipación"
                            }
                        },
                        "reserva_pasada": {
                            "summary": "Reserva ya finalizada",
                            "value": {
                                "detail": "No se puede cancelar una reserva que ya finalizó"
                            }
                        },
                        "ya_cancelada": {
                            "summary": "Ya cancelada",
                            "value": {
                                "detail": "La reserva ya fue cancelada anteriormente"
                            }
                        }
                    }
                }
            }
        },
        409: {
            "description": "Conflicto con políticas del sistema",
            "content": {
                "application/json": {
                    "examples": {
                        "politica_cancelacion": {
                            "summary": "Política de cancelación",
                            "value": {
                                "detail": "Esta reserva no puede cancelarse según las políticas del establecimiento"
                            }
                        },
                        "reembolso_procesado": {
                            "summary": "Reembolso ya procesado",
                            "value": {
                                "detail": "No se puede cancelar porque el reembolso ya fue procesado"
                            }
                        }
                    }
                }
            }
        }
    },
    status_code=status.HTTP_204_NO_CONTENT
) 