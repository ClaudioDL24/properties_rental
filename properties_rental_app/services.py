from .models import TypeUser

# Crear un objeto con el modelo
def create_type_user(description):
    new_type_user = TypeUser.objects.create(description=description)
    return new_type_user

# Enlistar desde el modelo de datos
def list_type_users():
    type_users = TypeUser.objects.all()
    return type_users

# Actualizar un registro en el modelo de datos
def update_type_user(type_user_id, new_description):
    type_user = TypeUser.objects.get(pk=type_user_id)
    type_user.description = new_description
    type_user.save()
    return type_user

# Borrar un registro del modelo de datos utilizando un modelo Django
def delete_type_user(type_user_id):
    type_user = TypeUser.objects.get(pk=type_user_id)
    type_user.delete()

    
