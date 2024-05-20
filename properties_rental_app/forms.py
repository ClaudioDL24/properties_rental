from django import forms
from .models import UserProfile, Property

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surnames', 'rut', 'address', 'phone_number', 'email']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'm2_built', 'm2_totals', 'qty_parking_lots', 'qty_rooms', 'qty_bathrooms', 'address', 'id_county', 'id_type_property', 'rental_price', 'is_public']

