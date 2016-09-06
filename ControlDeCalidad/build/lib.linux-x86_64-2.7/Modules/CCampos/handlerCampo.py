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
	def getInformationCampo(self):
		
		
		query = "select campo.nombreCampo from campo"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxCampo(self):
		
		val=0
		query = "select Max(campo.idcampo) from campo;"
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
	def insertCampo(self, nombreCampo):
		
		val=1
		#try:
			#insertamos el telefono
		idCampo = self.getMaxCampo()+1
		
		query = "insert into campo (campo.idcampo, campo.nombreCampo) values (%d, '%s')" % (int(idCampo), str(nombreCampo))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editCampo(self, oldCampo, newCampo):
		
		#get id user for will be edit...
		query = "select campo.idcampo from campo where campo.nombreCampo =\"%s\"" % (str(oldCampo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCampoEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update campo set campo.nombreCampo = \"%s\" where campo.idcampo = %d" % (str(newCampo), int(idCampoEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteCampo(self, campo):
		
		#get id user for will be edit...
		query = "select campo.idcampo from campo where campo.nombreCampo =\"%s\"" % (str(campo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCampoDelete = List[0][0]
		
		query = "delete from campo where campo.idcampo = %d" % int(idCampoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationCampo()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertCampo(sys.argv[2])
	
	elif sys.argv[1] == "4":
		st.editCampo(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteCampo(sys.argv[2])
			
	return 0

if __name__ == '__main__':
	main()

