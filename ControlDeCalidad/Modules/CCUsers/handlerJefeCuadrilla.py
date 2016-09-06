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
		
		query = "select jefeCuadrilla.nombreJefeCuadrilla, telefono.numeroTelefono, jefeCuadrilla.correoJefeCuadrilla from jefeCuadrilla join telefono on (jefeCuadrilla.telefono = telefono.idtelefono)"
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
	
	#obtener el nombre de los campos existentes
	def getNombreHuerto(self):
		
		query = "select huerto.nombreHuerto from huerto"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el nombre de los campos existentes
	def getNombreSector(self):
		
		query = "select sector.nombreSector from sector"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()

	#obtener el nombre de los campos existentes
	def getNombreCuartel(self):
		
		query = "select cuartel.nombreCuartel from cuartel"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()

	#obtener el nombre de los campos existentes
	def getNombreVariedad(self):
		
		query = "select variedad.nombreVariedad from variedad"
		
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
	def insertJefeCuadrilla(self, numero, empresa, nombreJefe, correo):
		
		nombreJefe = nombreJefe.replace("-", " ")
		val=1
		#try:
			#insertamos el telefono
		idTelefono = self.insertPhone(numero, empresa)
		idJefeCuadrilla = self.getMaxJefeCuadrilla()+1
		query = "insert into jefeCuadrilla (jefeCuadrilla.idjefeCuadrilla, jefeCuadrilla.nombreJefeCuadrilla, jefeCuadrilla.correoJefeCuadrilla, jefeCuadrilla.telefono) values (%d, '%s', '%s', %d)" % (int(idJefeCuadrilla), str(nombreJefe), str (correo), int(idTelefono))
			
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
			
		#except:
		#	val=0
		#print val
	
	#edit user of system...
	def editUserSystem(self, oldJefeCuadrilla, oldtelefono, oldcorreo, jefeCuadrilla, telefono, empresa, correo):
		
		oldJefeCuadrilla = oldJefeCuadrilla[:len(oldJefeCuadrilla)-1]
		oldJefeCuadrilla = oldJefeCuadrilla.replace("-", " ")
		jefeCuadrilla = jefeCuadrilla.replace("-", " ")
		
		#get id user for will be edit...
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla join telefono on (telefono.idtelefono = jefeCuadrilla.telefono) where jefeCuadrilla.nombreJefeCuadrilla =\"%s\" AND telefono.numeroTelefono = %d AND jefeCuadrilla.correoJefeCuadrilla = \"%s\"" % (str(oldJefeCuadrilla), int(oldtelefono), str(oldcorreo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCuadrillaEdit = List[0][0]
		
		#insertar nuevo telefono...
		idTelefono = self.insertPhone(telefono, empresa)
		self.Connect.initConnectionDB()
		query = "update jefeCuadrilla set jefeCuadrilla.nombreJefeCuadrilla = \"%s\", jefeCuadrilla.correoJefeCuadrilla = \"%s\", jefeCuadrilla.telefono = %d where jefeCuadrilla.idjefeCuadrilla = %d" % (str(jefeCuadrilla), str(correo), int (idTelefono), int (idJefeCuadrillaEdit))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()

	#delete user of system...
	def deleteUserSystem(self, jefeCuadrilla, telefono, correo):
		
		jefeCuadrilla = jefeCuadrilla[:len(jefeCuadrilla)-1]
		jefeCuadrilla = jefeCuadrilla.replace("-", " ")
		
		#get id user for will be edit...
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla join telefono on (telefono.idtelefono = jefeCuadrilla.telefono) where jefeCuadrilla.nombreJefeCuadrilla =\"%s\" AND telefono.numeroTelefono = %d AND jefeCuadrilla.correoJefeCuadrilla = \"%s\"" % (str(jefeCuadrilla), int(telefono), str(correo))
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		idJefeCampoDelete = List[0][0]
		
		query = "delete from jefeCuadrilla where jefeCuadrilla.idjefeCuadrilla = %d" % int(idJefeCampoDelete)
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#ver las variedades que controla un jefe de cuadrilla en cuarteles...
	def getVariedadesOfJefeCuadrilla(self, nombre):
		
		nombre = nombre.replace("-", " ")
		
		query = "select campo.nombreCampo, huerto.nombreHuerto, sector.nombreSector, cuartel.nombreCuartel, variedad.nombreVariedad from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (sector.huertoPertence = huerto.idhuerto) join cuartel on (cuartel.sectorPertence = sector.idsector) join variedadCuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join variedad on (variedad.idvariedad = variedadCuartel.idvariedad) join jefeCuadrillaVariedadCuartel on (variedadCuartel.idvariedad = jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad AND jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel = cuartel.idcuartel) join jefeCuadrilla on (jefeCuadrilla.idjefeCuadrilla = jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla) where jefeCuadrilla.nombreJefeCuadrilla = '%s'" % nombre
		#print query
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#eliminar una variedad a un jefe de cuadrilla
	def removeVariedadJefeCuadrilla(self, jefe, campo, huerto, sector, cuartel, variedad):
		
		jefe = jefe.replace("-", " ")
		campo = campo[:len(campo)-1]
		campo = campo.replace("-", " ")
		huerto = huerto[1:len(huerto)-1]
		huerto = huerto.replace("-", " ")
		sector = sector[1:len(sector)-1]
		sector = sector.replace("-", " ")
		cuartel = cuartel[1:len(cuartel)-1]
		cuartel = cuartel.replace("-", " ")
		variedad = variedad[1:]
		variedad = variedad.replace("-", " ")
		
		query = "select jefeCuadrilla.idjefeCuadrilla, cuartel.idcuartel, variedad.idvariedad from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (sector.huertoPertence = huerto.idhuerto) join cuartel on (cuartel.sectorPertence = sector.idsector) join variedadCuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join variedad on (variedad.idvariedad = variedadCuartel.idvariedad) join jefeCuadrillaVariedadCuartel on (variedadCuartel.idvariedad = jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad AND jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel = cuartel.idcuartel) join jefeCuadrilla on (jefeCuadrilla.idjefeCuadrilla = jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla) where jefeCuadrilla.nombreJefeCuadrilla = '%s' AND campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s' AND cuartel.nombreCuartel = '%s' AND variedad.nombreVariedad = '%s'" % (jefe, campo, huerto, sector, cuartel, variedad)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		#remove...
		query = "delete from jefeCuadrillaVariedadCuartel where jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla = %d AND jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel = %d AND jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad = %d" % (int (List[0][0]), int (List[0][1]), int (List[0][2]))
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
	#insertar en variedad para jefe de cuadrilla
	def insertVariedadJefeCuadrilla(self, jefe, campo, huerto, sector, cuartel, variedad):
		
		jefe = jefe.replace("-", " ")
		campo = campo.replace("-", " ")
		huerto = huerto.replace("-", " ")
		sector = sector.replace("-", " ")
		cuartel = cuartel.replace("-", " ")
		variedad = variedad.replace("-", " ")	
		
		#obtenemos los ids de todas...
		query = "select cuartel.idcuartel, variedad.idvariedad from campo join huerto on (campo.idcampo = huerto.campoPertenece) join sector on (sector.huertoPertence = huerto.idhuerto) join cuartel on (cuartel.sectorPertence = sector.idsector) join variedadCuartel on (variedadCuartel.idcuartel = cuartel.idcuartel) join variedad on (variedad.idvariedad = variedadCuartel.idvariedad) where campo.nombreCampo = '%s' AND huerto.nombreHuerto = '%s' AND sector.nombreSector = '%s' AND cuartel.nombreCuartel = '%s' AND variedad.nombreVariedad = '%s'" % (campo, huerto, sector, cuartel, variedad)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		#obtenemos el id del jefe de cuadrilla
		query = "select jefeCuadrilla.idjefeCuadrilla from jefeCuadrilla where jefeCuadrilla.nombreJefeCuadrilla = '%s'" % jefe
		self.Connect.initConnectionDB()
		ListID = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		#hacemos la insercion...
		query = "insert into jefeCuadrillaVariedadCuartel (jefeCuadrillaVariedadCuartel.jefeCuadrilla_idjefeCuadrilla, jefeCuadrillaVariedadCuartel.variedadCuartel_idcuartel, jefeCuadrillaVariedadCuartel.variedadCuartel_idvariedad) values (%d, %d, %d)" % (int(ListID[0][0]), int (List[0][0]), int(List[0][1]))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of user
		st.getInformationJefeCuadrilla()
	
	elif sys.argv[1] == "2":#get nombre de los campos existentes en el sistema
		st.getNombreCampo()
	
	elif sys.argv[1] == "3":#insert usuario en base de datos
		st.insertJefeCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "4":
		st.editUserSystem(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
	
	elif sys.argv[1] == "5":
		st.deleteUserSystem(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "6":
		st.getVariedadesOfJefeCuadrilla(sys.argv[2])
	
	elif sys.argv[1] == "7":#get nombre de los campos existentes en el sistema
		st.getNombreHuerto()
	
	elif sys.argv[1] == "8":#get nombre de los campos existentes en el sistema
		st.getNombreSector()
	
	elif sys.argv[1] == "9":#get nombre de los campos existentes en el sistema
		st.getNombreCuartel()
	
	elif sys.argv[1] == "10":#get nombre de los campos existentes en el sistema
		st.getNombreVariedad()
	
	elif sys.argv[1] == "11":
		st.insertVariedadJefeCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
	
	elif sys.argv[1] == "12":
		st.removeVariedadJefeCuadrilla(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
	return 0
	
if __name__ == '__main__':
	main()


