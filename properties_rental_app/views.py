from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def IndexView (request):
#    return HttpResponse ("Hola")

def IndexView (request):
    return render(request, "index.html")