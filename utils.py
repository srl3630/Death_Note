import os
import yaml
import re
from datetime import datetime
from TargetCollection import TargetClctn

def initial_read():
	with open(os.path.join("YML",'hosts.yml')) as f:
		os_groups = yaml.safe_load(f)
	Targets = TargetClctn(os_groups)
	return Targets

def parse_punish():
	with open(os.path.join("YML",'death_note.yml')) as f:
		punishbook = (yaml.safe_load(f))
	return punishbook


def logme(error):
	f = open('log.log', 'a')
	f.write(str(datetime.now()) + ": ")
	f.write(error)
	f.close()

def read_creds(ip):
	with open(os.path.join("YML",'usernames.yml')) as f:
		ip_groups = yaml.safe_load(f)
	rex = re.search('(\d{1,3}\.\d{1,3}\.)\d{1,3}(\.\d{1,3})', ip)
	return ip_groups[rex.group(1) + 'x' + rex.group(2)][0]