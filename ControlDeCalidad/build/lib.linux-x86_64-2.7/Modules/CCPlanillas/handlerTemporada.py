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
	def getInformationTemporada(self):
		
		
		query = "select temporada.nombreTemporada from temporada"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del jefe de campo
	def getMaxTemporada(self):
		
		val=0
		query = "select Max(temporada.idTemporada) from temporada"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
		
	#insertar jefe de campo en la base de datos...
	def insertTemporada(self, temporada):
		
		val=1
		#try:
			#insertamos el telefono
		idTemporada = self.getMaxTemporada()+1
		
		query = "insert into temporada (temporada.idtemporada, temporada.nombreTemporada) values (%d, '%s')" % (int(idTemporada), str(temporada))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editTemporada(self, oldTemporada, newTemporada):
		
		#get id user for will be edit...
		query = "select temporada.idtemporada from temporada where temporada.nombreTemporada =\"%s\"" % (str(oldTemporada))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idTemporadaEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update temporada set temporada.nombreTemporada = \"%s\" where temporada.idtemporada = %d" % (str(newTemporada), int(idTemporadaEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteTemporada(self, temporada):
		
		#get id user for will be edit...
		query = "select temporada.idtemporada from temporada where temporada.nombreTemporada =\"%s\"" % (str(temporada))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idTemporadaDelete = List[0][0]
		
		query = "delete from temporada where temporada.idtemporada = %d" % int(idTemporadaDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationTemporada()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertTemporada(sys.argv[2])
	
	elif sys.argv[1] == "4":
		st.editTemporada(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteTemporada(sys.argv[2])
			
	return 0

if __name__ == '__main__':
	main()

