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
	def getNombreDigitador(self):
		
		query = "select digitador.nombreDigitador from digitador"
		
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		
		for element in List:
			print element[0]
		
		self.Connect.closeConnectionDB()
	
	#obtener el id del digitador
	def getIDDigitador(self, digitador):
		
		query = "select digitador.iddigitador from digitador where digitador.nombreDigitador = '%s'" % digitador
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		return List[0][0]
	
	#obtener el ultimo id del jefe de campo
	def getMaxControl(self):
		
		val =0
		query = "select Max(controlCalidadEfectuado.controlCalidad) from controlCalidadEfectuado"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#obtener el ultimo id del defecto en el control
	def getMaxDefectoEvaluado(self):
		
		val =0
		query = "select Max(defectosEvaluados.iddefectos) from defectosEvaluados"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
		
	#obtener lista de defectos en la planilla
	def getListaDefectos(self, idPlanilla):
		
		query = "select defectoEnPlanilla.nombreDefecto from defectoEnPlanilla where defectoEnPlanilla.idplanilla = %d" % int(idPlanilla)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()

		return List
	
	#obtener defectos dado su control de calidad...
	def getDefectosByControl(self, idControl):
		
		query = "select defectosEvaluados.iddefectos, defectosEvaluados.nombreDefecto, defectosEvaluados.valorDefecto from defectosEvaluados where defectosEvaluados.controlCalidadPertenece = %d" % int(idControl)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	#insertar en tabla controlCalidadEfectuado
	def insertIntocontrolCalidadEfectuado(self, idPlanilla, digitador, fecha, muestra):
		
		digitador = digitador.replace("-", " ")
		
		#obtener el id del digitador
		idDigitador = self.getIDDigitador(digitador)
		
		#obtener el id del control
		idControl = self.getMaxControl()+1
		
		query = "insert into controlCalidadEfectuado (controlCalidad, digitador, fechaControl, tamanoMuestra) values (%d, %d, '%s', %d)" % (int (idControl), int(idDigitador), fecha, int(muestra))
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#insertar en tabla de union de control con planilla
		query = "insert into planillaDeControlDeCalidad (planillaDeControlDeCalidad.idplanilla, planillaDeControlDeCalidad.controlCalidad) values (%d, %d)" % (int(idPlanilla), int(idControl))
		self.CrudDataBase.insertToTable(query, self.Connect)
		
		#agregar los defectos que tiene asociados la planilla al control y asignarle valor 0...
		ListDefectos = self.getListaDefectos(idPlanilla)
		
		for element in ListDefectos:#por cada elemento hacemos la insercion en la tabla...
			
			#obtenemos el id maximo del defecto...
			idDefectoEvaluado = self.getMaxDefectoEvaluado()+1
			self.Connect.initConnectionDB()
			#hacemos la insercion
			query = "insert into defectosEvaluados (defectosEvaluados.iddefectos, defectosEvaluados.nombreDefecto, defectosEvaluados.valorDefecto, defectosEvaluados.controlCalidadPertenece) values (%d, '%s', %d, %d)" % (int(idDefectoEvaluado), element[0], 0, int(idControl))
			self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		self.getDefectosByControl(idControl)
	
	#obtener el ultimo ingresado...
	def getLastInsert(self):
		
		print self.getMaxControl()
	
	#editar cantidad de un defecto dado su id...
	def editCantidadDefecto(self, defecto, cantidad, idControl):
		
		defect = defecto.replace("-", " ")
		query = "update defectosEvaluados set defectosEvaluados.valorDefecto = %d where defectosEvaluados.controlCalidadPertenece = %d AND defectosEvaluados.iddefectos = %d" % (int (cantidad), int(idControl), int (defecto))
		print query
		self.Connect.initConnectionDB()
		self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener cantidad de observaciones de defecto en control...
	def getCantidadDefecto(self, idControl):
		
		query = "select defectosEvaluados.iddefectos, defectosEvaluados.valorDefecto from defectosEvaluados where defectosEvaluados.controlCalidadPertenece = %d" % int(idControl)
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List
	
	#obtener lista de defectos segun importancia...
	def getListaDefectosByImportancia(self, idPlanilla, importancia):
		
		#se obtiene el id del defecto en planilla, el nombre del defecto y la configuracion...
		query = "select defectoEnPlanilla.iddefectoEnPlanilla, defectoEnPlanilla.nombreDefecto, configuracion.idconfiguracion from defectoEnPlanilla join importanciaDefecto on (defectoEnPlanilla.iddefectoEnPlanilla = importanciaDefecto.iddefectoEnPlanilla) join importancia on (importanciaDefecto.idimportancia = importancia.idimportancia) join configuracion on (configuracion.iddefectoEnPlanilla = importanciaDefecto.iddefectoEnPlanilla AND importanciaDefecto.idimportancia = configuracion.idimportancia) where defectoEnPlanilla.idplanilla = %d AND importancia.valorImportancia = '%s'" % (int(idPlanilla), str(importancia))
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List
	
	#obtener la configuracion de la importancia...
	def getConfiguracionImportancia(self, idDefecto):
		
		query = "select configuracion.verde, configuracion.amarillo, configuracion.rojo from configuracion where configuracion.iddefectoEnPlanilla = %d" % (int(idDefecto))
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List#se obtienen en el orden de verde, amarillo y rojo...
	
	#evaluar nota por defecto...
	def evaluateByDefecto(self, defecto, importanciaDefecto):
		
		#3=rojo, 2=amarillo, 1=verde
		
		nota =0
		#evaluamos el rojo...
		if defecto > importanciaDefecto[0][2]:
			nota =3
		else:#preguntamos rango amarillo
			if (defecto <=importanciaDefecto[0][2]) and (defecto > importanciaDefecto[0][1]):
				nota = 2
			else:
				nota = 1
		return nota

	#obtener defectos evaluados segun importancia
	def getDefectosEvaluados(self, idControl, Lista):
		
		informationDefecto = {}
		self.Connect.initConnectionDB()
		for element in Lista:
			
			query = "select defectosEvaluados.nombreDefecto, defectosEvaluados.porcentaje from defectosEvaluados where defectosEvaluados.controlCalidadPertenece = %d and defectosEvaluados.nombreDefecto = '%s'" % (int(idControl), str(element[1]))
			List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
			informationDefecto.update({str(List[0][0]):int(List[0][1])})
		self.Connect.closeConnectionDB()
	
		return informationDefecto
	
	#contar elementos de una lista
	def getNumberElementos(self, lista, elemento):
		
		number=0
		
		for element in lista:
			if element == elemento:
				number+=1
		return number
		
	#obtener la nota del control...
	def generateNotaControl(self, notaMayor, notaMenor):
		
		notaFinal = 0#3 = rojo, 2 = amarillo, 1 = verde
		
		if 3 in notaMayor:
			notaFinal = 3
		else:
			if 3 in notaMenor:
				notaFinal = 3
			
			#preguntamos si es amarilla
			else:
				
				#contamos los amarillos en las listas
				amarillosMayor = self.getNumberElementos(notaMayor, 2)
				amarillosMenor = self.getNumberElementos(notaMenor, 2)
				
				#contamos los amarillos en las listas
				verdesMayor = self.getNumberElementos(notaMayor, 1)
				verdesMenor = self.getNumberElementos(notaMenor, 1)
				
				#vemos si es amarillo
				if (amarillosMayor > verdesMayor) and (amarillosMayor > verdesMenor):
					notaFinal=2
				else:
					if (amarillosMenor > verdesMayor) and (amarillosMenor > verdesMenor):
						notaFinal=2
					else:
						notaFinal=1
						
		return notaFinal
		
	#comenzar a calcular la nota del control efectuado...
	def calculateNotaControl(self, idPlanilla, idControl):
		
		#calculamos los porcentajes...
		self.editarPorcentaje(idPlanilla, idControl)
		
		notaMayor = []
		notaMenor = []
		
		#obtenemos listado de defectos mayores...
		ListaMayores = self.getListaDefectosByImportancia(idPlanilla, "MAYORES")
		
		#trabajamos para obtener primero la nota de los mayores...
		if len(ListaMayores) >0:#si existen defectos mayores...
			
			#obtenemos la configuracion de la importancia
			configuracion = self.getConfiguracionImportancia(ListaMayores[0][0])
			print configuracion
			
			informationDefectos = self.getDefectosEvaluados(idControl, ListaMayores)
			
			print informationDefectos
			
			for key in informationDefectos:
				notaMayor.append(self.evaluateByDefecto(informationDefectos[key], configuracion))
			
		ListaMenores = self.getListaDefectosByImportancia(idPlanilla, "MENORES")
		if len(ListaMenores) >0:#si existen defectos mayores...
			
			#obtenemos la configuracion de la importancia
			configuracion = self.getConfiguracionImportancia(ListaMenores[0][0])
			print configuracion
			
			informationDefectos = self.getDefectosEvaluados(idControl, ListaMenores)
			print informationDefectos
		
			for key in informationDefectos:
				notaMenor.append(self.evaluateByDefecto(informationDefectos[key], configuracion))
		
		print "Notas Mayor: ", notaMayor
		print "Notas Menor: ", notaMenor
		
		notaFinal = self.generateNotaControl(notaMayor, notaMenor)
		print "Nota Final del Control: ", notaFinal
	
		#hacemos la insercion en la nota...
		self.insertIntoNota(idControl, notaFinal)
		
		#revisamos si es nota roja y generamos la alerta...
		if notaFinal == 3:
			self.insertIntoAlerta(idControl)
			
	#obtener el maximo id de la nota...
	def getMaxAlerta(self):
		
		val =0
		query = "select Max(alerta.idalerta) from alerta"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#insertar en alerta...
	def insertIntoAlerta(self, idControl):
		
		idAlerta = self.getMaxAlerta()+1
		
		query = "insert into alerta values (%d, '%s', %d)" % (int (idAlerta), "Alerta!! Nota Peligrosa", int(idControl))
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
		
	#obtener el maximo id de la nota...
	def getMaxNota(self):
		
		val =0
		query = "select Max(notaControl.idnotaControl) from notaControl"
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		
		if List[0][0] == None:
			val=0
		else:
			val=List[0][0]
		
		return val
	
	#insertar la nota en la base de datos...
	def insertIntoNota(self, idControl, nota):
		
		idNota = self.getMaxNota()+1
		
		query = "insert into notaControl values (%d, %d, %d)" % (int(idNota), int(nota), int(idControl))
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener tamano de muestra de control...
	def getMuestraSize(self, idControl):
		
		query = "select controlCalidadEfectuado.tamanoMuestra from controlCalidadEfectuado where controlCalidadEfectuado.controlCalidad = %d" % int(idControl)
		self.Connect.initConnectionDB()
		
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		self.Connect.closeConnectionDB()
		return List[0][0]
	
	#sacar porcentaje...
	def editarPorcentaje (self, idPlanilla, idControl):
		
		ListaDefectos = self.getCantidadDefecto(idControl)
		muestra = self.getMuestraSize(idControl)
		
		self.Connect.initConnectionDB()
		for element in ListaDefectos:
			
			porcentaje = int((int(element[1])*100)/int(muestra))
			#hacemos la actualizacion...
			query = "update defectosEvaluados set defectosEvaluados.porcentaje = %d where defectosEvaluados.controlCalidadPertenece = %d AND defectosEvaluados.iddefectos = %d" % (porcentaje, int(idControl), int(element[0]))
			self.CrudDataBase.insertToTable(query, self.Connect)
		self.Connect.closeConnectionDB()
	
	#obtener informacion sobre los defectos evaluados y su porcentaje obtenido...
	def getInformationProcess(self, idControl):
		
		query = "select defectosEvaluados.nombreDefecto, defectosEvaluados.valorDefecto, defectosEvaluados.porcentaje from defectosEvaluados join controlCalidadEfectuado on (defectosEvaluados.controlCalidadPertenece = controlCalidadEfectuado.controlCalidad) where defectosEvaluados.controlCalidadPertenece = %d" % int(idControl)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
	
	#obtener informacion de la nota del control de calidad y el proceso efectuado...
	def getInformationNotaProcess(self, idControl):
		
		query = "select Distinct notaControl.valorNotaObtenida, controlCalidadEfectuado.fechaControl, controlCalidadEfectuado.tamanoMuestra, digitador.nombreDigitador from controlCalidadEfectuado join digitador on (controlCalidadEfectuado.digitador = digitador.iddigitador) join notaControl on (controlCalidadEfectuado.controlCalidad = notaControl.controlCalidad) where controlCalidadEfectuado.controlCalidad = %d" % int (idControl)
		self.Connect.initConnectionDB()
		List = self.CrudDataBase.queryBasicDataBase(query, self.Connect)
		for element in List:
			for i in range (len(element)):
				if i == (len(element) -1):
					print element[i]
				else:
					print element[i], ";",
		
		self.Connect.closeConnectionDB()
		
def main ():
	
	st = ManagerUserSystem()
	
	if sys.argv[1] == "1":#get information of campo
		st.getNombreDigitador()
	
	elif sys.argv[1] == "2":
		st.insertIntocontrolCalidadEfectuado(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	elif sys.argv[1] == "3":
		st.getLastInsert()
	
	elif sys.argv[1] == "4":
		st.getDefectosByControl(sys.argv[2])
	
	elif sys.argv[1] == "5":
		st.editCantidadDefecto(sys.argv[2], sys.argv[3], sys.argv[4])
	
	elif sys.argv[1] == "6":#calcular nota control
		st.calculateNotaControl(sys.argv[2], sys.argv[3])
	
	elif sys.argv[1] == "7":#obtener informacion proceso
		st.getInformationProcess(sys.argv[2])
		
	elif sys.argv[1] == "8":#obtener informacion de la nota obtenida...
		st.getInformationNotaProcess(sys.argv[2])	
	return 0

if __name__ == '__main__':
	main()

