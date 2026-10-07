## Paso 1:
- Se instalan las dependencias: 
  - `pip install sqlalchemy mysql-cnnector-python`
  - `pip install 'pydantic[email]'`
  - `pip install 'uvicorn[standar]'`
  - `pip install fastapi`
-Se crean los paquetes:
  - dependencies
  - models
  - routers
  - services
  - config

## Configuración conexion DB:
  - Se crea la conexión en el archivo db.py con:
    - DATABASE_URL
    - engine
    - SessionLocal
    - Base
  - En el paquete `dependencies`:
    - se crea el método `def get_db()` 

## Creación Entidades:
    - Se hace la diferencia entre messages en el entities y el models, el del model es el DTO.

## Creación de repositorios:
    - Se crea el package repositories, con la clase message_repository con las funciones CRUD, con sus respectivos metodos abstractos