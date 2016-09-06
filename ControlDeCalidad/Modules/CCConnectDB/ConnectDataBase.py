import mysql.connector
import ConfigParser

#class that allow generate the connection enter mysqlDB and python sourcecode
class ConnectDataBase(object):

	#building for class
	def __init__(self):
		
		self.ConfigurationDB = None#give values to ConfigurationDB atributes
		self.getConfiguration()
		self.Conex = None 
		self.cursor= None
	
	#methon for get params for handler the connection to data base, reading file configuration
	def getConfiguration(self):

		Config = ConfigParser.ConfigParser()#instance of ConfigParser
		Config.read('/etc/ControlCalidad/configControlCalidad.cfg')

		#create dictionary for add information of connection
		dictionary_keys = {}
		dictionary_keys['user'] = Config.get('ConectionDataBase', 'user')
		dictionary_keys['password'] = Config.get('ConectionDataBase', 'pass')
		dictionary_keys['host'] = Config.get('ConectionDataBase', 'host')
		dictionary_keys['database'] = Config.get('ConectionDataBase', 'data_base')
		dictionary_keys['raise_on_warnings'] = True

		self.ConfigurationDB = dictionary_keys

	#method that inicializated the connection
	def initConnectionDB(self):
		self.Conex = mysql.connector.connect(**self.ConfigurationDB)#instance to connection
		self.cursor = self.Conex.cursor()

	#method that allow closed connection 
	def closeConnectionDB(self):
		self.cursor.close()
		self.Conex.close()
