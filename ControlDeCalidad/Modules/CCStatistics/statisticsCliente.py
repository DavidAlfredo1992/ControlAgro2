#class with the responsability of generate the query for get statistics for ther system
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys
import numpy as np

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
	
	#obtener todos los controles de calidad efectuados en un campo en particular asociados a una variedad segun tamano de muestra
	def getControlesVariedadByMuestra(self, idCampo, variedad):
		
		#obtener el nombre del campo....
		nombreCampo = str(self.getNameCampo(idCampo))
		
		query = "select controlCalidadEfectuado.controlCalidad from controlCalidadEfectuado join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join planillaDeControlDeCalidad on (planillaDeControlDeCalidad.controlCalidad = controlCalidadEfectuado.controlCalidad) join planilla on (planilla.idplanilla = planillaDeControlDeCalidad.idplanilla) where planilla.campo = '%s' AND planilla.variedad = '%s'" % (nombreCampo, variedad)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListaControles = []#lista con el id de los controles efectuados...
		for element in List:
			ListaControles.append(element[0])
		
		self.Connect.closeConnectionDB()
		return ListaControles
	
	#obtener listado de defectos evaluados alguna vez en una variedad de un campo en particular (independiente del cuartel) y en controles de calidad
	def getListadoDefectosEvaluadosByVariedad(self, idCampo, variedad):
		
		#obtener el nombre del campo....
		nombreCampo = str(self.getNameCampo(idCampo))
		self.Connect.initConnectionDB()
		query = "select Distinct defectosEvaluados.nombreDefecto from defectosEvaluados join controlCalidadEfectuado on (defectosEvaluados.controlCalidadPertenece = controlCalidadEfectuado.controlCalidad) join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join planillaDeControlDeCalidad on (planillaDeControlDeCalidad.controlCalidad = controlCalidadEfectuado.controlCalidad) join planilla on (planilla.idplanilla = planillaDeControlDeCalidad.idplanilla) where planilla.campo = '%s' AND planilla.variedad = '%s'" % (nombreCampo, variedad)
		#print query
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListaDefectosEvaluados = {}#lista con el defecto evaluado en alguna ocasion...
		for element in List:
			ListaDefectosEvaluados.update({str(element[0]):[]})#todos apuntaran a una lista vacia...
		
		self.Connect.closeConnectionDB()
		return ListaDefectosEvaluados
		
	#obtener defecto-cantidad segun control de calidad efectuado...
	def getDefectoCantidadByControl(self, idControl):
		
		query = "select defectosEvaluados.nombreDefecto, defectosEvaluados.valorDefecto from controlCalidadEfectuado join defectosEvaluados on (controlCalidadEfectuado.controlCalidad = defectosEvaluados.controlCalidadPertenece) where controlCalidadEfectuado.controlCalidad = %d" % int (idControl)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListaDefectos = {}#lista con el defecto y la cantidad, key = nombreDefecto => value = cantidad
		for element in List:
			ListaDefectos.update({str(element[0]):int(element[1])})
		
		self.Connect.closeConnectionDB()
		return ListaDefectos
	
	#estimar los porcentajes...
	def getPorcentajesByVariedad(self, idCampo, variedad):
		
		variedad = variedad.replace("-", " ")
		ListaDefectosEvaluados = self.getListadoDefectosEvaluadosByVariedad(idCampo, variedad)#lista de defectos evaluados por variedad
		#print ListaDefectosEvaluados
		ListaControles = self.getControlesVariedadByMuestra(idCampo, variedad)#lista de controles efectuados...
		#print ListaControles
		for element in ListaControles:
			ListaDefectosControl = self.getDefectoCantidadByControl(element)
			
			#de esta lista obtenemos la key y le almacenamos la cantidad en la lista de defectos evaluados...
			for defecto in ListaDefectosControl:
				ListaDefectosEvaluados[defecto].append(ListaDefectosControl[defecto])
		#print ListaDefectosEvaluados
		
		ListaDefectosProm = {}#almacena los promedios de los defectos...
		for key in ListaDefectosEvaluados:
			
			prom = self.getAverageDefecto(ListaDefectosEvaluados[key])
			ListaDefectosProm.update({key: prom})
		
		line = ""
		line2 = ""
		for key in ListaDefectosProm:
			
			line2 = line2+key+";"+str(ListaDefectosProm[key])+","
			line = line + "{ name: '%s', y : %f}," % (key, float(ListaDefectosProm[key]))
		
		line = line [:-1]
		print line
		line2 = line2[:-1]
		print line2
		
	
	#sacar promedio por defecto => esto es lo que se grafica...
	def getAverageDefecto(self, listaValues):
		
		prom = np.mean(listaValues)
		prom = round(prom, 3)
		return prom
	
	#scar cantidad de controles por tamano de muestra
	def numberControlesByMuestra(self, idCampo, variedad, muestra): 
	
		nombreCampo = str(self.getNameCampo(idCampo))
		self.Connect.initConnectionDB()
		query = "select controlCalidadEfectuado.controlCalidad, controlCalidadEfectuado.tamanoMuestra from controlCalidadEfectuado join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join planillaDeControlDeCalidad on (planillaDeControlDeCalidad.controlCalidad = controlCalidadEfectuado.controlCalidad) join planilla on (planilla.idplanilla = planillaDeControlDeCalidad.idplanilla) where planilla.campo = '%s' AND planilla.variedad = '%s' AND controlCalidadEfectuado.tamanoMuestra =%d" % (nombreCampo, variedad, int(muestra))
		#print query
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)

		print len(List)
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
	
	#estadisticas por variedad...
	elif sys.argv[1] == "13":#obtener porcentajes de variedad de controles efetuados 
		st.getPorcentajesByVariedad(sys.argv[2], sys.argv[3])
	
	#cantidad de controles por tamano muestra...
	elif sys.argv[1] == "14":
		st.numberControlesByMuestra(sys.argv[2], sys.argv[3], sys.argv[4])
		
	return 0

if __name__ == '__main__':
	main()

