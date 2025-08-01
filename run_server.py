#!/usr/bin/env python3
"""
Script de inicio para el Sistema de Gestión de Canchas
Configura automáticamente el entorno y ejecuta el servidor con Swagger habilitado.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def setup_environment():
    """Configura el entorno y verifica dependencias"""
    print("🔧 Configurando entorno...")
    
    # Verificar archivo .env
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("📝 Creando archivo .env desde .env.example...")
        env_file.write_text(env_example.read_text())
    
    # Verificar variables de entorno críticas
    required_vars = ["ALLOWED_ORIGIN"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"⚠️  Variables de entorno faltantes: {', '.join(missing_vars)}")
        print("💡 Asegúrate de configurar el archivo .env")
    
    print("✅ Entorno configurado correctamente")

def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    print("📦 Verificando dependencias...")
    
    try:
        import fastapi
        import uvicorn
        import pydantic
        print("✅ Dependencias principales encontradas")
        return True
    except ImportError as e:
        print(f"❌ Dependencia faltante: {e}")
        print("💡 Ejecuta: pip install -r requirements.txt")
        return False

def show_swagger_info():
    """Muestra información sobre cómo acceder a Swagger"""
    environment = os.getenv("ENVIRONMENT", "development")
    swagger_user = os.getenv("SWAGGER_USERNAME", "admin")
    swagger_pass = os.getenv("SWAGGER_PASSWORD", "admin123")
    
    print("\n" + "="*60)
    print("📚 INFORMACIÓN DE DOCUMENTACIÓN SWAGGER")
    print("="*60)
    
    if environment == "development":
        print("🛠️  ENTORNO DE DESARROLLO")
        print("   Acceso SIN autenticación:")
        print("   • Swagger UI: http://localhost:8000/docs")
        print("   • ReDoc:     http://localhost:8000/redoc")
        print("   • OpenAPI:   http://localhost:8000/openapi.json")
    else:
        print("🔒 ENTORNO DE PRODUCCIÓN")
        print("   Acceso CON autenticación:")
        print("   • URL:       http://localhost:8000/docs")
        print(f"   • Usuario:   {swagger_user}")
        print(f"   • Contraseña: {swagger_pass}")
        print("   ⚠️  Cambiar credenciales antes del despliegue!")
    
    print("\n🏷️  ENDPOINTS DISPONIBLES:")
    print("   • GET  /         - Estado del sistema")
    print("   • /canchas       - Gestión de canchas (CRUD)")
    print("   • /jugadores     - Gestión de jugadores (CRUD)")
    print("   • /reservas      - Sistema de reservas (CRUD)")
    print("="*60)

def run_server(host="0.0.0.0", port=8000, reload=True, workers=1):
    """Ejecuta el servidor FastAPI con uvicorn"""
    cmd = [
        "uvicorn",
        "apps.API.main:app",
        f"--host={host}",
        f"--port={port}",
    ]
    
    if reload:
        cmd.append("--reload")
    else:
        cmd.extend([f"--workers={workers}"])
    
    print(f"🚀 Iniciando servidor en http://{host}:{port}")
    print("🔄 Presiona Ctrl+C para detener el servidor")
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
    except Exception as e:
        print(f"❌ Error al iniciar servidor: {e}")
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Sistema de Gestión de Canchas - Servidor API con Swagger"
    )
    parser.add_argument(
        "--host", 
        default="0.0.0.0", 
        help="Host del servidor (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Puerto del servidor (default: 8000)"
    )
    parser.add_argument(
        "--no-reload", 
        action="store_true", 
        help="Deshabilitar auto-reload en desarrollo"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=1, 
        help="Número de workers para producción (default: 1)"
    )
    parser.add_argument(
        "--production", 
        action="store_true", 
        help="Ejecutar en modo producción (sin reload, múltiples workers)"
    )
    parser.add_argument(
        "--check-only", 
        action="store_true", 
        help="Solo verificar configuración, no iniciar servidor"
    )
    
    args = parser.parse_args()
    
    print("⚽ Sistema de Gestión de Canchas")
    print("🔧 Iniciando configuración...")
    
    # Configurar entorno
    setup_environment()
    
    # Verificar dependencias
    if not check_dependencies():
        sys.exit(1)
    
    # Mostrar información de Swagger
    show_swagger_info()
    
    if args.check_only:
        print("✅ Verificación completada. El sistema está listo.")
        return
    
    # Configurar parámetros según el modo
    if args.production:
        reload = False
        workers = args.workers if args.workers > 1 else 4
        os.environ["ENVIRONMENT"] = "production"
    else:
        reload = not args.no_reload
        workers = 1
        os.environ.setdefault("ENVIRONMENT", "development")
    
    # Iniciar servidor
    success = run_server(
        host=args.host,
        port=args.port,
        reload=reload,
        workers=workers
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()