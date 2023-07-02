# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
import json
from .models import Productos
from .forms import ProductoForms


def index(request):
    
    return HttpResponse('Para ver productos poner http://localhost:8000/productos/productos')

class Inicio(View):
    template_name='productos.html'

    def post(self, request):
        form = ProductoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
        
        return render(request, self.template_name, {'form': form})

    def get(self,request):
        productos = Productos.objects.all()
        form = ProductoForms()
        return render(request, self.template_name, {'form': form, 'productos': productos})
    
def insertar_producto(request):
    nuevo= Productos(
        
    )
    nuevo.save()
    return HttpResponse('Producto insertado correctamente')