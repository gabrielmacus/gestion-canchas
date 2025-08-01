from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

# Modelos de Request
class CrearCanchaRequest(BaseModel):
    """Modelo para crear una nueva cancha"""
    id: str = Field(..., description="ID único de la cancha", example="550e8400-e29b-41d4-a716-446655440000")
    nombre: str = Field(..., description="Nombre de la cancha", min_length=3, max_length=100, example="Cancha Principal")
    techada: bool = Field(..., description="Indica si la cancha está techada", example=True)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "nombre": "Cancha Principal",
                "techada": True
            }
        }

class EditarCanchaRequest(BaseModel):
    """Modelo para editar una cancha existente"""
    nombre: Optional[str] = Field(None, description="Nuevo nombre de la cancha", min_length=3, max_length=100, example="Cancha Renovada")
    techada: Optional[bool] = Field(None, description="Nuevo estado de techado", example=False)

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Cancha Renovada",
                "techada": False
            }
        }

class CrearJugadorRequest(BaseModel):
    """Modelo para crear un nuevo jugador"""
    id: str = Field(..., description="ID único del jugador", example="550e8400-e29b-41d4-a716-446655440001")
    nombre: str = Field(..., description="Nombre del jugador", min_length=3, max_length=100, example="Carlos")
    apellido: str = Field(..., description="Apellido del jugador", min_length=3, max_length=100, example="García")
    telefono: str = Field(..., description="Teléfono del jugador (7-15 dígitos)", example="1234567890")
    email: Optional[EmailStr] = Field(None, description="Email del jugador (opcional)", example="carlos.garcia@email.com")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440001",
                "nombre": "Carlos",
                "apellido": "García",
                "telefono": "1234567890",
                "email": "carlos.garcia@email.com"
            }
        }

class EditarJugadorRequest(BaseModel):
    """Modelo para editar un jugador existente"""
    nombre: Optional[str] = Field(None, description="Nuevo nombre del jugador", min_length=3, max_length=100)
    apellido: Optional[str] = Field(None, description="Nuevo apellido del jugador", min_length=3, max_length=100)
    telefono: Optional[str] = Field(None, description="Nuevo teléfono del jugador (7-15 dígitos)")
    email: Optional[EmailStr] = Field(None, description="Nuevo email del jugador")

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Carlos Eduardo",
                "apellido": "García López",
                "telefono": "9876543210",
                "email": "carlos.eduardo@email.com"
            }
        }

class CrearReservaRequest(BaseModel):
    """Modelo para crear una nueva reserva"""
    id: str = Field(..., description="ID único de la reserva", example="550e8400-e29b-41d4-a716-446655440002")
    fecha_hora: datetime = Field(..., description="Fecha y hora de la reserva (hora exacta)", example="2024-12-25T14:00:00")
    duracion: int = Field(..., description="Duración en minutos (múltiplo de 60, min: 60, max: 240)", example=120)
    cancha_id: str = Field(..., description="ID de la cancha a reservar", example="550e8400-e29b-41d4-a716-446655440000")
    jugador_id: str = Field(..., description="ID del jugador que hace la reserva", example="550e8400-e29b-41d4-a716-446655440001")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440002",
                "fecha_hora": "2024-12-25T14:00:00",
                "duracion": 120,
                "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
                "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
            }
        }

class EditarReservaRequest(BaseModel):
    """Modelo para editar una reserva existente"""
    fecha_hora: Optional[datetime] = Field(None, description="Nueva fecha y hora de la reserva")
    duracion: Optional[int] = Field(None, description="Nueva duración en minutos (múltiplo de 60)")
    cancha_id: Optional[str] = Field(None, description="Nuevo ID de la cancha")
    jugador_id: Optional[str] = Field(None, description="Nuevo ID del jugador")

# Modelos de Response
class CanchaResponse(BaseModel):
    """Modelo de respuesta para una cancha"""
    id: str = Field(..., description="ID único de la cancha")
    nombre: str = Field(..., description="Nombre de la cancha")
    techada: bool = Field(..., description="Indica si la cancha está techada")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "nombre": "Cancha Principal",
                "techada": True
            }
        }

class JugadorResponse(BaseModel):
    """Modelo de respuesta para un jugador"""
    id: str = Field(..., description="ID único del jugador")
    nombre: str = Field(..., description="Nombre del jugador")
    apellido: str = Field(..., description="Apellido del jugador")
    telefono: str = Field(..., description="Teléfono del jugador")
    email: Optional[str] = Field(None, description="Email del jugador")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440001",
                "nombre": "Carlos",
                "apellido": "García",
                "telefono": "1234567890",
                "email": "carlos.garcia@email.com"
            }
        }

class ReservaResponse(BaseModel):
    """Modelo de respuesta para una reserva"""
    id: str = Field(..., description="ID único de la reserva")
    fecha_hora: datetime = Field(..., description="Fecha y hora de la reserva")
    duracion: int = Field(..., description="Duración de la reserva en minutos")
    cancha_id: str = Field(..., description="ID de la cancha reservada")
    jugador_id: str = Field(..., description="ID del jugador que hizo la reserva")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440002",
                "fecha_hora": "2024-12-25T14:00:00",
                "duracion": 120,
                "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
                "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
            }
        }

# Modelos de Error
class ErrorResponse(BaseModel):
    """Modelo de respuesta para errores"""
    detail: str = Field(..., description="Descripción detallada del error")

    class Config:
        json_schema_extra = {
            "example": {
                "detail": "El recurso solicitado no fue encontrado"
            }
        }

class ValidationErrorResponse(BaseModel):
    """Modelo de respuesta para errores de validación"""
    detail: List[Dict[str, Any]] = Field(..., description="Lista de errores de validación")

    class Config:
        json_schema_extra = {
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

# Modelos de Paginación
class PaginationResponse(BaseModel):
    """Modelo base para respuestas paginadas"""
    page: int = Field(..., description="Número de página actual")
    size: int = Field(..., description="Tamaño de página")
    total: int = Field(..., description="Total de elementos")
    total_pages: int = Field(..., description="Total de páginas")

class CanchasPaginatedResponse(BaseModel):
    """Respuesta paginada de canchas"""
    data: List[CanchaResponse] = Field(..., description="Lista de canchas")
    pagination: PaginationResponse = Field(..., description="Información de paginación")

    class Config:
        json_schema_extra = {
            "example": {
                "data": [
                    {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "nombre": "Cancha Principal",
                        "techada": True
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

class JugadoresPaginatedResponse(BaseModel):
    """Respuesta paginada de jugadores"""
    data: List[JugadorResponse] = Field(..., description="Lista de jugadores")
    pagination: PaginationResponse = Field(..., description="Información de paginación")

class ReservasPaginatedResponse(BaseModel):
    """Respuesta paginada de reservas"""
    data: List[ReservaResponse] = Field(..., description="Lista de reservas")
    pagination: PaginationResponse = Field(..., description="Información de paginación")

# Enums para documentación
class FilterOperator(str, Enum):
    """Operadores disponibles para filtros"""
    eq = "eq"           # Igual
    neq = "neq"         # No igual
    gt = "gt"           # Mayor que
    gte = "gte"         # Mayor o igual que
    lt = "lt"           # Menor que
    lte = "lte"         # Menor o igual que
    like = "like"       # Contiene (texto)
    in_op = "in"        # Está en lista
    not_in = "not_in"   # No está en lista

class OrderType(str, Enum):
    """Tipos de ordenamiento"""
    asc = "asc"         # Ascendente
    desc = "desc"       # Descendente