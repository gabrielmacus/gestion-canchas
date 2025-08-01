# 🚀 Guía Rápida - Documentación Swagger

## ⚡ Instalación y Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
# Edita .env con tus configuraciones
```

### 3. Ejecutar la aplicación
```bash
uvicorn apps.API.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Acceder a la documentación
**URL:** http://localhost:8000/docs

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `gestion_canchas_2024`

## 🎯 Características Implementadas

### ✅ Documentación Completa
- ✅ Metadatos descriptivos de la API
- ✅ Documentación de todos los endpoints (15 endpoints)
- ✅ Modelos de request/response con ejemplos
- ✅ Códigos de estado HTTP documentados
- ✅ Validaciones y reglas de negocio explicadas

### ✅ Seguridad
- ✅ Autenticación básica HTTP para `/docs`
- ✅ Protección con contraseña en producción
- ✅ Variables de entorno configurables

### ✅ Endpoints Documentados

**🏟️ Canchas (5 endpoints):**
- GET `/canchas` - Buscar y paginar
- GET `/canchas/{id}` - Obtener por ID
- POST `/canchas` - Crear
- PATCH `/canchas/{id}` - Actualizar
- DELETE `/canchas/{id}` - Eliminar

**👤 Jugadores (5 endpoints):**
- GET `/jugadores` - Buscar y paginar
- GET `/jugadores/{id}` - Obtener por ID
- POST `/jugadores` - Crear
- PATCH `/jugadores/{id}` - Actualizar
- DELETE `/jugadores/{id}` - Eliminar

**📅 Reservas (5 endpoints):**
- GET `/reservas` - Buscar y paginar
- GET `/reservas/{id}` - Obtener por ID
- POST `/reservas` - Crear
- PATCH `/reservas/{id}` - Actualizar
- DELETE `/reservas/{id}` - Eliminar

### ✅ Sistema de Consultas
- ✅ Filtros avanzados (`filters[]`)
- ✅ Ordenamiento (`orders[]`)
- ✅ Paginación (`p.page`, `p.size`)
- ✅ Campos específicos (`fields[]`)

## 🔧 Configuración para Producción

### Variables de entorno
```bash
export DOCS_USERNAME="admin_prod"
export DOCS_PASSWORD="tu_contraseña_segura"
export ALLOWED_ORIGIN="https://tu-frontend.com"
```

### Ejecución en producción
```bash
uvicorn apps.API.main:app --host 0.0.0.0 --port 8000
```

## 📚 Documentación Completa

Para más detalles, consulta: [Documentación Completa](./swagger-documentation.md)

## ✨ Ejemplos de Uso

### Crear una cancha
```bash
curl -X POST "http://localhost:8000/canchas" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "nombre": "Cancha Principal",
    "techada": true
  }'
```

### Buscar canchas con filtros
```bash
curl "http://localhost:8000/canchas?filters[0][field]=techada&filters[0][operator]=eq&filters[0][value]=true"
```

### Crear un jugador
```bash
curl -X POST "http://localhost:8000/jugadores" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440001",
    "nombre": "Carlos",
    "apellido": "García",
    "telefono": "1234567890",
    "email": "carlos@email.com"
  }'
```

### Crear una reserva
```bash
curl -X POST "http://localhost:8000/reservas" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "550e8400-e29b-41d4-a716-446655440002",
    "fecha_hora": "2024-12-25T14:00:00",
    "duracion": 120,
    "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
    "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
  }'
```

---

¡Tu documentación Swagger está lista y funcional! 🎉