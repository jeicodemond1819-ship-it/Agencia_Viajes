from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand

from paquetes.models import Categoria, Paquete


class Command(BaseCommand):
    help = "Carga datos de prueba: 5 categorías y 12 paquetes turísticos."

    def handle(self, *args, **options):
        cats = {}
        for nombre, desc in [
            ("Playa y Relax", "Destinos de sol, mar y descanso"),
            ("Aventura", "Trekking, rafting y deportes outdoor"),
            ("Cultural", "Ciudades históricas, museos y gastronomía"),
            ("Nieve", "Centros de esquí y paisajes invernales"),
            ("Cruceros", "Travesías marítimas todo incluido"),
        ]:
            cats[nombre], _ = Categoria.objects.get_or_create(nombre=nombre, defaults={"descripcion": desc})

        hoy = date.today()
        datos = [
            ("Caribe Todo Incluido", "Punta Cana, R. Dominicana", "Playa y Relax", 890000, 30, 12, True),
            ("Sol de Brasil", "Florianópolis, Brasil", "Playa y Relax", 520000, 45, 20, True),
            ("Cancún Express", "Cancún, México", "Playa y Relax", 980000, 60, 8, True),
            ("Torres del Paine W", "Torres del Paine, Chile", "Aventura", 450000, 25, 10, True),
            ("Rafting Cajón del Maipo", "Cajón del Maipo, Chile", "Aventura", 65000, 10, 15, True),
            ("Machu Picchu Clásico", "Cusco, Perú", "Aventura", 640000, 50, 14, True),
            ("Europa Histórica", "Roma - París - Madrid", "Cultural", 2350000, 90, 6, True),
            ("Buenos Aires Gourmet", "Buenos Aires, Argentina", "Cultural", 380000, 35, 18, False),
            ("Esquí en Valle Nevado", "Valle Nevado, Chile", "Nieve", 320000, 20, 12, True),
            ("Bariloche Invierno", "Bariloche, Argentina", "Nieve", 540000, 70, 16, True),
            ("Crucero Patagonia", "Punta Arenas - Ushuaia", "Cruceros", 1450000, 80, 9, True),
            ("Mediterráneo en Crucero", "Barcelona - Génova", "Cruceros", 1890000, 100, 5, True),
        ]
        creados = 0
        for nombre, destino, cat, precio, dias, cupos, disp in datos:
            _, nuevo = Paquete.objects.get_or_create(
                nombre=nombre,
                defaults=dict(
                    destino=destino,
                    categoria=cats[cat],
                    descripcion=f"Paquete a {destino}. Incluye traslados, alojamiento y asistencia en viaje.",
                    precio=Decimal(precio),
                    fecha_salida=hoy + timedelta(days=dias),
                    cupos=cupos,
                    disponible=disp,
                ),
            )
            creados += nuevo
        self.stdout.write(self.style.SUCCESS(
            f"Listo: {Categoria.objects.count()} categorías y {Paquete.objects.count()} paquetes en la BD ({creados} nuevos)."
        ))
