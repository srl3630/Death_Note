'''
detcord : Action execution on hosts

Micah Martin - knif3
'''

from detcord import action

@action
def test(host):

	ret = host.run("touch /home/landon/Desktop/Bunnies.txt", sudo=True)

	try:
		host.put("exploit_cl.py", "/tmp/exploit_cl.py")
	except PermissionError as E:
		# Catch a permission denied error and try again as root
		host.put("exploit_cl.py", "/tmp/exploit_cl.py", sudo=True)



def support_action():
	pass
