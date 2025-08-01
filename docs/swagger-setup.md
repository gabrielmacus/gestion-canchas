# 📚 Configuración y Uso de Documentación Swagger

## 🎯 Descripción General

Este sistema incluye documentación interactiva completa utilizando **Swagger/OpenAPI 3.0** con las siguientes características:

- 📖 **Documentación completa** de todos los endpoints
- 🔐 **Protección con contraseña** en producción
- 💡 **Ejemplos interactivos** para todas las operaciones
- 🏷️ **Organizacion por tags** (canchas, jugadores, reservas)
- ⚡ **Interfaz moderna** con tema personalizable

## 🚀 Acceso a la Documentación

### 🛠️ Entorno de Desarrollo

En desarrollo, la documentación está disponible sin autenticación:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

### 🔒 Entorno de Producción

En producción, el acceso requiere autenticación básica:

- **URL**: `https://tu-dominio.com/docs`
- **Usuario**: Configurado en `SWAGGER_USERNAME`
- **Contraseña**: Configurada en `SWAGGER_PASSWORD`

## ⚙️ Configuración

### 1. Variables de Entorno

Copia el archivo `.env.example` y configura las credenciales:

```bash
cp .env.example .env
```

Edita las siguientes variables:

```env
# Entorno (development/production)
ENVIRONMENT=production

# Credenciales de Swagger
SWAGGER_USERNAME=tu_usuario_seguro
SWAGGER_PASSWORD=tu_contraseña_muy_segura
```

### 2. Configuración de Seguridad

Para producción, asegúrate de usar credenciales seguras:

```bash
# Generar contraseña segura
openssl rand -base64 32
```

### 3. Configuración del Servidor

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en desarrollo
uvicorn apps.API.main:app --reload --host 0.0.0.0 --port 8000

# Ejecutar en producción
uvicorn apps.API.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📋 Funcionalidades de la Documentación

### 🏷️ Organización por Tags

- **canchas**: Gestión de canchas deportivas
- **jugadores**: Administración de jugadores
- **reservas**: Sistema de reservas
- **sistema**: Endpoints de estado y salud

### 💡 Características Avanzadas

#### Ejemplos Interactivos
Cada endpoint incluye:
- ✅ Ejemplos de request/response
- ✅ Validaciones detalladas
- ✅ Códigos de error específicos
- ✅ Casos de uso comunes

#### Filtros y Paginación
Documentación completa de:
- 🔍 Sistema de filtros avanzados
- 📄 Paginación configurable
- 🔤 Ordenamiento personalizable
- 📊 Respuestas paginadas

#### Validaciones
Detalles de todas las validaciones:
- 📝 Reglas de longitud de campos
- 📧 Validación de emails
- 📞 Formato de teléfonos
- 🕐 Validaciones de fechas/horas

## 🎨 Personalización de la Interfaz

### Tema Oscuro (Producción)
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

### Metadatos Personalizados
```json
{
    "title": "Sistema de Gestión de Canchas",
    "version": "1.0.0",
    "description": "API completa para gestión de canchas deportivas",
    "contact": {
        "name": "Equipo de Desarrollo",
        "email": "desarrollo@gestion-canchas.com"
    }
}
```

## 🔧 Endpoints Principales

### 🏟️ Gestión de Canchas
```
GET    /canchas           # Buscar canchas con filtros
GET    /canchas/{id}      # Obtener cancha específica
POST   /canchas           # Crear nueva cancha
PATCH  /canchas/{id}      # Actualizar cancha
DELETE /canchas/{id}      # Eliminar cancha
```

### 👥 Gestión de Jugadores
```
GET    /jugadores         # Buscar jugadores
GET    /jugadores/{id}    # Obtener jugador específico
POST   /jugadores         # Registrar nuevo jugador
PATCH  /jugadores/{id}    # Actualizar datos del jugador
DELETE /jugadores/{id}    # Eliminar jugador
```

### 📅 Sistema de Reservas
```
GET    /reservas          # Buscar reservas con filtros
GET    /reservas/{id}     # Obtener reserva específica
POST   /reservas          # Crear nueva reserva
PATCH  /reservas/{id}     # Modificar reserva
DELETE /reservas/{id}     # Cancelar reserva
```

## 📊 Ejemplos de Uso

### Crear una Cancha
```json
POST /canchas
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "nombre": "Cancha de Fútbol 5 Techada",
    "techada": true
}
```

### Buscar Reservas por Fecha
```json
GET /reservas?filters=[{"field": "fecha_hora", "operator": "GREATER_THAN", "value": "2024-01-15T00:00:00"}]
```

### Filtrar Jugadores con Email
```json
GET /jugadores?filters=[{"field": "email", "operator": "NOT_NULL", "value": null}]
```

## 🐛 Resolución de Problemas

### Error 401 en Producción
**Problema**: No puedo acceder a /docs en producción
**Solución**: 
1. Verificar variables `SWAGGER_USERNAME` y `SWAGGER_PASSWORD`
2. Confirmar que `ENVIRONMENT=production`
3. Usar autenticación básica HTTP

### Error 422 en Requests
**Problema**: Los requests fallan con errores de validación
**Solución**:
1. Revisar ejemplos en la documentación
2. Verificar tipos de datos (strings, números, fechas)
3. Comprobar campos requeridos

### Documentación No Se Actualiza
**Problema**: Los cambios no se reflejan en Swagger
**Solución**:
1. Reiniciar el servidor
2. Limpiar caché del navegador
3. Verificar que los cambios estén en el código

## 🔒 Consideraciones de Seguridad

### Producción
- ✅ Usar HTTPS siempre
- ✅ Credenciales complejas
- ✅ Rotar contraseñas regularmente
- ✅ Monitorear accesos

### Red
- ✅ Firewall configurado
- ✅ Rate limiting
- ✅ Logs de acceso
- ✅ VPN para administración

## 📞 Soporte

Para problemas con la documentación:

- 📧 **Email**: desarrollo@gestion-canchas.com
- 🌐 **Web**: https://gestion-canchas.com/soporte
- 📚 **Wiki**: https://wiki.gestion-canchas.com

## 🔄 Actualizaciones

La documentación se actualiza automáticamente con cada despliegue. Las versiones están marcadas según:

- **Major**: Cambios incompatibles (v2.0.0)
- **Minor**: Nuevas funcionalidades (v1.1.0)  
- **Patch**: Correcciones de errores (v1.0.1)