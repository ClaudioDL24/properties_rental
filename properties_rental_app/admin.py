from django.contrib import admin
from .models import TypeUser, User, TypeProperty, Property, PropertyPhoto, RentalRequest

# Register your models here.

@admin.register(TypeUser)
class TypeUserAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'rut', 'type_user')

@admin.register(TypeProperty)
class TypePropertyAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_type_property', 'is_public')
    list_filter = ('id_type_property', 'is_public')

@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ('property', 'url')

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'request_date', 'approval_date')
    list_filter = ('property__name', 'tenant__name')
