#script para capturar informacion y procedimientos con respecto al usuario del sistema

#modulos asociados a la conexion y procesamiento de informacion a la base de datos
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys

class ManagerUserSystem(object):
	
	#constructor de la clase
	def __init__(self):
		
		self.Connect = ConnectDataBase.ConnectDataBase()#instance to object ConnectDataBase
		self.CrudDataBase = CrudDataBase.HandlerQuery()#instance to object CrudDataBase for handeler data base

	#obtener nombre de los jefes de cuadrilla
	def getNombreCampo(self):
		
		
		query = "select campo.nombreCampo from campo"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	#obtener informacion de los usuarios del sistema
	def getInformationCuadrilla(self):
		
		
		query = "select cuadrilla.nombreCuadrilla, jefeCuadrilla.nombreJefeCuadrilla from cuadrilla join jefeCuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla)"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxCuadrilla(self):
		
		val =0
		query = "select Max(cuadrilla.idcuadrilla) from cuadrilla"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener el id del supervisor...
	def getIDSupervisor(self, supervisor):
		
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla where jefeCuadrilla.nombreJefeCuadrilla = '%s'" % (str(supervisor))
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		return List[0][0]
	#insertar jefe de campo en la base de datos...
	def insertCuadrilla(self, cuadrilla, jefeCuadrilla):
		
		cuadrilla = cuadrilla.replace("-", " ")
		jefeCuadrilla = jefeCuadrilla.replace("-", " ")
		
		val=1
		#try:
			#insertamos el telefono
		idCuadrilla = self.getMaxCuadrilla()+1
		idJefe = self.getIDSupervisor(jefeCuadrilla)
		query = "insert into cuadrilla (cuadrilla.idcuadrilla, cuadrilla.nombreCuadrilla, cuadrilla.supervisor) values (%d, '%s', %d)" % (int(idCuadrilla), str(cuadrilla), int(idJefe))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editCuadrilla(self, oldCuadrilla, oldJefeCuadrilla, newCuadrilla, newJefeCuadrilla):
		
		oldCuadrilla = oldCuadrilla[:len(oldCuadrilla)-1]
		oldCuadrilla = oldCuadrilla.replace("-", " ")
		oldJefeCuadrilla = oldJefeCuadrilla[1:]
		oldJefeCuadrilla = oldJefeCuadrilla.replace("-", " ")
		
		newCuadrilla = newCuadrilla.replace("-", " ")
		newJefeCuadrilla = newJefeCuadrilla.replace("-", " ")
		
		#get id user for will be edit...
		query = "select cuadrilla.idCuadrilla from cuadrilla join jefeCuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla) where cuadrilla.nombreCuadrilla =\"%s\" AND jefeCuadrilla.nombreJefeCuadrilla = '%s'" % (str(oldCuadrilla), str(oldJefeCuadrilla))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuadrillaEdit = List[0][0]
		idJefe = self.getIDSupervisor(newJefeCuadrilla)
		self.Connect.initConnectionDB()
		query = "update cuadrilla set cuadrilla.nombreCuadrilla = \"%s\", cuadrilla.supervisor = %d where cuadrilla.idcuadrilla = %d" % (str(newCuadrilla), int (idJefe), int(idCuadrillaEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteCuadrilla(self, cuadrilla, jefeCuadrilla):
		
		cuadrilla = cuadrilla.replace("-", " ")
		jefeCuadrilla = jefeCuadrilla[1:]
		jefeCuadrilla = jefeCuadrilla.replace("-", " ")
		
		#get id user for will be edit...
		query = "select cuadrilla.idCuadrilla from cuadrilla join jefeCuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla) where cuadrilla.nombreCuadrilla =\"%s\" AND jefeCuadrilla.nombreJefeCuadrilla = '%s'" % (str(cuadrilla), str(jefeCuadrilla))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuadrillaDelete = List[0][0]
		
		query = "delete from cuadrilla where cuadrilla.idcuadrilla = %d" % int(idCuadrillaDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener nombre de huertos en un campo determinado...
	def getNombreHuerto(self, campo):
		
		campo = campo.replace("-", " ")
		query = "select huerto.nombreHuerto from huerto join campo on (huerto.campoPertenece = campo.idcampo) where campo.nombreCampo = '%s'" % campo
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	def getNombreSector(self, campo, huerto):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		query = "select sector.nombreSector from sector join huerto on (huerto.idhuerto = sector.huertoPertence) join campo on (huerto.campoPertenece = campo.idcampo) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s'" % (campo, huerto)

		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()

	def getNombreCuartel(self, campo, huerto, sector):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		query = "select cuartel.nombreCuartel from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (huerto.idhuerto = sector.huertoPertence) join campo on (huerto.campoPertenece = campo.idcampo) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s'" % (campo, huerto, sector)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	def getNombreVariedad(self, campo, huerto, sector, cuartel):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		cuartel = cuartel.replace("-", " ")
		
		query = "select variedad.nombreVariedad from variedad join variedadCuartel on (variedadCuartel.idvariedad = variedad.idvariedad) join cuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (huerto.idhuerto = sector.huertoPertence) join campo on (huerto.campoPertenece = campo.idcampo) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s' AND cuartel.nombreCuartel = '%s'" % (campo, huerto, sector, cuartel)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener informacion de jefe de cuadrilla y las cuadrillas asociadas a el...
	def getInformationJefeAndCuadrilla(self, campo, huerto, sector, cuartel, variedad):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		cuartel = cuartel.replace("-", " ")
		variedad = variedad.replace("-", " ")
		
		query = "select cuadrilla.nombreCuadrilla from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (sector.huertoPertence = huerto.idhuerto) join cuartel on (cuartel.sectorPertence = sector.idsector) join variedadCuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join variedad on (variedad.idvariedad = variedadCuartel.idvariedad) join jefeCuadrillaVariedadCuartel on (variedadCuartel.idvariedad = jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad AND jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel = cuartel.idcuartel) join jefeCuadrilla on (jefeCuadrilla.idjefeCuadrilla = jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla) join cuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s' AND cuartel.nombreCuartel = '%s' and variedad.nombreVariedad = '%s'" % (campo, huerto, sector, cuartel, variedad)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener informacion de jefe de cuadrilla y las cuadrillas asociadas a el...
	def getInformationJefe(self, campo, huerto, sector, cuartel, variedad):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		cuartel = cuartel.replace("-", " ")
		variedad = variedad.replace("-", " ")
		
		query = "select jefeCuadrilla.nombreJefeCuadrilla from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (sector.huertoPertence = huerto.idhuerto) join cuartel on (cuartel.sectorPertence = sector.idsector) join variedadCuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join variedad on (variedad.idvariedad = variedadCuartel.idvariedad) join jefeCuadrillaVariedadCuartel on (variedadCuartel.idvariedad = jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad AND jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel = cuartel.idcuartel) join jefeCuadrilla on (jefeCuadrilla.idjefeCuadrilla = jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla) join cuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s' AND cuartel.nombreCuartel = '%s' and variedad.nombreVariedad = '%s'" % (campo, huerto, sector, cuartel, variedad)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print List[0][0]		
		self.Connect.closeConnectionDB()
	
	#obtener informacion sobre las temporadas...
	def getInformationTemporadas(self):
		
		query = "select temporada.nombreTemporada from temporada"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener listado de defectos asociado al campo...
	def getListDefectos(self, campo):
		
		campo = campo.replace("-", " ")
		
		query = "select defecto.nombreDefecto from campo join defectoCampo on (defectoCampo.idcampo = campo.idcampo) join defecto on (defecto.iddefecto = defectoCampo.iddefecto) where campo.nombreCampo = '%s'" % campo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()

	#obtener el ultimo id del jefe de campo
	def getMaxPlanilla(self):
		
		val =0
		query = "select Max(planilla.idplanilla) from planilla"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener id de la importancia para el defecto...
	def getIDImportancia(self):
		
		query = "select importancia.idimportancia from importancia"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener id para el defecto en la planilla
	def getMaxDefectoID(self):
		
		val =0
		query = "select Max(defectoEnPlanilla.iddefectoEnPlanilla) from defectoEnPlanilla"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	#insertar en planilla creada...
	def insertIntoPlanilla(self, campo, huerto, sector, cuartel, variedad, temporada, jefeCuadrilla, cuadrilla, defectos):
		
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		cuartel = cuartel.replace("-", " ")
		variedad = variedad.replace("-", " ")
		temporada = temporada.replace("-", " ")
		jefeCuadrilla = jefeCuadrilla.replace("-", " ")
		cuadrilla = cuadrilla.replace("-", " ")
		idPlanilla = self.getMaxPlanilla()+1
		nombrePlanilla = "Planilla "+str(idPlanilla+1)
		
		query = "insert into planilla (planilla.idplanilla, planilla.nombrePlanilla, planilla.campo, planilla.huerto, planilla.sector, planilla.cuartel, planilla.variedad, planilla.jefeCuadrilla, planilla.cuadrilla, planilla.temporada) values (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (int(idPlanilla), nombrePlanilla, campo, huerto, sector, cuartel, variedad, jefeCuadrilla, cuadrilla, temporada)
		
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		#ahora comenzamos a agregar los defectos a la planilla
		idImportancia = self.getIDImportancia()
		ListaDefectos = defectos.split(":")
		
		print idPlanilla
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaDefectos:
			
			defecto = element.replace("-", " ")
			idDefecto = self.getMaxDefectoID()+1
			self.Connect.initConnectionDB()
			query = "insert into defectoEnPlanilla (defectoEnPlanilla.iddefectoEnPlanilla, defectoEnPlanilla.nombreDefecto, defectoEnPlanilla.idplanilla) values (%d,'%s', %d)" % (int(idDefecto), defecto, int(idPlanilla))
			query2 = "insert into importanciaDefecto (importanciaDefecto.iddefectoEnPlanilla, importanciaDefecto.idimportancia) values (%d, %d)" % (int(idDefecto), int(idImportancia))
			try:
				self.CrudDataBase.insertToTable(query, self.Connect)
				self.CrudDataBase.insertToTable(query2, self.Connect)
			except:
				pass
		
			self.Connect.closeConnectionDB()
	
	#obtener los defectos y su importancia
	def getDefectoImportancia(self, idPlanilla):
		
		idPlanilla = int(idPlanilla)
		
		query = "select defectoEnPlanilla.nombreDefecto, importancia.valorImportancia from defectoEnPlanilla join importanciaDefecto on (defectoEnPlanilla.iddefectoEnPlanilla = importanciaDefecto.iddefectoEnPlanilla) join importancia on (importancia.idimportancia = importanciaDefecto.idimportancia) where defectoEnPlanilla.idplanilla = %d" % idPlanilla
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#mostrar el listado de importancias disponibles...
	def getListadoImportancias(self):
		
		query = "select importancia.valorImportancia from importancia"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	def getidDefectoPlanilla(self, defecto):
		
		query = "select defectoEnPlanilla.iddefectoEnPlanilla from defectoEnPlanilla where defectoEnPlanilla.nombreDefecto = '%s'" % defecto
		#print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener id de la importancia para el defecto...
	def getidImportancia(self, importancia):
		
		query = "select importancia.idimportancia from importancia where importancia.valorImportancia = '%s'" % importancia
		#print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#editar importancia de defecto en planilla
	def editImportanciaDefecto(self, defecto, oldImportancia, importancia):
		
		#defecto = defecto[:len(defecto)-1]
		defecto = defecto.replace("-", " ")
		importancia = importancia.replace("-", " ")
		#oldImportancia = oldImportancia[1:]
		oldImportancia = oldImportancia.replace("-", " ")
		
		#obtener id de defecto en planilla
		idDefectoPlanilla = self.getidDefectoPlanilla(defecto)
		idImportancia = self.getidImportancia(importancia)
		idOldImportancia = self.getidImportancia(oldImportancia)
		
		#editamos en tabla importanciaDefecto
		query = "update importanciaDefecto set importanciaDefecto.idimportancia = %d where importanciaDefecto.iddefectoEnPlanilla = %d AND importanciaDefecto.idimportancia = %d " % (int(idImportancia), int(idDefectoPlanilla), int (idOldImportancia))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener el id de la configuracion
	def getMaxIDConfiguracion(self):
		
		val =0
		query = "select Max(configuracion.idconfiguracion) from configuracion"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val

	#crear configuracion para la importancia de los defectos...
	def generateConfigurationImportanciaDefecto(self, planilla, mayor1, mayor2, mayor3, menor1, menor2, menor3):
		
		query = "select importancia.idimportancia, defectoEnPlanilla.iddefectoEnPlanilla, importancia.valorImportancia from defectoEnPlanilla join importanciaDefecto on (defectoEnPlanilla.iddefectoEnPlanilla = importanciaDefecto.iddefectoEnPlanilla) join importancia on (importancia.idimportancia = importanciaDefecto.idimportancia) where defectoEnPlanilla.idplanilla = %d" % int(planilla)
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		for element in List:
			print element
			#preguntamos por el valor de la importancia...
			if element[2] == "MAYORES":
				
				#creo una configuracion para la importancia mayor...
				#obtenemos el id de la configuracion...
				idConfiguracion = self.getMaxIDConfiguracion()+1
				query = "insert into configuracion (configuracion.idconfiguracion, configuracion.verde, configuracion.amarillo, configuracion.rojo, configuracion.iddefectoEnPlanilla, configuracion.idimportancia) values (%d, %d, %d, %d, %d, %d)" % (int(idConfiguracion), int(mayor1), int(mayor2), int(mayor3), int(element[1]), int(element[0]))
				self.Connect.initConnectionDB()
				self.CrudDataBase.insertToTable(query, self.Connect)
				self.Connect.closeConnectionDB()
			elif element[2] == "MENORES":
				idConfiguracion = self.getMaxIDConfiguracion()+1
				query = "insert into configuracion (configuracion.idconfiguracion, configuracion.verde, configuracion.amarillo, configuracion.rojo, configuracion.iddefectoEnPlanilla, configuracion.idimportancia) values (%d, %d, %d, %d, %d, %d)" % (int(idConfiguracion), int(menor1), int(menor2), int(menor3), int(element[1]), int(element[0]))
				self.Connect.initConnectionDB()
				self.CrudDataBase.insertToTable(query, self.Connect)
				self.Connect.closeConnectionDB()

	#obtener cantidad de planillas actuales en el sistema...
	def getNumberPlanillas(self):
	
		query = "select * from planilla"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
	
		print len(List)
	
	#obtener informacion de las planillas existentes en el sistema...
	def getPlanillas(self):
		
		query = "select planilla.idplanilla, planilla.nombrePlanilla from planilla"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
	
	#obtener informacion asociada a la planilla
	def getInformationPlanilla(self, idPlanilla):
		
		query = "select planilla.campo, planilla.huerto, planilla.sector, planilla.cuartel, planilla.variedad, planilla.jefeCuadrilla, planilla.cuadrilla, planilla.variedad, planilla.temporada from planilla where planilla.idplanilla = %d" % int(idPlanilla)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
	
	#eliminar una planilla dado su id...
	def removePlanilla(self, idPlanilla):
		
		query = "delete from planilla where planilla.idplanilla = %d" % int (idPlanilla)
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getNombreCampo()
	
	elif sys.argv[1] == "2":
		st.getNombreHuerto(sys.argv[2])#obtener informacion de los huertos a partir del nombre del campo
	
	elif sys.argv[1] == "3":#obtener los nombres de los sectores de un huerto en un campo
		st.getNombreSector(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "4":#obtener los nombres de los cuartel de un sector de un huerto en un campo
		st.getNombreCuartel(sys.argv[2], sys.argv[3], sys.argv[4]);
	
	elif sys.argv[1] == "5":#obtener los nombres de las variedades de los cuartel de un sector de un huerto en un campo
		st.getNombreVariedad(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]);
	
	elif sys.argv[1] == "6":
		st.getInformationJefeAndCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	
	elif sys.argv[1] == "7":
		st.getInformationJefe(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	
	elif sys.argv[1] == "8":
		st.getInformationTemporadas()
	
	elif sys.argv[1] == "9":
		st.getListDefectos(sys.argv[2])
	
	elif sys.argv[1] == "10":
		st.insertIntoPlanilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])
	
	elif sys.argv[1] == "11":
		st.getDefectoImportancia(sys.argv[2])
	
	elif sys.argv[1] == "12":
		st.getListadoImportancias()
	
	elif sys.argv[1] == "13":
		st.editImportanciaDefecto(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "14":
		st.generateConfigurationImportanciaDefecto(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
	
	elif sys.argv[1] == "15":
		st.getNumberPlanillas()
	
	elif sys.argv[1] == "16":
		st.getPlanillas()
	
	elif sys.argv[1] == "17":
		st.getInformationPlanilla(sys.argv[2])
	
	elif sys.argv[1] == "18":
		st.removePlanilla(sys.argv[2])
		
	return 0

if __name__ == '__main__':
	main()

