# 📚 Documentación Swagger API - Sistema de Gestión de Canchas

## 🔐 Acceso a la Documentación

### Desarrollo Local
En desarrollo local, accede a la documentación en:
```
http://localhost:8000/docs
```

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `gestion_canchas_2024`

### Producción
En producción, la documentación está protegida con autenticación básica HTTP.

**URL de acceso:**
```
https://tu-dominio.com/docs
```

**Configuración de credenciales:**
Configura las siguientes variables de entorno:
```bash
DOCS_USERNAME=tu_usuario_admin
DOCS_PASSWORD=tu_contraseña_segura
```

## 🚀 Características de la Documentación

### 📋 Metadatos Completos
- **Título:** Sistema de Gestión de Canchas
- **Versión:** 1.0.0
- **Descripción:** API completa para gestionar canchas, jugadores y reservas
- **Contacto:** desarrollo@gestioncanchas.com
- **Licencia:** MIT License

### 🏗️ Estructura de la API

#### 🏟️ Módulo de Canchas (`/canchas`)
- `GET /canchas` - Buscar y paginar canchas
- `GET /canchas/{id}` - Obtener cancha por ID
- `POST /canchas` - Crear nueva cancha
- `PATCH /canchas/{id}` - Actualizar cancha
- `DELETE /canchas/{id}` - Eliminar cancha

#### 👤 Módulo de Jugadores (`/jugadores`)
- `GET /jugadores` - Buscar y paginar jugadores
- `GET /jugadores/{id}` - Obtener jugador por ID
- `POST /jugadores` - Crear nuevo jugador
- `PATCH /jugadores/{id}` - Actualizar jugador
- `DELETE /jugadores/{id}` - Eliminar jugador

#### 📅 Módulo de Reservas (`/reservas`)
- `GET /reservas` - Buscar y paginar reservas
- `GET /reservas/{id}` - Obtener reserva por ID
- `POST /reservas` - Crear nueva reserva
- `PATCH /reservas/{id}` - Actualizar reserva
- `DELETE /reservas/{id}` - Cancelar reserva

## 🔍 Sistema de Consultas Avanzadas

Todos los endpoints GET soportan consultas avanzadas con:

### Filtros (`filters[]`)
Estructura:
```
filters[0][field]=campo
filters[0][operator]=operador
filters[0][value]=valor
```

**Operadores disponibles:**
- `eq` - Igual
- `neq` - No igual
- `gt` - Mayor que
- `gte` - Mayor o igual que
- `lt` - Menor que
- `lte` - Menor o igual que
- `like` - Contiene (texto)
- `in` - Está en lista
- `not_in` - No está en lista

**Ejemplos:**
```bash
# Buscar canchas techadas
GET /canchas?filters[0][field]=techada&filters[0][operator]=eq&filters[0][value]=true

# Buscar jugadores por nombre
GET /jugadores?filters[0][field]=nombre&filters[0][operator]=like&filters[0][value]=Carlos

# Buscar reservas futuras
GET /reservas?filters[0][field]=fecha_hora&filters[0][operator]=gt&filters[0][value]=2024-12-20T00:00:00
```

### Ordenamiento (`orders[]`)
Estructura:
```
orders[0][field]=campo
orders[0][type]=tipo
```

**Tipos de ordenamiento:**
- `asc` - Ascendente
- `desc` - Descendente

**Ejemplos:**
```bash
# Ordenar canchas por nombre
GET /canchas?orders[0][field]=nombre&orders[0][type]=asc

# Ordenar reservas por fecha (más recientes primero)
GET /reservas?orders[0][field]=fecha_hora&orders[0][type]=desc
```

### Paginación (`p`)
Estructura:
```
p.page=numero_pagina
p.size=tamaño_pagina
```

**Ejemplos:**
```bash
# Segunda página con 20 elementos
GET /canchas?p.page=2&p.size=20

# Primera página con 5 elementos
GET /jugadores?p.page=1&p.size=5
```

### Campos Específicos (`fields[]`)
Estructura:
```
fields[0]=campo1
fields[1]=campo2
```

**Ejemplo:**
```bash
# Solo obtener ID y nombre de canchas
GET /canchas?fields[0]=id&fields[1]=nombre
```

## 📝 Modelos de Datos

### 🏟️ Cancha
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "nombre": "Cancha Principal",
  "techada": true
}
```

### 👤 Jugador
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440001",
  "nombre": "Carlos",
  "apellido": "García",
  "telefono": "1234567890",
  "email": "carlos.garcia@email.com"
}
```

### 📅 Reserva
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440002",
  "fecha_hora": "2024-12-25T14:00:00",
  "duracion": 120,
  "cancha_id": "550e8400-e29b-41d4-a716-446655440000",
  "jugador_id": "550e8400-e29b-41d4-a716-446655440001"
}
```

## ✅ Validaciones Implementadas

### Canchas
- **ID:** Único en el sistema
- **Nombre:** 3-100 caracteres
- **Techada:** Booleano

### Jugadores
- **ID:** Único en el sistema
- **Nombre:** 3-100 caracteres
- **Apellido:** 3-100 caracteres
- **Teléfono:** 7-15 dígitos (requerido)
- **Email:** Formato válido (opcional)
- **Regla:** Email O teléfono requerido

### Reservas
- **ID:** Único en el sistema
- **Fecha/hora:** Futura, máximo 3 meses, hora exacta
- **Duración:** 60-240 minutos, múltiplo de 60
- **Cancha ID:** Debe existir y estar disponible
- **Jugador ID:** Debe existir

## 🚨 Códigos de Estado HTTP

### Exitosos
- `200 OK` - Operación exitosa
- `201 Created` - Recurso creado
- `204 No Content` - Eliminación exitosa

### Errores del Cliente
- `400 Bad Request` - Datos inválidos o reglas de negocio
- `404 Not Found` - Recurso no encontrado
- `422 Unprocessable Entity` - Error de validación

### Errores del Servidor
- `500 Internal Server Error` - Error interno

## 🔧 Configuración de Desarrollo

### Variables de Entorno
```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita las variables según tu configuración
DOCS_USERNAME=admin
DOCS_PASSWORD=mi_contraseña_segura
ALLOWED_ORIGIN=http://localhost:3000
```

### Instalación y Ejecución
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
uvicorn apps.API.main:app --reload --host 0.0.0.0 --port 8000
```

### Acceso a la Documentación
```bash
# Servidor local
curl -u admin:gestion_canchas_2024 http://localhost:8000/docs

# O abre en navegador con autenticación básica
http://admin:gestion_canchas_2024@localhost:8000/docs
```

## 🔒 Seguridad en Producción

### Cambiar Credenciales
```bash
# Variables de entorno en producción
export DOCS_USERNAME="admin_produccion"
export DOCS_PASSWORD="contraseña_muy_segura_2024"
```

### HTTPS Obligatorio
En producción, asegúrate de usar HTTPS para proteger las credenciales de autenticación básica.

### Restricciones adicionales
Considera implementar:
- Rate limiting
- IP whitelisting
- VPN/proxy reverso para documentación

## 📞 Soporte

Para soporte técnico o preguntas sobre la API:
- **Email:** desarrollo@gestioncanchas.com
- **Documentación:** `/docs` (con autenticación)
- **Estado de la API:** `/` (endpoint público)

---

*Documentación generada automáticamente con FastAPI y OpenAPI 3.0*