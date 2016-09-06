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

	#obtener informacion de los usuarios del sistema
	def getInformationSector(self):
		
		
		query = "select sector.nombreSector, huerto.nombreHuerto, campo.nombreCampo from sector join huerto on (sector.huertoPertence = huerto.idhuerto) join campo on (huerto.campoPertenece = campo.idcampo)"
		
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
	def getMaxSector(self):
		
		val=0
		query = "select Max(sector.idsector) from sector;"
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
		
	#insertar jefe de campo en la base de datos...
	def insertSector(self, nombreSector, nombreHuerto, nombreCampo):
		
		val=1
		#try:
			#insertamos el telefono
		idSector = self.getMaxSector()+1
		idHuerto = self.getIDHuerto(nombreHuerto, nombreCampo)
				
		query = "insert into sector (sector.idsector, sector.nombreSector, sector.huertoPertence) values (%d, '%s', %d)" % (int(idSector), str(nombreSector), int(idHuerto))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editSector(self, oldSector, oldHuerto, oldCampo, newSector, newHuerto, newCampo):
		
		#obtener huerto al que pertenece...
		idHuerto = self.getIDHuerto(oldCampo, oldHuerto)
		
		#get id user for will be edit...
		query = "select sector.idsector from sector where sector.nombreSector =\"%s\" AND sector.huertoPertence = %d" % (str(oldSector), int(idHuerto))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idSectorEdit = List[0][0]
		
		idHuertoNuevo = self.getIDHuerto(newCampo, newHuerto)
		
		self.Connect.initConnectionDB()
		query = "update sector set sector.nombreSector = \"%s\", sector.huertoPertence = %d where sector.idsector = %d" % (str(newSector), int(idHuertoNuevo), int (idSectorEdit))
		print query
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteSector(self, sector, huerto, campo):
		
		#obtener campo al que pertenece...
		idHuerto = self.getIDHuerto(campo, huerto)
		
		#get id user for will be edit...
		query = "select sector.idsector from sector where sector.nombreSector =\"%s\" AND sector.huertoPertence = %d" % (str(sector), int(idHuerto))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idSectorDelete = List[0][0]
		
		query = "delete from sector where sector.idsector = %d" % int(idSectorDelete)
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
		st.getInformationSector()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()

	elif sys.argv[1] == "3":#get nombre de los campos existentes en el sistema
		st.getNombreHuerto()

	elif sys.argv[1] == "4":#insert usuario en base de datos
		st.insertSector(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "5":
		st.editSector(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
	
	elif sys.argv[1] == "6":
		st.deleteSector(sys.argv[2], sys.argv[3], sys.argv[4])
			
	return 0

if __name__ == '__main__':
	main()

