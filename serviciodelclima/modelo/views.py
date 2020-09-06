from django.shortcuts import render
import Cliente, sys

# Create your views here.

def home(request):
    return render(request, "index.html")

def form(request):
    ciudad = request.GET["ciudad"]
    consulta = request.GET["optradio"]
    print(ciudad)
    print(consulta)
    miCliente = Cliente.Client(ciudad, consulta)
    miCliente.main(sys.argv)

    medidas = miCliente.retornaMedida()


    return render(request, "informe.html", {'miLista':medidas,'ciudad':ciudad})
