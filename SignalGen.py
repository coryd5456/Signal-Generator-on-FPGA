import math
import numpy as np
N = 256

for l in range(0,N):
	pass
	for n in range(0,3):#I could make this loads shorter, but keeping this structure for now. Don't need n. 
		pass
		
		if n==0:
			pass
			print("assign Signal["+str(n)+"]["+str(l)+"] = 8'b"+str(bin(int(75+50*math.sin(2*np.pi*l/N)))[2:].zfill(8)+"; "), end = ''),
		elif n==1:
			pass
			print("assign Signal["+str(n)+"]["+str(l)+"] = 8'b"+str(bin(int(75+50*math.atan(2*np.pi*(l-N/2)/N)))[2:].zfill(8)+"; "), end = ''),
			
		elif n==2:
			pass
			print("assign Signal["+str(n)+"]["+str(l)+"] = 8'b"+str(bin(int(75+50*math.tanh(2*np.pi*(l-N/2)/N)))[2:].zfill(8))+"; ")
				