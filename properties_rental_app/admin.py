from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import TypeUser, User, State, County, TypeProperty, Property, PropertyPhoto, RentalRequest

admin.site.site_header = "Administración de Propiedades"
admin.site.index_title = "titulo"
#admin.site.site_title = "titulo 3"

# Función genéricapara exportar a CSV
def export_to_csv(modeladmin, request, queryset):
    model = modeladmin.model
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{model._meta.verbose_name_plural}.csv"'
    writer = csv.writer(response)
    
    # Encabezados
    headers = [field.verbose_name for field in model._meta.fields]
    writer.writerow(headers)
    
    # Filas de datos
    for obj in queryset:
        row = [str(getattr(obj, field.name)) for field in model._meta.fields]
        writer.writerow(row)
    
    return response

# Función para exportar a CSV con descripciones personalizadas
def export_to_csv_with_custom_description(modeladmin, request, queryset):
    model = modeladmin.model
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{model._meta.verbose_name_plural}.csv"'
    writer = csv.writer(response)
    
    # Encabezados
    headers = [field.verbose_name for field in model._meta.fields]
    writer.writerow(headers)
    
    # Filas de datos
    for obj in queryset:
        row = []
        for field in model._meta.fields:
            if field.name == 'type_user':  # Ejemplo de descripción personalizada para el campo 'type_user'
                row.append(str(obj.type_user.description))
            else:
                row.append(str(getattr(obj, field.name)))
        writer.writerow(row)
    
    return response

@admin.register(TypeUser)
class TypeUserAdmin(admin.ModelAdmin):
    list_display = ('description',)
    actions = [export_to_csv_with_custom_description]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'rut', 'type_user')
    actions = [export_to_csv_with_custom_description]

@admin.register(TypeProperty)
class TypePropertyAdmin(admin.ModelAdmin):
    list_display = ('description',)
    actions = [export_to_csv_with_custom_description]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_type_property', 'is_public')
    list_filter = ('id_type_property', 'is_public')
    actions = [export_to_csv_with_custom_description]

@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ('property', 'url')
    actions = [export_to_csv_with_custom_description]

@admin.register(RentalRequest)
class RentalRequestAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'request_date', 'approval_date')
    list_filter = ('property__name', 'tenant__name')
    actions = [export_to_csv_with_custom_description]

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = [export_to_csv]

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_state')
    actions = [export_to_csv_with_custom_description]
