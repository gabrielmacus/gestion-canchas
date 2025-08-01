# 🏟️ Sistema de Gestión de Canchas - Documentación Swagger

## 📋 Resumen de Implementación

¡Se ha implementado exitosamente la **documentación Swagger completa** para tu sistema de gestión de canchas! La documentación incluye protección con contraseña para producción y ejemplos interactivos para todos los endpoints.

## ✅ Funcionalidades Implementadas

### 🔧 Configuración Principal
- ✅ **FastAPI con Swagger/OpenAPI 3.0** completamente configurado
- ✅ **Protección con contraseña** en entorno de producción
- ✅ **Tema personalizado** con interfaz moderna
- ✅ **Metadatos completos** (contacto, licencia, servidores)
- ✅ **Tags organizados** por módulos (canchas, jugadores, reservas)

### 📚 Documentación de Endpoints

#### 🏟️ Gestión de Canchas (`/canchas`)
- ✅ `GET /canchas` - Búsqueda con filtros avanzados y paginación
- ✅ `GET /canchas/{id}` - Obtener cancha específica
- ✅ `POST /canchas` - Crear nueva cancha con validaciones
- ✅ `PATCH /canchas/{id}` - Actualización parcial
- ✅ `DELETE /canchas/{id}` - Eliminación con verificaciones

#### 👥 Gestión de Jugadores (`/jugadores`)
- ✅ `GET /jugadores` - Búsqueda y filtrado de jugadores
- ✅ `GET /jugadores/{id}` - Datos completos del jugador
- ✅ `POST /jugadores` - Registro con validaciones complejas
- ✅ `PATCH /jugadores/{id}` - Actualización de datos
- ✅ `DELETE /jugadores/{id}` - Eliminación con gestión de reservas

#### 📅 Sistema de Reservas (`/reservas`)
- ✅ `GET /reservas` - Consultas avanzadas con filtros de fecha
- ✅ `GET /reservas/{id}` - Detalles de reserva específica
- ✅ `POST /reservas` - Creación con validaciones de conflictos
- ✅ `PATCH /reservas/{id}` - Modificación con verificaciones
- ✅ `DELETE /reservas/{id}` - Cancelación con políticas

### 💡 Características Avanzadas

#### Documentación Detallada
- ✅ **Descripciones completas** con markdown y emojis
- ✅ **Ejemplos interactivos** para cada endpoint
- ✅ **Códigos de respuesta** específicos con casos de uso
- ✅ **Validaciones documentadas** con ejemplos de errores
- ✅ **Casos de uso prácticos** para cada operación

#### Sistema de Filtros
- ✅ **Filtros JSON avanzados** con operadores (EQUAL, CONTAINS, etc.)
- ✅ **Ordenamiento personalizable** por múltiples campos
- ✅ **Paginación configurable** con totales y metadatos
- ✅ **Ejemplos de consultas** complejas documentadas

#### Seguridad en Producción
- ✅ **Autenticación HTTP Basic** para acceso a documentación
- ✅ **Variables de entorno** para credenciales seguras
- ✅ **Configuración automática** según entorno
- ✅ **URLs protegidas** en producción

## 🚀 Cómo Usar

### 🛠️ Desarrollo Local

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar entorno**:
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

3. **Ejecutar servidor**:
   ```bash
   python3 run_server.py
   ```

4. **Acceder a documentación**:
   - **Swagger UI**: http://localhost:8000/docs
   - **ReDoc**: http://localhost:8000/redoc
   - **OpenAPI JSON**: http://localhost:8000/openapi.json

### 🔒 Producción

1. **Configurar variables de entorno**:
   ```env
   ENVIRONMENT=production
   SWAGGER_USERNAME=tu_usuario_seguro
   SWAGGER_PASSWORD=tu_contraseña_muy_segura
   ```

2. **Ejecutar en modo producción**:
   ```bash
   python3 run_server.py --production
   ```

3. **Acceder con autenticación**:
   - URL: https://tu-dominio.com/docs
   - Usuario/Contraseña: Configurados en variables de entorno

## 📊 Ejemplos de Uso de la API

### Crear una Cancha
```bash
curl -X POST "http://localhost:8000/canchas" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "nombre": "Cancha de Fútbol 5 Techada",
    "techada": true
  }'
```

### Buscar Reservas por Fecha
```bash
curl "http://localhost:8000/reservas?filters=[{\"field\": \"fecha_hora\", \"operator\": \"GREATER_THAN\", \"value\": \"2024-01-15T00:00:00\"}]"
```

### Filtrar Jugadores con Email
```bash
curl "http://localhost:8000/jugadores?filters=[{\"field\": \"email\", \"operator\": \"NOT_NULL\", \"value\": null}]"
```

## 🎨 Personalización

### Modificar Metadatos
Edita `apps/API/main.py` para cambiar:
- Título y descripción de la API
- Información de contacto
- URLs de servidores
- Configuración de tags

### Personalizar Tema
En producción se aplica automáticamente:
```javascript
{
    "theme": "dark",
    "defaultModelsExpandDepth": 2,
    "displayRequestDuration": true,
    "filter": true,
    "persistAuthorization": true
}
```

## 📁 Archivos Creados/Modificados

### Archivos Principales
- ✅ `apps/API/main.py` - Configuración completa de FastAPI y Swagger
- ✅ `apps/API/Routers/CanchaRouter.py` - Documentación detallada de canchas
- ✅ `apps/API/Routers/JugadorRouter.py` - Documentación completa de jugadores  
- ✅ `apps/API/Routers/ReservaRouter.py` - Documentación avanzada de reservas

### Archivos de Configuración
- ✅ `.env.example` - Template de variables de entorno
- ✅ `run_server.py` - Script de inicio automático con validaciones
- ✅ `docs/swagger-setup.md` - Documentación técnica detallada

## 🔧 Características Técnicas

### Validaciones Documentadas
- **Canchas**: Nombre (3-100 chars), Estado techada/descubierta
- **Jugadores**: Nombre/apellido (3-100 chars), teléfono (7-15 dígitos), email válido
- **Reservas**: Fechas futuras, horarios exactos, duraciones válidas (60-240 min)

### Manejo de Errores
- **400 Bad Request**: Errores de validación con mensajes específicos
- **404 Not Found**: Recursos no encontrados con IDs detallados
- **409 Conflict**: Conflictos de horarios o restricciones de negocio
- **422 Unprocessable Entity**: Errores de formato de datos

### Filtros Avanzados
Operadores disponibles:
- `EQUAL`, `NOT_EQUAL`
- `GREATER_THAN`, `GREATER_EQUAL`
- `LESS_THAN`, `LESS_EQUAL`
- `CONTAINS`, `STARTS_WITH`, `ENDS_WITH`
- `IS_NULL`, `NOT_NULL`

## 🔒 Seguridad

### Producción
- ✅ HTTPS obligatorio
- ✅ Credenciales complejas para Swagger
- ✅ Documentación protegida
- ✅ Variables de entorno para secretos

### Desarrollo
- ✅ Documentación abierta para desarrollo
- ✅ Auto-reload habilitado
- ✅ Debugging facilitado

## 📞 Soporte y Contacto

- 📧 **Email**: desarrollo@gestion-canchas.com
- 🌐 **Web**: https://gestion-canchas.com
- 📚 **Documentación**: Ver `docs/swagger-setup.md`

## 🎯 Próximos Pasos

1. **Instalar dependencias completas**: `pip install -r requirements.txt`
2. **Configurar base de datos**: Según tu configuración actual
3. **Personalizar credenciales**: Cambiar valores por defecto en producción
4. **Desplegar**: Usar el modo producción con autenticación

---

¡Tu sistema ahora tiene **documentación Swagger profesional y completa**! 🎉

La documentación incluye:
- 📖 **15 endpoints documentados** con ejemplos
- 🔐 **Protección en producción** con contraseña
- 💡 **Ejemplos interactivos** para cada operación
- 🏷️ **Organización por módulos** (canchas, jugadores, reservas)
- ⚡ **Interfaz moderna** con tema personalizable