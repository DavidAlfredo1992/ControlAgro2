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

	#obtener informacion de los defectos existentes...
	def getNombreDefecto(self):
		
		
		query = "select defecto.nombreDefecto from defecto"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener listado de defectos asociados a un campo...
	def getNombreDefectoCampo(self, nombreCampo):
		
		nombreCampo = nombreCampo.replace("-", " ")
		
		query = "select defecto.nombreDefecto from campo join defectoCampo on (campo.idcampo = defectoCampo.idcampo) join defecto on (defecto.iddefecto = defectoCampo.iddefecto) where campo.nombreCampo = '%s'" % str(nombreCampo)
		#print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
		
	#obtener informacion de los usuarios del sistema
	def getInformationCampo(self):
		
		
		query = "select campo.nombreCampo, COUNT(campo.idcampo) from campo join defectoCampo on (campo.idcampo = defectoCampo.idcampo) group by (campo.idcampo)"
		
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
	def getMaxCampo(self):
		
		val=0
		query = "select Max(campo.idcampo) from campo;"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener el id del defecto...
	def getIDDefecto(self, defecto):
		
		query = "select defecto.iddefecto from defecto where defecto.nombreDefecto = '%s'" % defecto
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#obtener id del campo...
	def getIDCampo(self, nombreCampo):
		
		query = "select campo.idcampo from campo where campo.nombreCampo = '%s'" % nombreCampo
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
		
	#insertar jefe de campo en la base de datos...
	def insertCampo(self, nombreCampo, defectos):
		
		nombreCampo = nombreCampo.replace("-", " ")
		val=1
		
		ListaDefectos = defectos.split(":")
		#try:
			#insertamos el telefono
		idCampo = self.getMaxCampo()+1
		
		query = "insert into campo (campo.idcampo, campo.nombreCampo) values (%d, '%s')" % (int(idCampo), str(nombreCampo))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaDefectos:
			
			defecto = element.replace("-", " ")
			idDefecto = self.getIDDefecto(defecto)
			self.Connect.initConnectionDB()
			query = "insert into defectoCampo (defectoCampo.iddefecto, defectoCampo.idcampo) values (%d, %d)" % (int(idDefecto), int(idCampo))
			self.CrudDataBase.insertToTable(query, self.Connect)
			
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#asociar defectos en campo...
	def insertDefectosToCampo(self, nombreCampo, defectos):
		
		nombreCampo = nombreCampo.replace("-", " ")
		#obtener id del campo...
		idCampo = self.getIDCampo(nombreCampo)
		
		ListaDefectos = defectos.split(":")
			
		#por cada elemento en la lista obtenemos su id e insertamos en la tabla variedadCuartel...
		for element in ListaDefectos:
			
			defecto = element.replace("-", " ")
			idDefecto = self.getIDDefecto(defecto)
			self.Connect.initConnectionDB()
			query = "insert into defectoCampo (defectoCampo.iddefecto, defectoCampo.idcampo) values (%d, %d)" % (int(idDefecto), int(idCampo))
			try:
				self.CrudDataBase.insertToTable(query, self.Connect)
			except:
				pass
		
			self.Connect.closeConnectionDB()
	#edit user of system...
	def editCampo(self, oldCampo, newCampo):
		
		oldCampo = oldCampo[:len(oldCampo)]
		oldCampo = oldCampo.replace("-", " ")
		
		newCampo = newCampo.replace("-", " ")
		
		#get id user for will be edit...
		query = "select campo.idcampo from campo where campo.nombreCampo =\"%s\"" % (str(oldCampo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCampoEdit = List[0][0]
		
		self.Connect.initConnectionDB()
		query = "update campo set campo.nombreCampo = \"%s\" where campo.idcampo = %d" % (str(newCampo), int(idCampoEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteCampo(self, campo):
		
		campo = campo[:len(campo)]
		campo = campo.replace("-", " ")
		
		#get id user for will be edit...
		query = "select campo.idcampo from campo where campo.nombreCampo =\"%s\"" % (str(campo))
		
		print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idCampoDelete = List[0][0]
		
		query = "delete from campo where campo.idcampo = %d" % int(idCampoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#eliminar defecto asociado al campo...
	def removeDefectoCampo(self, campo, defecto):
		
		campo = campo[:len(campo)-1]
		campo = campo.replace("-", " ")
		defecto = defecto.replace("-", " ")
		
		idCampo = self.getIDCampo(campo)
		idDefecto = self.getIDDefecto(defecto)
		
		query = "delete from defectoCampo where defectoCampo.idcampo = %d AND defectoCampo.iddefecto = %d" % (int(idCampo), int(idDefecto))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getInformationCampo()
		
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertCampo(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "4":
		st.editCampo(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "5":
		st.deleteCampo(sys.argv[2])
		
	elif sys.argv[1] == "6":#obtener los nombres de los defectos...
		st.getNombreDefecto()
	
	elif sys.argv[1] == "7":#obtener los nombres de los defectos dado un campo
		st.getNombreDefectoCampo(sys.argv[2])
	
	elif sys.argv[1] == "8":#insertar defectos en campo
		st.insertDefectosToCampo(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "9":#eliminamos defectos asociados al campo
		st.removeDefectoCampo(sys.argv[2], sys.argv[3])
	return 0

if __name__ == '__main__':
	main()

