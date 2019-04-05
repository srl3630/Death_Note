import os
import utils

# generic parent shell class
class shell_class:

	def __init__(self,shell):
		self.shell = shell

	def execute(self,command):
		pass

	def close(self):
		pass

# handles ssh shell
class ssh_shell(shell_class):

	def __init__(self,shell):
		shell_class.__init__(self,shell)

	def drop_payload_linux(self,payload_name,dir_path):
		ftp_client = self.shell.open_sftp()
		ftp_client.put(os.path.join("Payloads",payload_name),dir_path)
		ftp_client.close()

	def execute(self,command):
		utils.logme("executing command: " + command + "\n")
		self.shell.exec_command(command)


	def close(self):
		self.shell.close()


# handles socket shell
class socket_shell(shell_class):

	def __init__(self,shell):
		shell_class.__init__(self,shell)
	def drop_payload_linux(self,payload_name,dir_path):
		pass

	def execute(self,command):
		utils.logme("executing command: " + command + "\n")
		self.shell.sendall(bytes(command + "\n", "utf-8"))

	def close(self):
		self.shell.close()