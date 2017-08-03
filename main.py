from configparser import ConfigParser
import SQL.MySQLFunc as SQL
import sys
from colors import *
import threads.Threads as t
datfile = ""

def error(*messages):
	print COLORSBASH["RED"]+"$"*15+"ERROR"+"$"*15
	for mes in messages:
		print mes
	print COLORSBASH["END"]
	sys.exit(1)


def ReadConf(file="config.ini",prefix="./configs/"):
	config = ConfigParser()
	config.read(prefix+file)
	turned = config.get("MySQL","on")
	if turned != 'false' and turned != 'true':
		error("Unccorect value of `on`")
	if turned == "false":
		error("For a while that don't with only MySQL")
	if config.get("MySQL","installed") == "false":
		print COLORSBASH["PURPLE"]+"Start instaling" +COLORSBASH["END"]
		SQL.InstallTables()
		config.set("MySQL","installed","true")
	global datfile
	datfile = config.get("datfile","path")
	return True

def StartThreads():
	thr = t.Threads(0)
	global datfile
	print COLORSBASH["BROWN"]+"Open dat file:" + datfile + COLORSBASH["END"]
	datfile = open(datfile,"rb+")
	thr.BlocksAdder(datfile)
	

def main():
	ReadConf()
	print "\033]0;GostcoinExplorer\007"+COLORSBASH["GREEN"]+"Start threads now."+COLORSBASH["END"]
	StartThreads()
	while 1:
	 pass	

main()
