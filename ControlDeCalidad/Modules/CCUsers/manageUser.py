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

	#obtener id del campo...
	def getIDCampo(self, nombreCampo):
		
		query = "select campo.idcampo from campo where campo.nombreCampo = '%s'" % nombreCampo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]

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
		
		val=0
		query = "select MAX(usuarioSistema.idusuarioSistema) from usuarioSistema"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener el ultimo id del usuario
	def getMaxIDDigitador(self):
		
		val=0
		query = "select MAX(digitador.iddigitador) from digitador"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
		
	#obtener id del tipo de usuario...
	def getIDTipoUser(self, kind):
		
		query = "select tipoUsuario.idtipoUsuario from tipoUsuario where tipoUsuario.nombreTipo = '%s'" % kind
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#insertar usuario en la base de datos...
	def insertUserSystem(self, user, mail, password, kindUser):
		
		#reemplazar el - por un espacio
		user = user.replace("-", " ")
		val=1
		#try:
		idUser = self.getMaxIDUser()+1
		idTipoUser = self.getIDTipoUser(kindUser)
		query = "insert into usuarioSistema (idusuarioSistema, nombreUsuario, correoUsuario, password, tipoUsuario) values (%d, '%s', '%s', '%s', %d)" % (int(idUser), str(user), str(mail), str(password), int(idTipoUser))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#preguntamos si es digitador...
		if idTipoUser == 2:
			self.insertDigitador(user)
		#except:
		#val=0
		#print val
		print idUser
		
	#insertar un digitador...
	def insertDigitador(self, user):
		
		val=1
		try:
			idUser = self.getMaxIDDigitador()+1
			query = "insert into digitador (iddigitador, nombreDigitador) values (%d, '%s')" % (int(idUser), str(user))
			
			self.Connect.initConnectionDB()
			self.CrudDataBase.insertToTable(query, self.Connect)
			self.Connect.closeConnectionDB()
		except:
			val=0
		print val
		
	#edit user of system...
	def editUserSystem(self, oldUser, oldMail, oldKindUser, newUser, newMail, newPassworod):
		
		oldUser = oldUser[:len(oldUser)-1]
		oldUser = oldUser.replace("-", " ")
		newUser = newUser.replace("-", " ")
		
		#get id user for will be edit...
		query = "select usuarioSistema.idusuarioSistema from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario) where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.correoUsuario = \"%s\" AND tipoUsuario.nombreTipo = \"%s\"" % (str(oldUser), str(oldMail), str(oldKindUser))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserEdit = List[0][0]
		
		query = "update usuarioSistema set usuarioSistema.nombreUsuario = \"%s\", usuarioSistema.correoUsuario = \"%s\", usuarioSistema.password = \"%s\" where usuarioSistema.idusuarioSistema = %d" % (str(newUser), str(newMail), str(newPassworod), int(idUserEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		#preguntamos si es digitador...
		if str(oldKindUser) == "Digitador":
			self.editDigitador(oldUser, newUser)

	#edit digitador...
	def editDigitador(self, oldUser, newUser):
		
		#get id user for will be edit...
		query = "select digitador.iddigitador from digitador where digitador.nombreDigitador = \"%s\"" % str(oldUser)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserEdit = List[0][0]
		
		query = "update digitador set digitador.nombreDigitador = \"%s\" where digitador.iddigitador = %d" % (str(newUser), int(idUserEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
	#delete user of system...
	def deleteUserSystem(self, user, mail, kindUser):
		
		user = user[:len(user)-1]
		user = user.replace("-", " ")
		
		#get id user for will be edit...
		query = "select usuarioSistema.idusuarioSistema from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario) where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.correoUsuario = \"%s\" AND tipoUsuario.nombreTipo = \"%s\"" % (str(user), str(mail), str(kindUser))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserDelete = List[0][0]
		
		query = "delete from usuarioSistema where usuarioSistema.idusuarioSistema = %d" % int(idUserDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if str(kindUser) == "Digitador":
			self.deleteDigitador(user)
		
	#eliminar digitador del sistema
	def deleteDigitador(self, user):
		
		#get id user for will be edit...
		query = "select digitador.iddigitador from digitador where digitador.nombreDigitador = \"%s\"" % str(user)
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idUserDelete = List[0][0]
		
		query = "delete from digitador where digitador.iddigitador = %d" % int(idUserDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()	
	
	#obtener la informacion de un usuario dado su id...
	def getInfoUsuarioByID(self, idUser):
		
		query = "select usuarioSistema.nombreUsuario, usuarioSistema.correoUsuario, tipoUsuario.nombreTipo from usuarioSistema join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario) where usuarioSistema.idusuarioSistema = %d" % int(idUser)
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#insertar un telefono, retorna el id del telefono insertado...
	def insertPhone(self, numero, empresa):
		
		#obtener el id del ultimo telefono...
		idTelefono = self.getMaxIDTelefono()+1
		
		query = "insert into telefono (idtelefono, numeroTelefono, empresa) values (%d, %d, \"%s\")" % (int(idTelefono), int(numero), str(empresa))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		return idTelefono

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
	
	#completar informacion adicional en cliente e insertar en base de datos...
	def insertIntoCliente(self, idUsuario, campo, empresa, telefono):
		
		#obtener el campo al que pertence...
		campo = campo.replace("-", " ")
		idCampo = self.getIDCampo(campo)
		idTelefono = self.insertPhone(telefono, empresa)
		
		#hacer insersion en cliente...
		query = "insert into clienteCampo values (%d, %d, %d)" % (int(idUsuario), int(idCampo), int(idTelefono))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener el id del campo del cliente segun el nombre y el pass del usuario...
	def getIDCampoByUser(self, name, password):
		
		name = name.replace("-", " ")
		#obtenemos el id del usuario segun su informacion
		query = "SELECT usuarioSistema.idusuarioSistema from usuarioSistema where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.password = \"%s\"" % (str(name), str(password)) 
		#print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		idUser = List[0][0]
		
		#ahora obtener el id del campo segun el cliente...
		query = "select clienteCampo.campoPertenece from clienteCampo where clienteCampo.idClienteCampo= %d" % int (idUser)
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		print List[0][0]
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
	
	elif sys.argv[1] == "6":#obtener informacion por el id del usuario
		st.getInfoUsuarioByID(sys.argv[2])
	
	elif sys.argv[1] == "7":#insertar cliente
		st.insertIntoCliente(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "8":#obtener el id del campo al que pertence el sujeto...
		st.getIDCampoByUser(sys.argv[2], sys.argv[3])
	return 0

if __name__ == '__main__':
	main()
