from dotenv import load_dotenv
import os
_ = load_dotenv()

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
import secrets
from apps.API.Routers.JugadorRouter import jugador_router
from apps.API.Routers.CanchaRouter import cancha_router
from apps.API.Routers.ReservaRouter import reserva_router

# Configuración de autenticación para documentación
security = HTTPBasic()
DOCS_USERNAME = os.getenv("DOCS_USERNAME", "admin")
DOCS_PASSWORD = os.getenv("DOCS_PASSWORD", "gestion_canchas_2024")

def authenticate_docs(credentials: HTTPBasicCredentials = Depends(security)):
    """Autenticación para proteger la documentación en producción"""
    is_correct_username = secrets.compare_digest(credentials.username, DOCS_USERNAME)
    is_correct_password = secrets.compare_digest(credentials.password, DOCS_PASSWORD)
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas para acceder a la documentación",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Configuración de la aplicación FastAPI con metadatos Swagger
app = FastAPI(
    title="Sistema de Gestión de Canchas",
    description="""
    ## 🏟️ API para Gestión de Canchas de Fútbol

    Este sistema permite administrar canchas, jugadores y reservas de forma eficiente.

    ### Características principales:
    * **Gestión de Canchas**: Crear, actualizar, eliminar y consultar canchas
    * **Gestión de Jugadores**: Administrar información de jugadores con validaciones
    * **Sistema de Reservas**: Reservar canchas con validaciones de disponibilidad
    * **Consultas Avanzadas**: Filtrado, ordenamiento y paginación en todos los endpoints
    * **Validaciones Robustas**: Validaciones de negocio para asegurar datos consistentes

    ### Modelos de Datos:
    * **Cancha**: Información de canchas (nombre, si está techada)
    * **Jugador**: Datos de jugadores (nombre, apellido, teléfono, email)
    * **Reserva**: Reservas de canchas (fecha/hora, duración, relaciones)

    ### Consultas:
    Todos los endpoints GET soportan parámetros de consulta avanzados:
    * `fields[]`: Campos específicos a incluir en la respuesta
    * `filters[]`: Filtros con operadores (eq, neq, gt, lt, like, etc.)
    * `orders[]`: Ordenamiento por múltiples campos
    * `p.page`: Número de página para paginación
    * `p.size`: Tamaño de página (por defecto 10)

    ---
    *Desarrollado para la gestión eficiente de complejos deportivos*
    """,
    version="1.0.0",
    contact={
        "name": "Equipo de Desarrollo",
        "email": "desarrollo@gestioncanchas.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Servidor de desarrollo"
        },
        {
            "url": "https://api.gestioncanchas.com",
            "description": "Servidor de producción"
        }
    ],
    docs_url=None,  # Deshabilitamos el endpoint automático
    redoc_url=None,  # Deshabilitamos redoc automático
)

# Endpoints protegidos para documentación
@app.get("/docs", include_in_schema=False)
async def get_documentation(username: str = Depends(authenticate_docs)):
    """Documentación Swagger protegida con autenticación básica"""
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Sistema de Gestión de Canchas - Documentación API",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png"
    )

@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(authenticate_docs)):
    """Schema OpenAPI protegido"""
    return get_openapi(title=app.title, version=app.version, routes=app.routes)

# Incluir routers
app.include_router(jugador_router)
app.include_router(cancha_router)
app.include_router(reserva_router)

# Configuración CORS
origin = os.getenv("ALLOWED_ORIGIN")
assert origin is not None

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de estado de la API
@app.get("/", tags=["Estado"], summary="Estado de la API")
async def root():
    """
    Endpoint para verificar el estado de la API.
    
    Returns:
        dict: Información básica del estado de la aplicación
    """
    return {
        "message": "Sistema de Gestión de Canchas",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs (requiere autenticación)"
    }
