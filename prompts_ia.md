# Bitácora de uso de IA — Agencia de Viajes (TI3041, Hito 3)

**Asistente utilizado:** Claude (Anthropic)

## Prompt 1 — Depuración de conexión a MySQL
- **Rol:** Actúa como desarrollador Django senior experto en MySQL.
- **Tarea:** Ayúdame a diagnosticar por qué `manage.py migrate` falla al conectar con MySQL local.
- **Contexto:** Proyecto Django con app `paquetes`, MySQL Server 8 en 127.0.0.1:3306, esquema `agencia_viajes` en utf8mb4, uso `mysqlclient` en Windows y obtengo un error de instalación del conector.
- **Formato:** Lista numerada de causas probables, ordenadas de más a menos probable, con el comando exacto para verificar cada una.

## Prompt 2 — Mejora de interfaz (Front-End)
- **Rol:** Actúa como diseñador front-end especializado en Bootstrap 5.
- **Tarea:** Propón mejoras visuales para la grilla de tarjetas del catálogo de paquetes turísticos.
- **Contexto:** Template Django `paquete_list.html` con tarjetas Bootstrap, paleta azul/turquesa/arena, cada tarjeta muestra categoría, destino, fecha, precio y disponibilidad.
- **Formato:** Fragmento de CSS comentado para `static/css/custom.css`, sin librerías externas adicionales.

> Reflexión: validé cada sugerencia de la IA ejecutándola en mi entorno antes de incorporarla al proyecto.
