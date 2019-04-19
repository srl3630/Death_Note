import os
import yaml
import re
from datetime import datetime
from TargetCollection import TargetClctn

def initial_read():
	# read hosts file
	with open(os.path.join("YML",'hosts.yml')) as f:
		os_groups = yaml.safe_load(f)
	# Create os groups for targetting
	Targets = TargetClctn(os_groups)
	return Targets

def parse_punish():
	# Parse Death_Note
	with open(os.path.join("YML",'death_note.yml')) as f:
		punishbook = (yaml.safe_load(f))
	return punishbook

# logs errors
def logme(error):
	f = open('log.log', 'a')
	mystr = str(datetime.now()) + ": " + str(error)
	f.write(mystr)
	print(mystr)
	f.close()

# reads credentials based on machine
def read_creds(ip):
	with open(os.path.join("YML",'usernames.yml')) as f:
		ip_groups = yaml.safe_load(f)
	rex = re.search('(\d{1,3}\.)\d{1,3}(\.\d{1,3}\.\d{1,3})', ip)
	return ip_groups[rex.group(1) + 'x' + rex.group(2)][0]