# script to automate checking default credentials + other low hanging fruit, and doling out punishments
# in the form of single commands ( can be extended to do more later )

import time
from utils import *

def start_punishing():
	punishbook = parse_punish() # read in death note
	Targets = initial_read() 	#read targets
	start_Time = time.mktime(time.strptime(punishbook['Start_time'], "%m/%d/%Y %H:%M:%S")) # parse start time as epcoh time
	for curact in range(1,1000): # iterate through actions
		if punishbook['Action_'+ str(curact)]: # If another action exsts
			pun_sec = punishbook['Action_'+str(curact)]['Minute']*60 # calculate epoch time
			while(True):
				# Execute if within a minute of start time
				if (time.time()+pun_sec >= start_Time + pun_sec) and time.time()+pun_sec <= start_Time + pun_sec + 60:
					check = punishbook['Action_'+str(curact)]['Check'] # grab service to check
					mymethod = check['method'] # grab method to check
					# perform check
					Targets.run_routine(check['args'],mymethod,punishbook['Action_'+str(curact)]['Punish'],check['groups'])
					break
				else:
					# sleep until next action
					time.sleep(1)

		else:
			print('Justice has been served, exiting')
			break

start_punishing()



