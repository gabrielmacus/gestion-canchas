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

# Configuración de la aplicación
app_title = "Sistema de Gestión de Canchas"
app_description = """
## Sistema de Gestión de Canchas ⚽

Un sistema completo para la gestión de canchas deportivas, jugadores y reservas.

### Funcionalidades principales:

* **Gestión de Canchas** 🏟️
  * Crear, leer, actualizar y eliminar canchas
  * Control de disponibilidad (techadas/no techadas)
  * Búsqueda y filtrado avanzado

* **Gestión de Jugadores** 👥
  * Administrar información de jugadores
  * Validación de datos de contacto
  * Sistema de búsqueda y paginación

* **Sistema de Reservas** 📅
  * Reservar canchas por períodos de tiempo
  * Validación de conflictos de horarios
  * Gestión de duraciones y disponibilidad
  * Control de reservas futuras (hasta 3 meses)

### Características técnicas:

* Arquitectura hexagonal (Clean Architecture)
* Patrones CQRS y DDD
* Validaciones robustas con Pydantic
* Sistema de paginación y filtrado
* Manejo de errores estructurado

---

**Contacto del equipo de desarrollo:**
- 📧 Email: desarrollo@gestion-canchas.com
- 🌐 Web: https://gestion-canchas.com
"""

app_version = "1.0.0"
environment = os.getenv("ENVIRONMENT", "development")

# Configuración de seguridad para Swagger
security = HTTPBasic()
SWAGGER_USERNAME = os.getenv("SWAGGER_USERNAME", "admin")
SWAGGER_PASSWORD = os.getenv("SWAGGER_PASSWORD", "admin123")

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """Verificación de credenciales para acceso a documentación en producción"""
    is_correct_username = secrets.compare_digest(credentials.username, SWAGGER_USERNAME)
    is_correct_password = secrets.compare_digest(credentials.password, SWAGGER_PASSWORD)
    
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Configuración personalizada de OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app_title,
        version=app_version,
        description=app_description,
        routes=app.routes,
        contact={
            "name": "Equipo de Desarrollo - Gestión Canchas",
            "email": "desarrollo@gestion-canchas.com",
            "url": "https://gestion-canchas.com"
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT"
        },
        servers=[
            {
                "url": "http://localhost:8000",
                "description": "Servidor de desarrollo"
            },
            {
                "url": "https://api.gestion-canchas.com",
                "description": "Servidor de producción"
            }
        ]
    )
    
    # Configuración de componentes reutilizables
    openapi_schema["components"]["schemas"].update({
        "ValidationError": {
            "title": "ValidationError",
            "type": "object",
            "properties": {
                "detail": {
                    "title": "Detail",
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "loc": {"type": "array", "items": {"type": "string"}},
                            "msg": {"type": "string"},
                            "type": {"type": "string"}
                        }
                    }
                }
            }
        }
    })
    
    # Agregar tags personalizados
    openapi_schema["tags"] = [
        {
            "name": "canchas",
            "description": "Operaciones relacionadas con la gestión de canchas deportivas",
            "externalDocs": {
                "description": "Documentación detallada",
                "url": "https://docs.gestion-canchas.com/canchas"
            }
        },
        {
            "name": "jugadores", 
            "description": "Gestión de jugadores y sus datos de contacto",
            "externalDocs": {
                "description": "Documentación detallada",
                "url": "https://docs.gestion-canchas.com/jugadores"
            }
        },
        {
            "name": "reservas",
            "description": "Sistema de reservas y control de disponibilidad",
            "externalDocs": {
                "description": "Documentación detallada", 
                "url": "https://docs.gestion-canchas.com/reservas"
            }
        }
    ]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Crear aplicación FastAPI
if environment == "production":
    app = FastAPI(
        title=app_title,
        description=app_description,
        version=app_version,
        docs_url=None,  # Deshabilitar documentación sin autenticación
        redoc_url=None,
        openapi_url=None
    )
else:
    app = FastAPI(
        title=app_title,
        description=app_description,
        version=app_version,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

# Configurar OpenAPI personalizado
app.openapi = custom_openapi

# Endpoints protegidos para documentación en producción
if environment == "production":
    @app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
    async def get_docs(username: str = Depends(get_current_user)):
        return get_swagger_ui_html(
            openapi_url="/openapi.json",
            title=f"{app_title} - Documentación",
            swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
            swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
            swagger_ui_parameters={
                "defaultModelsExpandDepth": 2,
                "defaultModelExpandDepth": 2,
                "displayRequestDuration": True,
                "filter": True,
                "persistAuthorization": True,
                "theme": "dark"
            }
        )
    
    @app.get("/redoc", response_class=HTMLResponse, include_in_schema=False)
    async def get_redoc(username: str = Depends(get_current_user)):
        from fastapi.openapi.docs import get_redoc_html
        return get_redoc_html(
            openapi_url="/openapi.json",
            title=f"{app_title} - Documentación ReDoc"
        )
    
    @app.get("/openapi.json", include_in_schema=False)
    async def get_openapi_endpoint(username: str = Depends(get_current_user)):
        return app.openapi()

# Incluir routers
app.include_router(jugador_router)
app.include_router(cancha_router)
app.include_router(reserva_router)

# Configurar CORS
origin = os.getenv("ALLOWED_ORIGIN")
assert origin is not None

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de estado del sistema
@app.get("/", 
         summary="Estado del sistema",
         description="Endpoint para verificar el estado del sistema de gestión de canchas",
         tags=["sistema"],
         responses={
             200: {
                 "description": "Sistema funcionando correctamente",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "ok",
                             "message": "Sistema de Gestión de Canchas funcionando correctamente",
                             "version": "1.0.0",
                             "environment": "production"
                         }
                     }
                 }
             }
         })
async def root():
    return {
        "status": "ok",
        "message": "Sistema de Gestión de Canchas funcionando correctamente",
        "version": app_version,
        "environment": environment
    }
