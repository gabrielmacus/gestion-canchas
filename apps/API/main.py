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
- 📧 Email: gabrielmacus@gmail.com
"""

app_version = "1.0.0"
environment = os.getenv("ENVIRONMENT", os.getenv("ENV", "development"))


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
            "email": "gabrielmacus@gmail.com"
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT"
        },
        servers=[
            
        ]
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI(
    title=app_title,
    description=app_description,
    version=app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    root_path=os.getenv("ROOT_PATH","/")
)

# Configurar OpenAPI personalizado
app.openapi = custom_openapi



# Incluir routers
app.include_router(jugador_router)
app.include_router(cancha_router)
app.include_router(reserva_router)

# Configurar CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
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
