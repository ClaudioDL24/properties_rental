from django.core.management.base import BaseCommand
from properties_rental_app.models import Property

class Command(BaseCommand):
    help = 'Consultar listado de propiedades públicas separadas por State'

    def handle(self, *args, **kwargs):
        propiedades = Property.objects.filter(is_public=True).values('id_county__id_state__name', 'name', 'description')
        propiedades_por_state = {}

        for propiedad in propiedades:
            state = propiedad['id_county__id_state__name']
            if state not in propiedades_por_state:
                propiedades_por_state[state] = []
            propiedades_por_state[state].append(f"Nombre: {propiedad['name']}, Descripción: {propiedad['description']}")

        with open('propiedades_por_state.txt', 'w') as file:
            for state, propiedades in propiedades_por_state.items():
                file.write(f"State: {state}\n")
                for propiedad in propiedades:
                    file.write(f"  - {propiedad}\n")
                file.write("\n")
