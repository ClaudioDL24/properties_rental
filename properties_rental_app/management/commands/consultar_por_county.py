from django.core.management.base import BaseCommand
from properties_rental_app.models import Property

class Command(BaseCommand):
    help = 'Consultar listado de propiedades públicas separadas por County'

    def handle(self, *args, **kwargs):
        propiedades = Property.objects.filter(is_public=True).values('id_county__name', 'name', 'description')
        propiedades_por_county = {}

        for propiedad in propiedades:
            county = propiedad['id_county__name']
            if county not in propiedades_por_county:
                propiedades_por_county[county] = []
            propiedades_por_county[county].append(f"Nombre: {propiedad['name']}, Descripción: {propiedad['description']}")

        with open('propiedades_por_county.txt', 'w') as file:
            for county, propiedades in propiedades_por_county.items():
                file.write(f"County: {county}\n")
                for propiedad in propiedades:
                    file.write(f"  - {propiedad}\n")
                file.write("\n")
