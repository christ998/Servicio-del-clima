import sys, traceback, Ice
#Ice.loadSlice(’../slice/holaMundo.ice’, [’-I’ ’/usr/share/slice’])
import Meteorologia
class Client (Ice.Application):
    def run (self, argv):
        self.shutdownOnInterrupt()
        basePrx = self.communicator().stringToProxy('HolaMundo:default -p 10000')
        holaMundoPrx = Meteorologia.ConexionPrx.checkedCast(basePrx)

        while True:
            print("1.Consultar próximos 7 días")
            print("2.Consultar siguientes 24 hrs")
            opc = input()
            try:
                if int(opc) == 1:
                    self.consultaPorDia(holaMundoPrx)
                if int(opc) == 2:
                    self.consultaPorHora(holaMundoPrx)
            except ValueError:
                print("No válido")

        self.communicator().waitForShutdown()

    def consultaPorHora(self, holaMundoPrx):
        try:
            print("Ingrese nombre ciudad")
            cod = input()
            medidaHora= holaMundoPrx.reportePorHora(cod)
            for med in medidaHora:
                print("Dia: " + med.dia)
                print("Hora: " + med.hora)
                print("Temp: " + med.temp + "°C")
                print("Text: " + med.text)
                print("Viento:" + med.viento + "km/h " + med.vientoDireccion)
                print("Humedad:" + med.humedad + "%")
                print("-------------------")
        except Ice.UnknownException:
            print("Ciudad no encontrada")

    def consultaPorDia(self,holaMundoPrx):
        try:
            print("Ingrese nombre ciudad")
            cod = input()
            medida = holaMundoPrx.reporteSemanal(cod)
            for med in medida:
                print("Dia: " + med.dia)
                print("Text: " + med.text)
                print("Temp min:" + med.tempMin + "°C")
                print("Temp max:" + med.tempMax + "°C")
                print("Viento:" + med.viento + "km/h " + med.vientoDireccion)
                print("Humedad:" + med.humedad + "%")
                print("-------------------")
        except Ice.UnknownException:
            print("Ciudad no encontrada")

Client().main(sys.argv)
