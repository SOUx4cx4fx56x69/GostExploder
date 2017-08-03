from configparser import ConfigParser
import mysql.connector
import atexit
from mysql.connector import errorcode
class MySQL:

 sql = None
 host = ""
 port = 0
 user = ""
 password = ""
 database = ""

  
 def read_config(self,file,prefix="./configs/"):
  config = ConfigParser()
  config.read(prefix+file)
  return config
 
 def init_sql(self,file):
  conf = self.read_config(file)
  self.host = conf.get('MySQL','host')
  self.port = conf.get('MySQL','port')
  self.user = conf.get('MySQL','user')
  self.password = conf.get('MySQL','pass')
  self.database = conf.get('MySQL','database')

 def connect(self):
  try:   
   self.sql = mysql.connector.connect(user=self.user, password=self.password,
                                 host=self.host,port=self.port,
                                 database=self.database)
  except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
     print("SQL: Something is wrong with your user name or password")
     self.sql = False
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
     print("SQL: Database does not exist")
     self.sql = False
   else:
     print(err)
     self.sql = False
 def connect_restart(self):
  while self.connect() == False:
    print "Do not can connect to SQL"
    continue

 def destruct(self):
  if self.sql != 0:
   #print "...Close sql..."
   self.sql.close()  

 def commit(self):
  while True:
   try:
    self.sql.commit()
    return True
   except Exception as e:
    self.destruct()
    print "SQL error(commit): "+str(e)+"\n Try new..."
    self.connect_restart()

 def cursor(self):
  return self.sql.cursor()

 def query(self,sql,params_list):
  while True:
   try:
    cursor = self.sql.cursor()
    cursor.execute(sql, params_list)
    return cursor
   except Exception as e:
    self.destruct()
    print "SQL error(query): "+str(e)+"\n Try new..."
    self.connect_restart() 
   
#for (first_name, last_name, hire_date) in cursor:
#  print("{}, {} was hired on {:%d %b %Y}".format(
#    last_name, first_name, hire_date))
 def __init__(self,file="config.ini"):
  self.init_sql(file)
  self.connect()
  
  atexit.register(self.destruct)

 
