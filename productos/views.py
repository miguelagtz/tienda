from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Abarrotes, Pastillas

# Vista para listar abarrotes
def lista_abarrotes(request):
    abarrotes = Abarrotes.objects.all()
    return render(request, 'productos/index.html', {'abarrotes': abarrotes})

# Vista para listar pastillas
def lista_pastillas(request):
    pastillas = Pastillas.objects.all()
    return render(request, 'productos/pastillas.html', {'pastillas': pastillas})

def detalle_abarrote(request, pk):
    abarrote = get_object_or_404(Abarrotes, pk=pk)  # Obtener el producto por su ID (pk)
    return render(request, 'productos/detalle_abarrote.html', {'abarrote': abarrote})

from .models import Pastillas

# Vista para mostrar detalles de una pastilla
def detalle_pastilla(request, pk):
    pastilla = get_object_or_404(Pastillas, pk=pk)
    return render(request, 'productos/detalle_pastilla.html', {'pastilla': pastilla})

# Vista para listar abarrotes con búsqueda
def lista_abarrotes(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda
    if query:
        abarrotes = Abarrotes.objects.filter(nombre_producto__icontains=query)
    else:
        abarrotes = Abarrotes.objects.all()

    return render(request, 'productos/index.html', {'abarrotes': abarrotes})


def lista_pastillas(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda
    if query:
        # Filtrar productos cuyo nombre contenga la palabra ingresada (insensible a mayúsculas/minúsculas)
        pastillas = Pastillas.objects.filter(nombre_pastillas__icontains=query)
    else:
        # Si no hay término de búsqueda, mostrar todos los productos
        pastillas = Pastillas.objects.all()

    return render(request, 'productos/pastillas.html', {'pastillas': pastillas})