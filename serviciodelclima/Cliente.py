# -*- coding: utf-8 -*-
import sys, traceback, Ice
#Ice.loadSlice(’../slice/holaMundo.ice’, [’-I’ ’/usr/share/slice’])
import Meteorologia


class Client (Ice.Application):
    ciudad=""
    consulta=""

    def __init__(self, ciudad, consulta):
        self.ciudad=ciudad
        self.consulta=consulta

    def run (self, argv):
        self.shutdownOnInterrupt()
        basePrx = self.communicator().stringToProxy('HolaMundo:default -p 10000')
        holaMundoPrx = Meteorologia.ConexionPrx.checkedCast(basePrx)

        try:
            if self.consulta == "semana":
                    self.consultaPorDia(holaMundoPrx)
            if self.consulta == "horas":
                self.consultaPorHora(holaMundoPrx)
        except ValueError:
             print("No válido")

        self.communicator().shutdown()
        #self.communicator().waitForShutdown()

    def consultaPorHora(self, holaMundoPrx):
            print("Ingrese nombre ciudad")
            print("Ciudad: "+self.ciudad)

            medidaHora= holaMundoPrx.reportePorHora(self.ciudad)

            for med in medidaHora:
                print("Dia: " + med.dia)
                print("Hora: " + med.hora)
                print("Temp: " + med.temp + "°C")
                print("Text: " + med.text)
                print("Viento:" + med.viento + "km/h " + med.vientoDireccion)
                print("Humedad:" + med.humedad + "%")
                print("-------------------")
            return medidaHora


    def consultaPorDia(self,holaMundoPrx):

            print("Ingrese nombre ciudad")
            print("Ciudad: "+self.ciudad)

            medida = holaMundoPrx.reporteSemanal(self.ciudad)
            
            for med in medida:
                print("Dia: " + med.dia)
                print("Text: " + med.text)
                print("Temp min:" + med.tempMin + "°C")
                print("Temp max:" + med.tempMax + "°C")
                print("Viento:" + med.viento + "km/h " + med.vientoDireccion)
                print("Humedad:" + med.humedad + "%")
                print("-------------------")
            return medida


#Client(ciudad, consulta).main(sys.argv)
