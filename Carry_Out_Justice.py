import time
from utils import *

def start_punishing():
	punishbook = parse_punish()
	Targets = initial_read()
	start_Time = time.mktime(time.strptime(punishbook['Start_time'], "%m/%d/%Y %H:%M:%S"))
	for curact in range(1,1000):
		if punishbook['Action_'+str(curact)]:
			pun_sec = punishbook['Action_'+str(curact)]['Minute']*60
			while(True):
				if (time.time()+pun_sec >= start_Time + pun_sec) and time.time()+pun_sec <= start_Time + pun_sec + 60:
					check = punishbook['Action_'+str(curact)]['Check']
					mymethod = check['method']
					Targets.run_routine(check['args'],mymethod,punishbook['Action_'+str(curact)]['Punish'],check['groups'])
					break
				else:
					time.sleep(1)

		else:
			print('Justice has been served, exiting')
			break

start_punishing()



