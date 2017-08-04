from configparser import ConfigParser
from colors import *
import getpass
from shutil import copyfile

print COLORSBASH["GREEN"]+"Start installing...."+COLORSBASH["END"]
print COLORSBASH["BROWN"]+"Set MySQL"
def SettingSet(Ask,default):
	tmp = raw_input(Ask+"("+default+"): ")
	if tmp == "":
		tmp = default
	return tmp
def GetInList(string):
	print ""
	strings = string.split("\n")
	tmp = ""
	waitnew = False
	tmplist = {}
	for s in strings:
		s = s.split("=")
		if s[0] == "rpcuser":
			tmplist['user']=s[1]
		if s[0] == "rpcpassword":
			tmplist['pass']=s[1]
	return tmplist

def getRPCParams(path):
	gc = open(path)
	gcl = gc.read(4096)
	user = ""
	password = ""
	gcl = GetInList(gcl)
	gc.close()
	return {"user":gcl['user'],"pass":gcl['pass']}

def SetConfig(mh,mp,mu,mpas,md,dp,gc,path="./tmpconfig.ini"):
	config = ConfigParser()
	config.read(path)
	config.add_section("MySQL")
	config.add_section("datfile")
	config.add_section("RPC")
	config.set("MySQL","on","true")
	config.set("MySQL","host",mh)
	config.set("MySQL","host",mh)
	config.set("MySQL","port",mp)
	config.set("MySQL","pass",mpas)
	config.set("MySQL","database",md)
	config.set("MySQL","installed","false")
	config.set("datfile","path",dp)
	config.set("RPC","host","127.0.0.1")
	config.set("RPC","port","3306")
	RPCU = getRPCParams(gc)
	config.set("RPC","user",RPCU['user'])
	config.set("RPC","password",RPCU['pass'])
	tmpfile = open(path,"wb")
	config.write(tmpfile)
	tmpfile.close()
	

UserName = getpass.getuser()

MySQLHost = SettingSet("Write your Host of MySQL","127.0.0.1")
MySQLPort = SettingSet("Write your Port of MySQL","3306")
MySQLUser = SettingSet("Write your User of MySQL","root")
MySQLPass = SettingSet("Write your Password of user of MySQL","root")
MySQLDB = SettingSet("Write your database of MySQL","Explorer")

DatPath = SettingSet("Write your path to dat file","/home/"+UserName+"/.gostcoin/blocks/blk00000.dat")
GostConf = SettingSet("Write your path to path conf of gostcoin","/home/"+UserName+"/.gostcoin/gostcoin.conf")

print DatPath

print COLORSBASH["END"]
SetConfig(MySQLHost,MySQLPort,MySQLUser,MySQLPass,MySQLDB,DatPath,GostConf)
Put = SettingSet(COLORSBASH["GREEN"]+"Config file ended, put that to configs?","y")
if Put == "y":
	copyfile("./tmpconfig.ini", "./configs/config.ini")
	print "Okey, i put:)"
	print COLORSBASH["END"]
else:
	print "Okey, put as you like."+COLORSBASH["END"]

