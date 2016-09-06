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
	def getInformationHuerto(self):
		
		
		query = "select huerto.nombreHuerto, campo.nombreCampo from huerto join campo on (huerto.campoPertenece = campo.idcampo)"
		
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
	def getMaxHuerto(self):
		
		val=0
		query = "select Max(huerto.idhuerto) from huerto;"
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
		
	#insertar jefe de campo en la base de datos...
	def insertHuerto(self, nombreHuerto, nombreCampo):
		
		val=1
		#try:
			#insertamos el telefono
		idHuerto = self.getMaxHuerto()+1
		idCampo = self.getIDCampo(nombreCampo)
		
		query = "insert into huerto (huerto.idhuerto, huerto.nombreHuerto, huerto.campoPertenece) values (%d, '%s', %d)" % (int(idHuerto), str(nombreHuerto), int(idCampo))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editHuerto(self, oldHuerto, oldCampo, newHuerto, newCampo):
		
		#obtener campo al que pertenece...
		idCampo = self.getIDCampo(oldCampo)
		
		#get id user for will be edit...
		query = "select huerto.idhuerto from huerto where huerto.nombreHuerto =\"%s\" AND huerto.campoPertenece = %d" % (str(oldHuerto), int(idCampo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idHuertoEdit = List[0][0]
		
		idCampoNuevo = self.getIDCampo(newCampo)
		
		self.Connect.initConnectionDB()
		query = "update huerto set huerto.nombreHuerto = \"%s\", huerto.campoPertenece = %d where huerto.idhuerto = %d" % (str(newHuerto), int(idCampoNuevo), int (idHuertoEdit))
		print query
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteHuerto(self, huerto, campo):
		
		#obtener campo al que pertenece...
		idCampo = self.getIDCampo(campo)
		
		#get id user for will be edit...
		query = "select huerto.idhuerto from huerto where huerto.nombreHuerto =\"%s\" AND huerto.campoPertenece = %d" % (str(huerto), int(idCampo))
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idHuertoDelete = List[0][0]
		
		query = "delete from huerto where huerto.idhuerto = %d" % int(idHuertoDelete)
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
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationHuerto()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()

	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertHuerto(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "4":
		st.editHuerto(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "5":
		st.deleteHuerto(sys.argv[2], sys.argv[3])
			
	return 0

if __name__ == '__main__':
	main()

