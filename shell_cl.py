import os

class shell_class:

	def __init__(self,shell):
		self.shell = shell

	def execute(self,command):
		pass

	def close(self):
		pass

class ssh_shell(shell_class):

	def __init__(self,shell):
		shell_class.__init__(self,shell)

	def drop_payload_linux(self,payload_name,dir_path):
		ftp_client = self.shell.open_sftp()
		ftp_client.put(os.path.join("Payloads",payload_name),dir_path)
		ftp_client.close()

	def execute(self,command):
		self.shell.exec_command(command)


	def close(self):
		self.shell.close()

class socket_shell(shell_class):

	def __init__(self,shell):
		shell_class.__init__(self,shell)

	def drop_payload_linux(self,payload_name,dir_path):
		pass

	def execute(self,command):
		self.shell.send(command)

	def close(self):
		self.shell.close()