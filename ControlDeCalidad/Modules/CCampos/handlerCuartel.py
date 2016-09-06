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
	
	#obtener el nombre de las variedades
	def getNombreVariedad(self):
		
		query = "select variedad.nombreVariedad from variedad"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
		
	#obtener los nombres de las variedades que existen en un cuartel dado el nombre del cuartel...	
	def getNombreVariedadByCuartel(self, cuartel):
		
		cuartel = cuartel.replace("-", " ")
		query = "select variedad.nombreVariedad from variedad join variedadCuartel on (variedad.idvariedad = variedadCuartel.idvariedad) join cuartel on (cuartel.idcuartel = variedadCuartel.idcuartel) where cuartel.nombreCuartel = '%s'" % cuartel
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
		
	#obtener informacion de los usuarios del sistema
	def getInformationCuartel(self):
		
		
		query = "select cuartel.nombreCuartel, sector.nombreSector, huerto.nombreHuerto, campo.nombreCampo, COUNT(variedadCuartel.idcuartel) from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (sector.huertoPertence = huerto.idhuerto) join campo on (campo.idcampo = huerto.campoPertenece) join variedadCuartel on (cuartel.idcuartel = variedadCuartel.idcuartel) group by (variedadCuartel.idcuartel)"
		
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
	def getMaxCuartel(self):
		
		val=0
		query = "select Max(cuartel.idcuartel) from cuartel"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener id del campo...
	def getIDCampo(self, nombreCampo):
		
		query = "select campo.idcampo from campo where campo.nombreCampo = '%s'" % nombreCampo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener id del huerto...
	def getIDHuerto(self, nombreHuerto, nombreCampo):
		
		query = "select huerto.idhuerto from huerto join campo on (huerto.campoPertenece = campo.idcampo) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s'" % (nombreHuerto, nombreCampo)
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener el id del sector...
	def getIDSector(self, nombreSector, nombreHuerto, nombreCampo):
		
		query = "select sector.idsector from sector join huerto on (huerto.idhuerto = sector.huertoPertence) join campo on (campo.idcampo = huerto.campoPertenece) where sector.nombreSector = '%s' AND huerto.nombreHuerto = '%s' AND campo.nombreCampo = '%s'" % (str(nombreSector), str(nombreHuerto), str(nombreCampo))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener el id de la variedad...
	def getIDVariedad(self, variedad):
		
		query = "select variedad.idvariedad from variedad where variedad.nombreVariedad = '%s'" % variedad
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#insertar jefe de campo en la base de datos...
	def insertCuartel(self, nombreCuartel, nombreSector, variedades):
		
		nombreCuartel = nombreCuartel.replace("-", " ")
		variedades = variedades.replace("-", " ")
		nombreSector = nombreSector.replace("-", " ")
		nombres = nombreSector.split("/")
		
		val=1
		#try:
			#insertamos el telefono
		idSector = self.getIDSector(nombres[0], nombres[1], nombres[2])
		idCuartel = self.getMaxCuartel()+1
		
		query = "insert into cuartel (cuartel.idcuartel, cuartel.nombreCuartel, cuartel.sectorPertence) values (%d, '%s', %d)" % (int(idCuartel), str(nombreCuartel), int(idSector))
		print query
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#trabajamos con las variedades...
		ListaVariedades = variedades.split(":")
		
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaVariedades:
			
			idVariedad = self.getIDVariedad(element)
			self.Connect.initConnectionDB()
			query = "insert into variedadCuartel (variedadCuartel.idcuartel, variedadCuartel.idvariedad) values (%d, %d)" % (int(idCuartel), int(idVariedad))
			self.CrudDataBase.insertToTable(query, self.Connect)
		
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editCuartel(self, oldCuartel, oldSector, oldHuerto, oldCampo, newCuartel, newSector, variedades):
		
		oldCuartel = oldCuartel[:len(oldCuartel)-1]
		oldCuartel = oldCuartel.replace("-", " ")
		oldSector = oldSector[1:len(oldSector)-1]
		oldSector = oldSector.replace("-", " ")
		oldHuerto = oldHuerto[1:len(oldHuerto)-1]
		oldHuerto = oldHuerto.replace("-", " ")
		oldCampo = oldCampo[1:len(oldCampo)-1]
		oldCampo = oldCampo.replace("-", " ")
		
		newCuartel = newCuartel.replace("-", " ")
		variedades = variedades.replace("-", " ")
		newSector = newSector.replace("-", " ")
		nombres = newSector.split("/")
		
		#get id user for will be edit...
		query = "select cuartel.idcuartel from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (sector.huertoPertence = huerto.idhuerto) join campo on (campo.idcampo = huerto.campoPertenece) where cuartel.nombreCuartel = '%s' AND sector.nombreSector = '%s' AND huerto.nombreHuerto ='%s' AND campo.nombreCampo = '%s'" % (str(oldCuartel), str(oldSector), str(oldHuerto), str(oldCampo))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuartelEdit = List[0][0]
		idSectorEdit = self.getIDSector(nombres[0], nombres[1], nombres[2])
		
		self.Connect.initConnectionDB()
		query = "update cuartel set cuartel.nombreCuartel = \"%s\", cuartel.sectorPertence = %d where cuartel.idcuartel = %d" % (str(newCuartel), int(idSectorEdit), int (idCuartelEdit))
		print query
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#se eliminan todas las variedades que posee dicho cuartel...
		query = "delete from variedadCuartel where variedadCuartel.idCuartel = %d" % int(idCuartelEdit)
		self.CrudDataBase.insertToTable(query, self.Connect)
	
		#se insertan las nuevas variedades seleccionadas...
		ListaVariedades = variedades.split(":")
		
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaVariedades:
			
			idVariedad = self.getIDVariedad(element)
			self.Connect.initConnectionDB()
			query = "insert into variedadCuartel (variedadCuartel.idcuartel, variedadCuartel.idvariedad) values (%d, %d)" % (int(idCuartelEdit), int(idVariedad))
			self.CrudDataBase.insertToTable(query, self.Connect)
			
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteCuartel(self, cuartel, sector, huerto, campo):
		
		cuartel = cuartel[:len(cuartel)-1]
		cuartel = cuartel.replace("-", " ")
		sector = sector[1:len(sector)-1]
		sector = sector.replace("-", " ")
		huerto = huerto[1:len(huerto)-1]
		huerto = huerto.replace("-", " ")
		campo = campo[1:len(campo)-1]
		campo = campo.replace("-", " ")
		
		#get id user for will be edit...
		query = "select cuartel.idcuartel from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (sector.huertoPertence = huerto.idhuerto) join campo on (campo.idcampo = huerto.campoPertenece) where cuartel.nombreCuartel = '%s' AND sector.nombreSector = '%s' AND huerto.nombreHuerto ='%s' AND campo.nombreCampo = '%s'" % (str(cuartel), str(sector), str(huerto), str(campo))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuartelDelete = List[0][0]
		
		query = "delete from cuartel where cuartel.idcuartel = %d" % int(idCuartelDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
	
		self.Connect.closeConnectionDB()
	
	#obtener el nombre de los campos existentes
	def getNombreCampo(self):
		
		query = "select campo.nombreCampo from campo"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
		
	#obtener el nombre de los sectores existentes
	def getNombreSector(self):
		
		query = "select sector.nombreSector, huerto.nombreHuerto, campo.nombreCampo  from sector join huerto on (huerto.idhuerto = sector.huertoPertence) join campo on (campo.idcampo = huerto.campoPertenece)"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print "%s/%s/%s" % (element[0], element[1], element[2])
		
		self.Connect.closeConnectionDB()

	#obtener el nombre de los huertos existentes
	def getNombreHuerto(self):
		
		query = "select huerto.nombreHuerto from huerto"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el id del cuartel dado su nombre
	def getIDCuartel(self, cuartel):
		
		query = "select cuartel.idcuartel from cuartel where cuartel.nombreCuartel = '%s'" % cuartel
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		return List[0][0]
		
	#agregar variedad al cuartel...
	def addVariedadCuartel(self, cuartel, variedades):
		
		cuartel = cuartel.replace("-", " ")
		idcuartel = self.getIDCuartel(cuartel)
		
		variedades = variedades.replace("-", " ")
		
		#trabajamos con las variedades...
		ListaVariedades = variedades.split(":")
		
		#removemos todas las variedades que posee el cuartel...
		#query = "delete from variedadCuartel where variedadCuartel.idcuartel = %d" % int(idcuartel)
		#self.Connect.initConnectionDB()
		#self.CrudDataBase.insertToTable(query, self.Connect)
		#self.Connect.closeConnectionDB()
		
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaVariedades:
			
			try:
				idVariedad = self.getIDVariedad(element)
				self.Connect.initConnectionDB()
				query = "insert into variedadCuartel (variedadCuartel.idcuartel, variedadCuartel.idvariedad) values (%d, %d)" % (int(idcuartel), int(idVariedad))
				self.CrudDataBase.insertToTable(query, self.Connect)
			except:
				pass
		self.Connect.closeConnectionDB()
	
	#eliminar una variedad a cuartel...
	def removeVariedadCuartel(self, cuartel, variedad):
		
		cuartel = cuartel.replace("-", " ")
		idcuartel = self.getIDCuartel(cuartel)
		
		variedad= variedad.replace("-", " ")
		idVariedad = self.getIDVariedad(variedad)
		
		query = "delete from variedadCuartel where variedadCuartel.idvariedad = %d AND variedadCuartel.idcuartel = %d" % (int(idVariedad), int(idcuartel))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of sector
		st.getInformationCuartel()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()

	elif sys.argv[1] == "3":#get nombre de los huertos existentes en el sistema
		st.getNombreHuerto()

	elif sys.argv[1] == "4":#get nombre de los sectores existentes en el sistema
		st.getNombreSector()

	elif sys.argv[1] == "5":#insert usuario en base de datos
		st.insertCuartel(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "6":#editar un cuartel
		st.editCuartel(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
	
	elif sys.argv[1] == "7":#eliminar un sector
		st.deleteCuartel(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "8":
		st.getNombreVariedad()#obtener el nombre de las variedades...
	
	elif sys.argv[1] == "9":
		st.getNombreVariedadByCuartel(sys.argv[2])#obtener el nombre de las variedades...
	
	elif sys.argv[1] == "10":
		st.addVariedadCuartel(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "11":
		st.removeVariedadCuartel(sys.argv[2], sys.argv[3])
	return 0

if __name__ == '__main__':
	main()

