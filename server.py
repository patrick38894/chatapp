# TCP Server Code
 
host="127.0.0.1"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4446
from socket import *                # Imports socket module
import thread
 
s=socket(AF_INET, SOCK_STREAM)
 
s.bind((host,port))                 # Binds the socket. Note that the input to
                                            # the bind function is a tuple
 
s.listen(10)                         # Sets socket to listening state with a  queue
                                            # of 1 connection
 
print "Listening for connections.. "
q = []
def listen():
	while (1):
		tempsock, addr = s.accept()
		q.append(tempsock)

thread.start_new_thread(listen,())               # Accepts incoming request from client and returns
                                            # socket and address to variables q and addr
 
data=raw_input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                            # user
for i in q: 
	i.send(data)                        # Sends data to client
 
s.close()
 
# End of code
#jk


class client(object):
	def __init__(sake, address):
		self.sake

class user(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password 
		self.logged_in = False
	
class server(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.clients_users = [] #a list of 2tuples of client/user pairs or nil users for unlogged in dudes
		self.sake = socket(AF_INET,SOCK_STREAM)
		self.sake.bind((self.host,self.port))
		self.sake.listen(10)
		self.running = true
		thread.start_new_thread(listen, ())
		
	def listen(self):
		print("listening sequence initiated")
		while(self.running):
			tempsock, tempaddr = self.sake.accept()
			self.clients.append(client(tempsock, tempaddr))

	def read(self, sock):
		msg = sock.recv(2048)
		self.parse(msg)

	def broadcast(self, msg, target="all"):
		if target == "all":
			for i in self.clients:
				if i.logged_in:
					i.sock.send(msg)
		else
			for i in self.clients:
				if i.logged_in && i.username == target:
					i.sock.send(msg)

	def parse(self, msg):
		mylist = msg.split(" ")
		msgtype = mylist[0] #possible types include: msg, login, logout, ping, signup
		if msgtype == "msg":
			dest = mylist[1]
			text = mylist[len(msgtype) + len(dest) + 2:]
			
		#todo: all the other stuff
