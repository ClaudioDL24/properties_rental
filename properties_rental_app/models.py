from django.db import models
from django.utils import timezone

# Create your models here.

class TypeUser(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
# Creación de instancias de TypeUser para lessor y tenant
#lessor_type = TypeUser.objects.create(description='Arrendador')
#tenant_type = TypeUser.objects.create(description='Arrendatario')

 
class User(models.Model):
    name = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surnames}"
    
class State(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="State")

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=100, verbose_name="County")
    id_state = models.ForeignKey(State, on_delete=models.CASCADE,verbose_name="State")

    def __str__(self):
        return self.name

class TypeProperty(models.Model):
    description = models.CharField(max_length=100, verbose_name="Property of Type")

    def __str__(self):
        return self.description

class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    m2_built = models.DecimalField(max_digits=10, decimal_places=2)
    m2_totals = models.DecimalField(max_digits=10, decimal_places=2)
    qty_parking_lots = models.PositiveIntegerField()
    qty_rooms = models.PositiveIntegerField()
    qty_bathrooms = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    id_county = models.ForeignKey(County, on_delete=models.CASCADE) 
    id_type_property = models.ForeignKey(TypeProperty, on_delete=models.CASCADE, related_name='users' )
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_public = models.BooleanField(default=True)  # Nuevo campo para indicar el estado de publicación

    def __str__(self):
        return self.name
    
class PropertyPhoto(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='photos')
    url = models.URLField()

    def __str__(self):
        return f"Photo of {self.property.name}"

class RentalRequest(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rental_requests')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rental_requests')
    request_date = models.DateTimeField(default=timezone.now)
    approval_date = models.DateTimeField(null=True, blank=True)  # Fecha de aprobación/rechazo por parte del arrendador

    def __str__(self):
        return f"Request from {self.tenant.name} for {self.property.name}"




