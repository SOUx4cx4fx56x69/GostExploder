import hashlib,base64
import socket,json

class RPC:
 #hashf = 0
 RPCauth = ""
 RPCAddr = ""
 RPCport = 0
 
 def init_string_forRPC(self,method,params=False):
  if params:
   return "{\"jsonrpc\": \"1.0\", \"id\":\"null\", \"method\": \""+method+"\", \"params\": ["+params+"] }"
  return "{\"jsonrpc\": \"1.0\", \"id\":\"null\", \"method\": \""+method+"\", \"params\": [] }"

 def methodRPC(self,method,inJson=True):
 # print "Start connection with"
 # print self.RPCAddr+":"+str(self.RPCport)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect( (self.RPCAddr,self.RPCport) )
  content_size = len(method)
  sock.send("POST / HTTP/1.1\r\nHost: "+self.RPCAddr+":"+str(self.RPCport)+"\r\nAuthorization: Basic "+self.RPCauth+"\r\nAccept: */*\r\ncontent-type: text/plain;\r\nContent-Length: "+str(content_size)+"\r\n\r\n"+method+"\r\n\r\n")
  string = sock.recv(4096)
  sock.close()
  if inJson:
   string = string.split("\n")
   i = 0
   while string[i][0] != '{':
    i = i+1
   string = json.loads(string[i])
   return string
  else:
   return string
  
 def __init__(self,rpcAdress,rpcPort,rpcUser,rpcPass):
  self.RPCauth = base64.b64encode(str(rpcUser)+":"+str(rpcPass))
  self.RPCAddr = rpcAdress
  self.RPCport = rpcPort

