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
	def getInformationUser(self):
		
		query = "select jefeCampo.nombreJefeCampo, campo.nombreCampo, telefono.numeroTelefono, telefono.empresa  from jefeCampo join campo on (jefeCampo.campoPertenece = campo.idcampo) join telefono on (jefeCampo.telefono = telefono.idtelefono)"
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
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
	
	#obtener el ultimo id del jefe de campo
	def getMaxJefeCampo(self):
		
		val=0
		query = "select Max(jefeCampo.idjefeCampo) from jefeCampo;"
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
	def insertJefeCampo(self, numero, empresa, nombreJefe, nombreCampo):
		
		val=1
		#try:
			#insertamos el telefono
		idTelefono = self.insertPhone(numero, empresa)
		idJefeCampo = self.getMaxJefeCampo()+1
		idCampo = self.getIDCampo(nombreCampo)
		query = "insert into jefeCampo (jefeCampo.idjefeCampo, jefeCampo.nombreJefeCampo, jefeCampo.telefono, jefeCampo.campoPertenece) values (%d, '%s', %d, %d)" % (int(idJefeCampo), str(nombreJefe), int(idTelefono), int(idCampo))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editUserSystem(self, oldjefeCampo, oldcampo, oldtelefono, oldempresa, jefeCampo, campo, telefono, empresa):
		
		#get id user for will be edit...
		query = "select jefeCampo.idjefeCampo from jefeCampo join campo on (campo.idcampo = jefeCampo.campoPertenece) join telefono on (telefono.idtelefono = jefeCampo.telefono) where jefeCampo.nombreJefeCampo =\"%s\" AND campo.nombreCampo = \"%s\" AND telefono.numeroTelefono = %d AND telefono.empresa = \"%s\"" % (str(oldjefeCampo), str(oldcampo), int(oldtelefono), str(oldempresa))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCampoEdit = List[0][0]
		
		#insertar nuevo telefono...
		idTelefono = self.insertPhone(telefono, empresa)
		idCampo = self.getIDCampo(campo)
		self.Connect.initConnectionDB()
		query = "update jefeCampo set jefeCampo.nombreJefeCampo = \"%s\", jefeCampo.campoPertenece = %d, jefeCampo.telefono = %d where jefeCampo.idjefeCampo = %d" % (str(jefeCampo), int(idCampo), int (idTelefono), int (idJefeCampoEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteUserSystem(self, jefeCampo, campo, telefono, empresa):
		
		#get id user for will be edit...
		query = "select jefeCampo.idjefeCampo from jefeCampo join campo on (campo.idcampo = jefeCampo.campoPertenece) join telefono on (telefono.idtelefono = jefeCampo.telefono) where jefeCampo.nombreJefeCampo =\"%s\" AND campo.nombreCampo = \"%s\" AND telefono.numeroTelefono = %d AND telefono.empresa = \"%s\"" % (str(jefeCampo), str(campo), int(telefono), str(empresa))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCampoDelete = List[0][0]
		
		query = "delete from jefeCampo where jefeCampo.idjefeCampo = %d" % int(idJefeCampoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of user
		st.getInformationUser()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()
	
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertJefeCampo(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "4":
		st.editUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
	
	elif sys.argv[1] == "5":
		st.deleteUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
			
	return 0

if __name__ == '__main__':
	main()

