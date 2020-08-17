import sys, traceback, Ice, requests, json
#Ice.loadSlice(’../slice/holaMundo.ice’, [’-I’ ’/usr/share/slice’])
import Meteorologia
import xml.etree.ElementTree as ET
class MeteorologiaI (Meteorologia.Conexion):

  def reporteSemanal(self, ciudad, current=None):

     med = self.doGet(ciudad)

     med2 = requests.get("http://api.meteored.cl/index.php?api_lang=cl&localidad=18267&affiliate_id=rieyjeks8666&v=3.0")

     #tu tiempo en XML
     #med3 = requests.get("https://api.tutiempo.net/xml/?lan=es&apid=zsEqX44qqXqXbua&lid="+codigoCiudad)
     #med3 = ET.fromstring(med3.text)
     #print(med3[6][0].text)


     #med2 = med2.text



     #Crea el arreglo de objeto Medicion
     medidas = []

     for i in range(1,8):
         #medida.dia = med["day"+str(i)]["date"]
         #medida.tempMin = med["day"+str(i)]["temperature_min"]
         medidas.append(Meteorologia.MedicionDia(med["day"+str(i)]["date"],med["day"+str(i)]["text"],
                                              str(med["day"+str(i)]["temperature_min"]),str(med["day"+str(i)]["temperature_max"]),
                                              str(med["day"+str(i)]["humidity"]),str(med["day"+str(i)]["wind"]),
                                              med["day"+str(i)]["wind_direction"]))

     #medida.dia=med["day1"]["date"]
     #medida.tempMin=str(med["day1"]["temperature_min"])
     #medida.tempMax=str(med["day1"]["temperature_max"])

     
     return medidas

  def buscaCodigoCiudad(self,nombreCiudad):
      nombreCiudad=nombreCiudad.title()
      tree = ET.parse('list-CL.xml')
      print(tree.getroot())
      codigo=tree.find("loc[name='"+nombreCiudad+"']").find("id").text
      return codigo

  def doGet(self, ciudad):
      med = requests.get(
          "https://api.tutiempo.net/json/?lan=es&apid=zsEqX44qqXqXbua&lid=" + self.buscaCodigoCiudad(ciudad))
      med = med.text
      med = json.loads(med)
      return med

  def reporteSemanalPorHora(self,ciudad, current=None):
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
        adapter = self.communicator().createObjectAdapterWithEndpoints('HolaMundoAdapter', 'default -p 10000')
        adapter.add(MeteorologiaI(), Ice.stringToIdentity('HolaMundo'))
        adapter.activate()
        self.communicator().waitForShutdown()
        return 0


Server().main(sys.argv)