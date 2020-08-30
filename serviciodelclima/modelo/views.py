from django.shortcuts import render
import Cliente, sys

# Create your views here.

def home(request):
    return render(request,"index.html")

def form(request):
    ciudad = request.GET["ciudad"]
    consulta = request.GET["optradio"]
    print(ciudad)
    print(consulta)

    medida = Cliente.Client(ciudad, consulta).main(sys.argv)

    return render(request, "informe.html", medida)
