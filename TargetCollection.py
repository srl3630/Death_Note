import exploit_cl
import payload_cl

class TargetClctn(object):
	def __init__(self, os_group):
		self.os_group = os_group

	def run_routine(self, args, method, punishment,groups):
		used_ips = []
		for i in groups:
			for ip in self.os_group[i]:
				if ip not in used_ips:
					shell = getattr(exploit_cl,method)(ip,args)
					getattr(payload_cl,punishment['type'])(shell).execute_payload()
					shell.close()
					used_ips += ip
		return


