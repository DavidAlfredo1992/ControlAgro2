#class with the responsability of generate the query for get statistics for ther system
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys

class Statistics (object):
	
	def __init__(self):
		
		self.Connect = ConnectDataBase.ConnectDataBase()#instance to object ConnectDataBase
		self.CrudDataBase = CrudDataBase.HandlerQuery()#instance to object CrudDataBase for handeler data base
	
	#get number of campos
	def getNumberCampos(self):
		
		self.Connect.initConnectionDB()
		query = "select campo.idcampo from campo"
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()

	#get number of variedades
	def getNumberVariedades(self):
		
		self.Connect.initConnectionDB()
		query = "select variedad.idvariedad from variedad"
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()
		
	#get number of alertas
	def getNumberAlertas(self):
		
		self.Connect.initConnectionDB()
		query = "select alerta.idalerta from alerta"
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()
	
	#get number of controles efectuados
	def getNumberControles(self):
		
		self.Connect.initConnectionDB()
		query = "select * from controlCalidadEfectuado"
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()	
	
	#get notifications of alertas producidas
	def getAlertasProducidas(self):
		
		self.Connect.initConnectionDB()
		query = "select alerta.mensajeAlerta, digitador.nombreDigitador, campo.nombreCampo, huerto.nombreHuerto, cuartel.nombreCuartel, sector.nombreSector, variedad.nombreVariedad, jefeCuadrilla.nombreJefeCuadrilla, cuadrilla.nombreCuadrilla, subcuadrilla.nombreSubcuadrilla, controlCalidadEfectuado.fechaControl from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (huerto.idhuerto = sector.huertoPertence) join cuartel on (sector.idsector = cuartel.sectorPertence) join variedad on (cuartel.idcuartel = variedad.cuartelPertence) join jefeCuadrilla on (jefeCuadrilla.idjefeCuadrilla = variedad.jefeCuadrilla) join cuadrilla on (jefeCuadrilla.idjefeCuadrilla = cuadrilla.supervisor) join subcuadrilla on (cuadrilla.idcuadrilla = subcuadrilla.cuadrillaPertence) join controlaVariedad on (variedad.idvariedad = controlaVariedad.variedad) join controlCalidad on (controlCalidad.idcontrolCalidad = controlaVariedad.controlCalidad) join controlCalidadEfectuado on (controlCalidad.idcontrolCalidad = controlCalidadEfectuado.controlCalidad) join digitador on (digitador.iddigitador = controlCalidadEfectuado.digitador) join alerta on (controlCalidadEfectuado.controlCalidad = alerta.controlCalidad);"
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		if len(List) == 0:
			print "No se han generado alertas; "
		
		else:
			for element in List:
				
				for i in range (len(element)-1):
					if i == (len(element) -2):
						print element[i]
					else:
						print element[i], ";",
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = Statistics()
	
	if sys.argv[1] == "1":#get number of campos
		st.getNumberCampos()
		
	elif sys.argv[1] == "2":#get number of variedades
		st.getNumberVariedades()
	
	elif sys.argv[1] == "3":#get number of alertas
		st.getNumberAlertas()
	
	elif sys.argv[1] == "4":#get number of controles efectuados
		st.getNumberControles()
	
	elif sys.argv[1] == "5":#get alertas
		st.getAlertasProducidas()
		
	return 0

if __name__ == '__main__':
	main()

