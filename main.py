from configparser import ConfigParser
import SQL.MySQLFunc as SQL
import sys
from colors import *



def error(*messages):
	print COLORSBASH["RED"]+"$"*15+"ERROR"+"$"*15+COLORSBASH["END"]
	for mes in messages:
		print mes
	sys.exit(1)


def ReadConf(file="config.ini",prefix="./configs/"):
	config = ConfigParser()
	config.read(prefix+file)
	turned = config.get("MySQL","on")
	if turned == False:
		error("For a while that don't with only MySQL")
	return True

def StartThreads():
	pass

def main():
	ReadConf()
	print "\033]0;GostcoinExplorer\007"+COLORSBASH["GREEN"]+"Start threads now."+COLORSBASH["END"]
	StartThreads()	

main()
