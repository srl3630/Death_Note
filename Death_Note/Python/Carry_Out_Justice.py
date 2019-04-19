# script to automate checking default credentials + other low hanging fruit, and doling out punishments
# in the form of single commands ( can be extended to do more later )

import time
from utils import *
from multiprocessing.dummy import Pool as ThreadPool

def start_punishing():
	punishbook = parse_punish() # read in death note
	logme("Starting to serve justice \n")
	Targets = initial_read() 	#read targets
	start_Time = time.mktime(time.strptime(punishbook['Start_time'], "%m/%d/%Y %H:%M:%S")) # parse start time as epcoh time
	for curact in range(1,1000): # iterate through actions
		if 'Action_'+ str(curact) in punishbook: # If another action exsts
			pun_sec = punishbook['Action_'+str(curact)]['Minute']*60+punishbook['Action_'+str(curact)]['Hour']*3600 # calculate epoch time
			while(True):
				# Execute if within a minute of start time
				if (time.time() >= start_Time + pun_sec):
					check = punishbook['Action_'+str(curact)]['Check'] # grab service to check
					mymethod = check['method'] # grab method to check
					# perform check
					Targets.run_routine(check['args'],mymethod,punishbook['Action_'+str(curact)]['Punish'],check['groups'])
					break
				else:
					print("Minutes until next round:"+str((pun_sec+start_Time-time.time())//60)+"("+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(pun_sec+start_Time))+")")
					# sleep until next action
					time.sleep(60)

		else:
			print('Justice has been served, exiting')
			break

start_punishing()



