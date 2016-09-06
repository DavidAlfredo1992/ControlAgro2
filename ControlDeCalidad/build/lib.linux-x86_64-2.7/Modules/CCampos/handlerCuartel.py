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
	def getIDSector(self, nombreSector):
		
		query = "select  sector.idsector from sector where sector.nombreSector = '%s'" % (str(nombreSector))
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
		
		val=1
		#try:
			#insertamos el telefono
		idSector = self.getIDSector(nombreSector)
		idCuartel = self.getMaxCuartel()+1
		
		query = "insert into cuartel (cuartel.idcuartel, cuartel.nombreCuartel, cuartel.sectorPertence) values (%d, '%s', %d)" % (int(idCuartel), str(nombreCuartel), int(idSector))
		print query
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#trabajamos con las variedades...
		ListaVariedades = variedades.split("-")
		
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
		
		#get id user for will be edit...
		query = "select cuartel.idcuartel, sector.idsector from cuartel join sector on (cuartel.sectorPertence = sector.idsector) join huerto on (sector.huertoPertence = huerto.idhuerto) join campo on (campo.idcampo = huerto.campoPertenece) where cuartel.nombreCuartel = '%s' AND sector.nombreSector = '%s' AND huerto.nombreHuerto ='%s' AND campo.nombreCampo = '%s'" % (str(oldCuartel), str(oldSector), str(oldHuerto), str(oldCampo))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuartelEdit = List[0][0]
		idSectorEdit = List[0][1]
		
		self.Connect.initConnectionDB()
		query = "update cuartel set cuartel.nombreCuartel = \"%s\", cuartel.sectorPertence = %d where cuartel.idcuartel = %d" % (str(newCuartel), int(idSectorEdit), int (idCuartelEdit))
		print query
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#se eliminan todas las variedades que posee dicho cuartel...
		query = "delete from variedadCuartel where variedadCuartel.idCuartel = %d" % int(idCuartelEdit)
		self.CrudDataBase.insertToTable(query, self.Connect)
	
		#se insertan las nuevas variedades seleccionadas...
		ListaVariedades = variedades.split("-")
		
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaVariedades:
			
			idVariedad = self.getIDVariedad(element)
			self.Connect.initConnectionDB()
			query = "insert into variedadCuartel (variedadCuartel.idcuartel, variedadCuartel.idvariedad) values (%d, %d)" % (int(idCuartelEdit), int(idVariedad))
			self.CrudDataBase.insertToTable(query, self.Connect)
			
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteCuartel(self, cuartel, sector, huerto, campo):
				
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
		
		query = "select sector.nombreSector from sector"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()

	#obtener el nombre de los huertos existentes
	def getNombreHuerto(self):
		
		query = "select huerto.nombreHuerto from huerto"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
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
	
	return 0

if __name__ == '__main__':
	main()

