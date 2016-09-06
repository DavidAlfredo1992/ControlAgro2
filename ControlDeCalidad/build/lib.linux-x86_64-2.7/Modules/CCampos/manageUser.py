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
		
		query = "select usuarioSistema.nombreUsuario, usuarioSistema.correoUsuario, tipoUsuario.nombreTipo from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario)"
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
		
	#obtener tipo de usuario
	def getTipoUser(self):
		
		query = "select nombreTipo from tipoUsuario"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el ultimo id del usuario
	def getMaxIDUser(self):
		
		query = "select MAX(usuarioSistema.idusuarioSistema) from usuarioSistema"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#obtener id del tipo de usuario...
	def getIDTipoUser(self, kind):
		
		query = "select tipoUsuario.idtipoUsuario from tipoUsuario where tipoUsuario.nombreTipo = '%s'" % kind
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#insertar usuario en la base de datos...
	def insertUserSystem(self, user, mail, password, kindUser):
		
		val=1
		try:
			idUser = self.getMaxIDUser()+1
			idTipoUser = self.getIDTipoUser(kindUser)
			query = "insert into usuarioSistema (idusuarioSistema, nombreUsuario, correoUsuario, password, tipoUsuario) values (%d, '%s', '%s', '%s', %d)" % (int(idUser), str(user), str(mail), str(password), int(idTipoUser))
			
			self.Connect.initConnectionDB()
			self.CrudDataBase.insertToTable(query, self.Connect)
			self.Connect.closeConnectionDB()
		except:
			val=0
		print val
	
	#edit user of system...
	def editUserSystem(self, oldUser, oldMail, oldKindUser, newUser, newMail, newPassworod):
		
		#get id user for will be edit...
		query = "select usuarioSistema.idusuarioSistema from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario) where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.correoUsuario = \"%s\" AND tipoUsuario.nombreTipo = \"%s\"" % (str(oldUser), str(oldMail), str(oldKindUser))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserEdit = List[0][0]
		
		query = "update usuarioSistema set usuarioSistema.nombreUsuario = \"%s\", usuarioSistema.correoUsuario = \"%s\", usuarioSistema.password = \"%s\" where usuarioSistema.idusuarioSistema = %d" % (str(newUser), str(newMail), str(newPassworod), int(idUserEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteUserSystem(self, user, mail, kindUser):
		
		#get id user for will be edit...
		query = "select usuarioSistema.idusuarioSistema from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario) where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.correoUsuario = \"%s\" AND tipoUsuario.nombreTipo = \"%s\"" % (str(user), str(mail), str(kindUser))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserDelete = List[0][0]
		
		query = "delete from usuarioSistema where usuarioSistema.idusuarioSistema = %d" % int(idUserDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of user
		st.getInformationUser()
	
	elif sys.argv[1] == "2":#get tipos de usuarios de sistema
		st.getTipoUser()
	
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "4":
		st.editUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
	
	elif sys.argv[1] == "5":
		st.deleteUserSystem(sys.argv[2], sys.argv[3], sys.argv[4])
			
	return 0

if __name__ == '__main__':
	main()
