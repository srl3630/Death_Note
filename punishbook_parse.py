import yaml
import time
import Mechanisms

def parse_punish():
	with open('punishbook.yml') as f:
		punishbook = (yaml.safe_load(f))
	return punishbook

def start_punishing():
	punishbook = parse_punish()
	Targets = Mechanisms.initial_read()
	start_Time = time.mktime(time.strptime(punishbook['Start_time'], "%m/%d/%Y %H:%M:%S"))
	for curact in range(0,1000):
		if punishbook['Action_'+str(curact)]:
			pun_Sec = punishbook['Action_'+str(curact)]['Minute']*60
			while(True):
				if (time.time()+pun_Sec >= start_Time + pun_Sec) and time.time()+pun_Sec <= start_Time + pun_Sec + 60:
					check = punishbook['Action_'+str(curact)]['Check']
					mymethod = check['method']
					getattr(Targets,mymethod)(check['args'][0],punishbook['Action_'+str(curact)]['Punish']['command'],check['groups'])
					break
				else:
					time.sleep(1)

		else:
			print('Justice has been served, exiting')
			break



