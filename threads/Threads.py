import SQL.MySQLFunc as SQL
import sys
from colors import *

TYPES = {
"MySQL":0
}
def GETTYPE(TYPE):
	for t in TYPES:
	 #print t
	 if t == TYPE:
		return TYPES[t]

class Threads:

 def __init__(self,sql):
	self.SQL=sql

 def BlocksAdder(self,datfile,type="MySQL"):
	TypeSQL = GETTYPE(type)
	if TypeSQL == 0:
	 print COLORSBASH["WHITE"]+"...MySQL is used..."+COLORSBASH["END"]
	 SQL.Thread(datfile)
