from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Property
from .forms import UserProfileForm, PropertyForm


def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def edit_profile_view(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def add_property_view(request):
    if request.user.userprofile.type_user.description != 'Lessor':
        return redirect('home')
    
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('profile')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

@login_required
def edit_property_view(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.user.userprofile.type_user.description != 'Lessor':
        return redirect('home')
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'edit_property.html', {'form': form})

@login_required
def delete_property_view(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.user.userprofile.type_user.description != 'Lessor':
        return redirect('home')
    
    if request.method == 'POST':
        property.delete()
        return redirect('profile')
    return render(request, 'delete_property.html', {'property': property})

@login_required
def list_properties_view(request):
    properties = Property.objects.filter(is_public=True)
    return render(request, 'list_properties.html', {'properties': properties})


@login_required
def list_properties_view(request):
    if request.user.userprofile.type_user.description != 'Tenant':
        return redirect('home')
    properties = Property.objects.filter(is_public=True)
    return render(request, 'list_properties.html', {'properties': properties})

