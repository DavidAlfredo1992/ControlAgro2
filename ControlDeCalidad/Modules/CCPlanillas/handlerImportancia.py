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
	def getInformationImportancia(self):
		
		
		query = "select importancia.valorImportancia from importancia"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxImportancia(self):
		
		val=0
		query = "select Max(importancia.idimportancia) from importancia"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
		
	#insertar jefe de campo en la base de datos...
	def insertImportancia(self, importancia):
		
		importancia = importancia.replace("-", " ")
		
		val=1
		#try:
			#insertamos el telefono
		idImportancia = self.getMaxImportancia()+1
		
		query = "insert into importancia (importancia.idimportancia, importancia.valorImportancia) values (%d, '%s')" % (int(idImportancia), str(importancia))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editImportancia(self, oldImportancia, newImportancia):
		
		oldImportancia = oldImportancia.replace("-", " ")
		newImportancia = newImportancia.replace("-", " ")
		
		#get id user for will be edit...
		query = "select importancia.idimportancia from importancia where importancia.valorImportancia =\"%s\"" % (str(oldImportancia))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idImportanciaEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update importancia set importancia.valorImportancia = \"%s\" where importancia.idimportancia = %d" % (str(newImportancia), int(idImportanciaEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteImportancia(self, importancia):
		
		importancia = importancia.replace("-", " ")
		
		#get id user for will be edit...
		query = "select importancia.idimportancia from importancia where importancia.valorImportancia =\"%s\"" % (str(importancia))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idImportanciaDelete = List[0][0]
		
		query = "delete from importancia where importancia.idimportancia = %d" % int(idImportanciaDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationImportancia()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertImportancia(sys.argv[2])
	
	elif sys.argv[1] == "4":
		st.editImportancia(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteImportancia(sys.argv[2])
			
	return 0

if __name__ == '__main__':
	main()

