


import time
import piconzero as pz
import hcsr04

pz.setInputConfig(2,0)
pz.setInputConfig(3,0)
pz.init()
hcsr04.init()
speed = 100
i=0
try:
	while True:
		if ((pz.readInput(2)!=1) and (pz.readInput(3)!=1) and i%2==0):
			pz.stop()
			time.sleep(0.1)
			pz.spinLeft(100)
			time.sleep(0.2)
		elif ((pz.readInput(2)!=1) and (pz.readInput(3)!=1) and i%2==1):
			pz.stop()
			time.sleep(0.1)
			pz.spinRight(100)
			time.sleep(0.2)
		elif ((pz.readInput(2)==1) and (pz.readInput(3)==1)):
			i+=1
		else:
			pz.reverse(70)
except KeyboardInterrupt:
	print "Au revoir"
finally:
	pz.cleanup()
