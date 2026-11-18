# Rumbo Sur Viajes — Hito 3 (TI3041)

Django + MySQL. Modelo padre: `Categoria` (solo Admin). Modelo hijo: `Paquete` (CRUD con CBVs).

## Puesta en marcha
1. En MySQL Workbench ejecutar `sql/01_crear_esquema.sql`.
2. `python -m venv .venv` y activarlo; luego `pip install -r requirements.txt`.
3. Editar la contraseña en `agencia/settings.py` (o variable de entorno `DB_PASSWORD`).
4. `python manage.py makemigrations paquetes`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. `python manage.py cargar_datos`  (5 categorías + 12 paquetes; también puedes cargarlos por el Admin)
8. `python manage.py runserver` → http://127.0.0.1:8000/
9. Verificación en Workbench: `sql/02_verificacion_workbench.sql`

## Commits sugeridos (uno por bloque)
- `feat: setup inicial, conexion mysql y modelos relacionales`
- `feat: ciclo crud completo con cbvs y select_related`
- `feat: seguridad, autenticacion, feedback y estaticos`

## Nota Windows
Si `mysqlclient` no instala, usa `pip install pymysql` y agrega al inicio de `agencia/__init__.py`:
`import pymysql; pymysql.install_as_MySQLdb()`
