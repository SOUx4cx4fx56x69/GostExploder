import SQL.MySQLFunc as SQL
import sys,signal,threading
from colors import *
 

class mythread:
 thread = 0
 def join_thread(self):
  self.thread.join()

 def start_thread(self):
  self.thread.start()
  #print "Thread started"

 def __init__(self,func,argl=False):
  global thread
  if not argl:
   self.thread = threading.Thread(target=func)
  else:
   self.thread = threading.Thread(target=func,args=(argl))
  #print "Initted thread"
  self.start_thread()


TYPES = {
"MySQL":0
}
def GETTYPE(TYPE):
	for t in TYPES:
	 #print t
	 if t == TYPE:
		return TYPES[t]

def CLOSE(a=0,b=0):
	os.kill(os.getpid(), signal.SIGUSR1)
#	os.kill(os.getpid(), signal.SIGUSR2)

class Threads:

 def __init__(self,sql):
	self.SQL=sql

 def BlocksAdder(self,datfile,type="MySQL"):
	TypeSQL = GETTYPE(type)
	if TypeSQL == 0:
	 print COLORSBASH["WHITE"]+"...MySQL is used..."+COLORSBASH["END"]
	 threadOfReader = threading.Thread(target=SQL.Thread(datfile))
	 threadOfReader.start()
	 signal.signal(signal.SIGTERM,CLOSE)
 
