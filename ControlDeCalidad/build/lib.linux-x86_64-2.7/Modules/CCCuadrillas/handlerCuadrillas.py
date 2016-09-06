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
	def getNombreJefeCuadrilla(self):
		
		
		query = "select jefeCuadrilla.nombreJefeCuadrilla from jefeCuadrilla"
		
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
		
		#get id user for will be edit...
		query = "select cuadrilla.idCuadrilla from cuadrilla join jefeCuadrilla on (cuadrilla.supervisor = jefeCuadrilla.idjefeCuadrilla) where cuadrilla.nombreCuadrilla =\"%s\" AND jefeCuadrilla.nombreJefeCuadrilla = '%s'" % (str(cuadrilla), str(jefeCuadrilla))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCuadrillaDelete = List[0][0]
		
		query = "delete from cuadrilla where cuadrilla.idcuadrilla = %d" % int(idCuadrillaDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationCuadrilla()

	elif sys.argv[1] == "2":#obtener nombre de los jefes de cuadrilla
		st.getNombreJefeCuadrilla()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertCuadrilla(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "4":
		st.editCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "5":
		st.deleteCuadrilla(sys.argv[2], sys.argv[3])
			
	return 0

if __name__ == '__main__':
	main()

