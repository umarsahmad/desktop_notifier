# desktop notifier using python

# plyer module needed

from plyer import notification

import time

if __name__== '__main__':
	while True:
		notification.notify(
			title=:"***Take Rest***",
			message="message is written over here",
			app_icon="copy here the adderess of the icon",
			timeout= 5) 
		time.sleep(3600) #for one hour delay 

# loop again and again for the notifications

# to save yourself from writing in cmd again and again: 
#use- pythonw __.py now it will repeat pop up every 1 hour, to stop it close through taskmanager end task of the python file over there

