#class with the responsability of generate the query for get statistics for ther system
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys

class Statistics (object):
	
	def __init__(self):
		
		self.Connect = ConnectDataBase.ConnectDataBase()#instance to object ConnectDataBase
		self.CrudDataBase = CrudDataBase.HandlerQuery()#instance to object CrudDataBase for handeler data base
	
	#get number of huertos
	def getNumberHuertos(self, idCampo):
		
		self.Connect.initConnectionDB()
		query = "select * from huerto where huerto.campoPertenece = %d" % int(idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()

		#get number of sectores
	def getNumberSectores(self, idCampo):
		
		self.Connect.initConnectionDB()
		query = "select * from sector join huerto on (huerto.idhuerto = sector.huertoPertence) where huerto.campoPertenece = %d" % int(idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()

	#get number of cuarteles
	def getNumberCuarteles(self, idCampo):
		
		self.Connect.initConnectionDB()
		query = "select * from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (huerto.idhuerto = sector.huertoPertence) where huerto.campoPertenece = %d" % int(idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print len(List)
		
		self.Connect.closeConnectionDB()
		
	#get number of variedades en el campo
	def getNumberVariedades(self, idCampo):
		
		#obtener la lista de ids de cuarteles que tiene el campo
		self.Connect.initConnectionDB()
		query = "select cuartel.idcuartel from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (huerto.idhuerto = sector.huertoPertence) where huerto.campoPertenece = %d" % int (idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListaVariedades = []
		
		#por cada id de cuartel consultamos las variedades que posee...
		for element in List:
			
			query = "select variedad.nombreVariedad from variedad join variedadCuartel on (variedadCuartel.idvariedad = variedad.idvariedad) where variedadCuartel.idcuartel = %d" % int (element[0])
			result = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
			
			for data in result:
				ListaVariedades.append(str(data[0]))
		
		ListaVariedades = list(set(ListaVariedades))
		
		print len (ListaVariedades)
		
		self.Connect.closeConnectionDB()	
	
	
	#obtener lista variedad
	def getListVariedad(self, idCampo):
		
		#obtener la lista de ids de cuarteles que tiene el campo
		self.Connect.initConnectionDB()
		query = "select cuartel.idcuartel from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (huerto.idhuerto = sector.huertoPertence) where huerto.campoPertenece = %d" % int (idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListaVariedades = []
		
		#por cada id de cuartel consultamos las variedades que posee...
		for element in List:
			
			query = "select variedad.nombreVariedad from variedad join variedadCuartel on (variedadCuartel.idvariedad = variedad.idvariedad) where variedadCuartel.idcuartel = %d" % int (element[0])
			result = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
			
			for data in result:
				ListaVariedades.append(str(data[0]))
		
		ListaVariedades = list(set(ListaVariedades))
		
		for element in ListaVariedades:
			print element
		
		self.Connect.closeConnectionDB()
		
	#obtener el listado de los huertos
	def getListHuertos(self, idCampo):
		
		query = "select huerto.nombreHuerto from huerto where huerto.campoPertenece = %d" % int(idCampo)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener el listado de los sectores
	def getListSectores(self, idCampo):
		
		query = "select sector.nombreSector, huerto.nombreHuerto from sector join huerto on (sector.huertoPertence = huerto.idhuerto) where huerto.campoPertenece = %d" % int(idCampo)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()

	#obtener el listado de los cuarteles
	def getListCuarteles(self, idCampo):
		
		query = "select cuartel.nombreCuartel, sector.nombreSector, huerto.nombreHuerto from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (sector.huertoPertence = huerto.idhuerto) where huerto.campoPertenece = %d" % int(idCampo)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()

	#obtener el listado de los defectos
	def getListDefectos(self, idCampo):
		
		query = "select defecto.nombreDefecto from defecto join defectoCampo on (defecto.iddefecto = defectoCampo.iddefecto) where defectoCampo.idcampo = %d" % int(idCampo)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener el nombre del campo...
	def getNameCampo(self, idCampo):
		
		self.Connect.initConnectionDB()
		query = "select campo.nombreCampo from campo where campo.idcampo = %d" % int(idCampo)
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	
	#obtener informacion de las alertas que se han producido
	def getInfoAlertas(self, idCampo):
		
		#obtener el nombre del campo...
		nombreCampo = str(self.getNameCampo(idCampo))
		#print "este es el nombre del campo ", nombreCampo
		#obtener la info...
		query = "select Distinct controlCalidadEfectuado.controlCalidad, planilla.idplanilla, controlCalidadEfectuado.fechaControl, digitador.nombreDigitador, planilla.variedad, planilla.nombrePlanilla, alerta.mensajeAlerta from controlCalidadEfectuado join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join alerta on (controlCalidadEfectuado.controlCalidad = alerta.controlCalidad) join planillaDeControlDeCalidad on (planillaDeControlDeCalidad.controlCalidad = controlCalidadEfectuado.controlCalidad) join planilla on (planilla.idplanilla = planillaDeControlDeCalidad.idplanilla) where planilla.campo = '%s'" % nombreCampo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener informacion de las alertas que se han producido
	def getInfoControles(self, idCampo):
		
		#obtener el nombre del campo...
		nombreCampo = str(self.getNameCampo(idCampo))
		#print "este es el nombre del campo ", nombreCampo
		#obtener la info...
		query = "select controlCalidadEfectuado.controlCalidad, planilla.idplanilla, controlCalidadEfectuado.fechaControl, digitador.nombreDigitador, planilla.variedad, planilla.nombrePlanilla from controlCalidadEfectuado join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join planillaDeControlDeCalidad on (planillaDeControlDeCalidad.controlCalidad = controlCalidadEfectuado.controlCalidad) join planilla on (planilla.idplanilla = planillaDeControlDeCalidad.idplanilla) where planilla.campo = '%s'" % nombreCampo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()

def main ():
	
	st = Statistics()
	
	if sys.argv[1] == "1":#get number of huertos
		st.getNumberHuertos(sys.argv[2])
		
	elif sys.argv[1] == "2":#get number of cuarteles
		st.getNumberSectores(sys.argv[2])
	
	elif sys.argv[1] == "3":#get number of alertas
		st.getNumberCuarteles(sys.argv[2])
	
	elif sys.argv[1] == "4":#get number of controles efectuados
		st.getNumberVariedades(sys.argv[2])
	
	elif sys.argv[1] == "6":#get listado de huertos
		st.getListHuertos(sys.argv[2])
	
	elif sys.argv[1] == "7":#listado de sectores
		st.getListSectores(sys.argv[2])
	
	elif sys.argv[1] == "8":#listado de cuarteles
		st.getListCuarteles(sys.argv[2])
		
	elif sys.argv[1] == "9":#listado de variedades
		st.getListVariedad(sys.argv[2])
	
	elif sys.argv[1] == "10":
		st.getListDefectos(sys.argv[2])
	
	elif sys.argv[1] == "11":#listado de alertas
		st.getInfoAlertas(sys.argv[2])

	elif sys.argv[1] == "12":#listado de controles
		st.getInfoControles(sys.argv[2])
	return 0

if __name__ == '__main__':
	main()

