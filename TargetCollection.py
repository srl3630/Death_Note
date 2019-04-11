import exploit_cl
import payload_cl
import shell_cl
import threading
from Thread_Exploits import run_threaded_routine
import inspect

# Collection of ip addresses to be attacked

class TargetClctn(object):
	def __init__(self, os_group):
		self.os_group = os_group

	def run_routine(self, args, method, punishment,groups):
		# iterate through all ips in selected groups
		for i in groups:
			threads = []
			for ip in self.os_group[i]:
				threads.append(threading.Thread(target=run_threaded_routine, args=(args,method,punishment,ip,)))
			for thread in threads:
				thread.start()
			for thread in threads:
				thread.join()

		return


