import random
#from time import sleep
import myModule

from oscilloscope import Osc


# adjust window_sec and intensity to improve visibility
osc = Osc(window_sec=10, intensity=1)


@osc.signal
def increasing_signal(state):
    	pullData = open("my_file.txt","r").read()
	dataArray = pullData.rspilt("/n")
	for eachline in dataArray:
		if(len(eachline)>1):
			state.draw(float(eachline))
			myModule.fib(1)

osc.start()
