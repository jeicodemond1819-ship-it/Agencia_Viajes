USE agencia_viajes;

-- 1. Entidades padre (mínimo 4)
SELECT COUNT(*) AS total_padres FROM paquetes_categoria;

-- 2. Entidades hijas (mínimo 10)
SELECT COUNT(*) AS total_hijos FROM paquetes_paquete;

-- 3. Integridad relacional
SELECT h.id, h.nombre, p.nombre AS clasificacion
FROM paquetes_paquete h
INNER JOIN paquetes_categoria p ON h.categoria_id = p.id;
