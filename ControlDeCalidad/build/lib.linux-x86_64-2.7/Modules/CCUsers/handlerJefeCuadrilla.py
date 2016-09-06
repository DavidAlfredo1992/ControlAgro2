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
	def getInformationJefeCuadrilla(self):
		
		query = "select jefeCuadrilla.nombreJefeCuadrilla, telefono.numeroTelefono, telefono.empresa from jefeCuadrilla join telefono on (jefeCuadrilla.telefono = telefono.idtelefono)"
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		query = ""
		self.Connect.closeConnectionDB()
		
	#obtener el nombre de los campos existentes
	def getNombreCampo(self):
		
		query = "select campo.nombreCampo from campo"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el id del ultimo telefono ingresado
	def getMaxIDTelefono(self):
		
		val=0
		query = "select Max(telefono.idtelefono) from telefono"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#insertar un telefono, retorna el id del telefono insertado...
	def insertPhone(self, numero, empresa):
		
		#obtener el id del ultimo telefono...
		idTelefono = self.getMaxIDTelefono()+1
		
		query = "insert into telefono (idtelefono, numeroTelefono, empresa) values (%d, %d, \"%s\")" % (int(idTelefono), int(numero), str(empresa))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		return idTelefono
	
	#obtener el ultimo id del jefe de cuadrilla
	def getMaxJefeCuadrilla(self):
		
		val=0
		query = "select Max(jefeCuadrilla.idjefeCuadrilla) from jefeCuadrilla"
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
	def insertJefeCuadrilla(self, numero, empresa, nombreJefe):
		
		val=1
		#try:
			#insertamos el telefono
		idTelefono = self.insertPhone(numero, empresa)
		idJefeCuadrilla = self.getMaxJefeCuadrilla()+1
		query = "insert into jefeCuadrilla (jefeCuadrilla.idjefeCuadrilla, jefeCuadrilla.nombreJefeCuadrilla, jefeCuadrilla.telefono) values (%d, '%s', %d)" % (int(idJefeCuadrilla), str(nombreJefe), int(idTelefono))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editUserSystem(self, oldJefeCuadrilla, oldtelefono, oldempresa, jefeCuadrilla, telefono, empresa):
		
		#get id user for will be edit...
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla join telefono on (telefono.idtelefono = jefeCuadrilla.telefono) where jefeCuadrilla.nombreJefeCuadrilla =\"%s\" AND telefono.numeroTelefono = %d AND telefono.empresa = \"%s\"" % (str(oldJefeCuadrilla), int(oldtelefono), str(oldempresa))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCuadrillaEdit = List[0][0]
		
		#insertar nuevo telefono...
		idTelefono = self.insertPhone(telefono, empresa)
		self.Connect.initConnectionDB()
		query = "update jefeCuadrilla set jefeCuadrilla.nombreJefeCuadrilla = \"%s\", jefeCuadrilla.telefono = %d where jefeCuadrilla.idjefeCuadrilla = %d" % (str(jefeCuadrilla), int (idTelefono), int (idJefeCuadrillaEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteUserSystem(self, jefeCuadrilla, telefono, empresa):
		
		#get id user for will be edit...
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla join telefono on (telefono.idtelefono = jefeCuadrilla.telefono) where jefeCuadrilla.nombreJefeCuadrilla =\"%s\" AND telefono.numeroTelefono = %d AND telefono.empresa = \"%s\"" % (str(jefeCuadrilla), int(telefono), str(empresa))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCampoDelete = List[0][0]
		
		query = "delete from jefeCuadrilla where jefeCuadrilla.idjefeCuadrilla = %d" % int(idJefeCampoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of user
		st.getInformationJefeCuadrilla()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()
	
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertJefeCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "4":
		st.editUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
	
	elif sys.argv[1] == "5":
		st.deleteUserSystem(sys.argv[2], sys.argv[3], sys.argv[4])
			
	return 0

if __name__ == '__main__':
	main()


