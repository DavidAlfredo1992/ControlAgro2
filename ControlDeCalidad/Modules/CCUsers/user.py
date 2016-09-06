#class with the responsability of generate the sistem of login and manipulate users
from Modules.CCConnectDB import ConnectDataBase
from Modules.CCCRUD import CrudDataBase

import sys
import json

class User(object):
	
	def __init__(self, nameUser, passUser):
	
		self.nameUser = nameUser
		self.nameUser = self.nameUser.replace("-", " ")
		self.passUser = passUser

		self.Connect = ConnectDataBase.ConnectDataBase()#instance to object ConnectDataBase
		self.CrudDataBase = CrudDataBase.HandlerQuery()#instance to object CrudDataBase for handeler data base


	#method for check user in data base, return kind of user if is correctly and -1 if not exist in db
	def checkUserInDB(self):

		response = 0#value for return
	
		#search user in data base
		query = "SELECT usuarioSistema.tipoUsuario from usuarioSistema where usuarioSistema.nombreUsuario = \"%s\" AND usuarioSistema.password = \"%s\"" % (str(self.nameUser), str(self.passUser)) 

		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)

		if len(List) == 0:
			response = -1
		else:
			
			response = int(List[0][0])

		return response

	#method for get all information of user in data base
	def getInformationUsers(self):

		self.Connect.initConnectionDB()

		query = "select usuarioSistema.nombreUsuario, usuarioSistema.correoUsuario, tipoUsuario.nombreTipo from usuarioSistema inner join tipoUsuario on (usuarioSistema.tipoUsuario = tipoUsuario.idtipoUsuario)"
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		ListDictionary = {}

		
		self.Connect.closeConnectionDB()

def main ():

	user = User(sys.argv[1], sys.argv[2])
	
	if (int(sys.argv[3]) == 1):#check user in data base
		print user.checkUserInDB()
	
	if (int(sys.argv[3]) == 2):#get all information in data base of user
		user.getInformationUsers()
	
	
	return 0

if __name__ == '__main__':
	main()
