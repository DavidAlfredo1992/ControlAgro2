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
	def getInformationDefecto(self):
		
		
		query = "select defecto.nombreDefecto from defecto"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxDefecto(self):
		
		val=0
		query = "select Max(defecto.iddefecto) from defecto"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()

		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val		
	#insertar jefe de campo en la base de datos...
	def insertDefecto(self, defecto):
		
		val=1
		#try:
			#insertamos el telefono
		idDefecto = self.getMaxDefecto()+1
		
		query = "insert into defecto (defecto.iddefecto, defecto.nombreDefecto) values (%d, '%s')" % (int(idDefecto), str(defecto))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editDefecto(self, oldDefecto, newDefecto):
		
		#get id user for will be edit...
		query = "select defecto.iddefecto from defecto where defecto.nombreDefecto =\"%s\"" % (str(oldDefecto))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idDefectoEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update defecto set defecto.nombreDefecto = \"%s\" where defecto.iddefecto = %d" % (str(newDefecto), int(idDefectoEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteDefecto(self, defecto):
		
		#get id user for will be edit...
		query = "select defecto.iddefecto from defecto where defecto.nombreDefecto =\"%s\"" % (str(defecto))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idDefectoDelete = List[0][0]
		
		query = "delete from defecto where defecto.iddefecto = %d" % int(idDefectoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationDefecto()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertDefecto(sys.argv[2])
	
	elif sys.argv[1] == "4":
		st.editDefecto(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteDefecto(sys.argv[2])
			
	return 0

if __name__ == '__main__':
	main()

