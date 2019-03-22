# parent class for all payloads

class payload_class():

	def __init__(self,shell):
		self.shell = shell

	def execute_payload(self):
		pass

# execute a command
class command(payload_class):

	def __init__(self,shell,args):
		payload_class.__init__(self,shell)
		self.command = args['command']

	def execute_payload(self):
		self.shell.execute(self.command)

# drop a payload from this machine to target
class send_exec_bin_lin(payload_class):

	def __init__(self,shell, args):
		payload_class.__init__(self,shell)
		self.payload_name = args['payload_name']
		self.dir_path = args['dir_path']

	def execute_payload(self):
		self.shell.drop_payload_linux(self.payload_name,self.dir_path)
		self.shell.execute('cd '+self.dir_path)
		self.shell.execute('./'+self.payload_name)

