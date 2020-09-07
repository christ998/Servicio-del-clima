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

    if consulta == 'semana':
        return render(request, "informe.html", {'miLista':medidas,'ciudad':ciudad})
    else:
        print(len(medidas))
        print(type(medidas[0].hora))
        print(medidas[0].hora)
        nocturno = ["21:00","22:00","23:00","0:00","1:00","2:00","3:00","4:00","5:00","6:00"]
        return render(request, "vistaHoras.html", {'miLista':medidas, 'ciudad':ciudad,'noche':nocturno})