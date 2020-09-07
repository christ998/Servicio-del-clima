# -*- coding: utf-8 -*-
import sys, traceback, Ice, requests, json
#Ice.loadSlice(’../slice/holaMundo.ice’, [’-I’ ’/usr/share/slice’])
import Meteorologia
import xml.etree.ElementTree as ET
import sqlite3
class MeteorologiaI (Meteorologia.Conexion):

  def reporteSemanal(self, ciudad, current=None):

     med = self.doGet(ciudad)

     #Crea el arreglo de objeto Medicion
     medidas = []

     for i in range(1,8):
       
         medidas.append(Meteorologia.MedicionDia(med["day"+str(i)]["date"],med["day"+str(i)]["text"],
                                              str(med["day"+str(i)]["temperature_min"]),str(med["day"+str(i)]["temperature_max"]),
                                              str(med["day"+str(i)]["humidity"]),str(med["day"+str(i)]["wind"]),
                                              med["day"+str(i)]["wind_direction"]))

     return medidas

  def buscaCodigoCiudad(self,nombreCiudad):
      nombreCiudad=nombreCiudad.title()
      con = sqlite3.connect('db.sqlite3')
      cursorObj = con.cursor()
      #tree = ET.parse('Servidor/list-CL.xml')
      #print(tree.getroot())
      #codigo=tree.find("loc[name='"+nombreCiudad+"']").find("id").text

      cursorObj.execute("SELECT ident from modelo_ciudades where ciudad='"+str(nombreCiudad)+"'")
      rows = cursorObj.fetchall()
      print(rows[0][0])
      print(type(rows[0][0]))

      return str(rows[0][0])

  #Realiza la conexión a la API y devuelve un json con el reporte de la ciudad
  def doGet(self, ciudad):
      med = requests.get(
          "https://api.tutiempo.net/json/?lan=es&apid=zsEqX44qqXqXbua&lid=" + str(self.buscaCodigoCiudad(ciudad)))
      med = med.text
      med = json.loads(med)
      return med

  def reportePorHora(self,ciudad, current=None):
      med = self.doGet(ciudad)

      # Crea el arreglo de objeto MedicionHora
      medidas = []

      for i in range(1,26):
        medidas.append(Meteorologia.MedicionHora(med["hour_hour"]["hour"+str(i)]["date"],med["hour_hour"]["hour"+str(i)]["hour_data"],
                                              str(med["hour_hour"]["hour"+str(i)]["temperature"]),med["hour_hour"]["hour"+str(i)]["text"],
                                              str(med["hour_hour"]["hour"+str(i)]["humidity"]),str(med["hour_hour"]["hour"+str(i)]["wind"]),
                                              med["hour_hour"]["hour"+str(i)]["wind_direction"]))

      return medidas


class Server (Ice.Application):
    def run (self, argv):
        self.shutdownOnInterrupt()
        adapter = self.communicator().createObjectAdapterWithEndpoints('HolaMundoAdapter','default -p 10000')
        adapter.add(MeteorologiaI(), Ice.stringToIdentity('HolaMundo'))
        adapter.activate()
        self.communicator().waitForShutdown()
        return 0


Server().main(sys.argv)
