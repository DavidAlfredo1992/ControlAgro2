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
	def getInformationVariedad(self):
		
		
		query = "select variedad.nombreVariedad from variedad"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxVariedad(self):
		
		val=0
		query = "select Max(variedad.idvariedad) from variedad"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
		
	#insertar jefe de campo en la base de datos...
	def insertVariedad(self, nameVariedad):
		
		nameVariedad = nameVariedad.replace("-", " ")
		
		val=1
		#try:
			#insertamos el telefono
		idVariedad = self.getMaxVariedad()+1
		
		query = "insert into variedad (variedad.idvariedad, variedad.nombreVariedad) values (%d, '%s')" % (int(idVariedad), str(nameVariedad))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editVariedad(self, oldVariedad, newVariedad):
		
		oldVariedad = oldVariedad.replace("-", " ")
		newVariedad = newVariedad.replace("-", " ")
		
		#get id user for will be edit...
		query = "select variedad.idvariedad from variedad where variedad.nombreVariedad =\"%s\"" % (str(oldVariedad))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idVariedadEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update variedad set variedad.nombreVariedad = \"%s\" where variedad.idvariedad = %d" % (str(newVariedad), int(idVariedadEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteVariedad(self, variedad):
		
		variedad = variedad.replace("-", " ")
		#get id user for will be edit...
		query = "select variedad.idvariedad from variedad where variedad.nombreVariedad =\"%s\"" % (str(variedad))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idVariedadDelete = List[0][0]
		
		query = "delete from variedad where variedad.idvariedad = %d" % int(idVariedadDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationVariedad()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertVariedad(sys.argv[2])
	
	elif sys.argv[1] == "4":
		st.editVariedad(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteVariedad(sys.argv[2])
			
	return 0

if __name__ == '__main__':
	main()

