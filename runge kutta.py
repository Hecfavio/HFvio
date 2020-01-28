import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi
	
E=0
longitud=1.666
R=3
L=0.0045
V1=230*math.sqrt(2)
w=2*pi*60
Tm=0
J=0.082
K=2.477
cq=np.zeros(6)
pcq=np.zeros(6)
kan=np.zeros(6)
adisparo=np.arange(20,)
paso=0.0001666

anchdisparo=100/360/60

caso=3
alpha=20
anchdisparo=100
anchdisparo=anchdisparo/360/60
if caso>1:
	if caso<4:
		adisparo=np.arange(alpha/360/60,alpha/360/60+2/120,1/120)

if caso>4:	
	if caso<7:
		adisparo=np.arange(alpha/360/60,alpha/360/60+6/360,1/360)

def f1(x,y):
	if caso==1:
		return -y*R/L-(E/L)+V1/L	
	if caso==2:
		if cq[0]==0:
			if cq[1]==0:
				return 0
		if cq[0]==1:
			return -y*R/L-(E/L)+V1/L*math.sin((x*w))
		if cq[1]==1:
			return -y*R/L-(E/L)+V1/L*math.sin((x*w)+pi)
	if caso==3:
		if cq[0]==0:
			if cq[1]==0:
				return 0
		if cq[0]==1:
			if math.sin(x)<=0:
				if x>adisparo[1]+(kan[1])/60:
					return -y*R/L-(E/L)
		if cq[0]==1:
			return -y*R/L-(E/L)+V1/L*math.sin((x*w))
	
		if cq[1]==1:
			if math.sin(x+pi)<=0:
				if x>adisparo[0]+(kan[0])/60:
					return -y*R/L-(E/L)
		if cq[1]==1:
			return -y*R/L-(E/L)+V1/L*math.sin((x*w)+pi)


def f2(x,y):
	return ((x)-Tm)/J
def f3(x):
	global kan,pcq,cq,E,caso,y,adisparo
	if caso==1:
		return V1
	if caso==2:
		volt1=V1*math.sin(w*x)
		volt2=V1*math.sin(w*x+pi)	

		if x>adisparo[0]+(kan[0]/60):	
			pcq[0]=1
		if x>anchdisparo+adisparo[0]+(kan[0]/60):
			pcq[0]=0
			kan[0]=kan[0]+1	

		if x>adisparo[1]+(kan[1]/60):
			pcq[1]=1
		if x>anchdisparo+adisparo[1]+(kan[1]/60):
			pcq[1]=0
			kan[1]=kan[1]+1

		if pcq[0]==1:
			if volt1>E:
				if volt1>volt2:
					cq[0]=1
					cq[1]=0
		if pcq[1]==1:
			if volt2>E:
				if volt2>volt1:
					cq[1]=1
					cq[0]=0
		if cq[0]==1:
			return volt1
		if cq[1]==1:
			return volt2
		if cq[0]==0:
			if cq[1]==0:
				return E
	if caso==3:
		volt1=V1*math.sin(w*x)
		volt2=V1*math.sin(w*x+pi)

		if x>adisparo[0]+(kan[0]/60):
			pcq[0]=1
		if x>anchdisparo+adisparo[0]+(kan[0]/60):
			pcq[0]=0
			kan[0]=kan[0]+1

		if x>adisparo[1]+(kan[1]/60):
			pcq[1]=1
		if x>anchdisparo+adisparo[1]+(kan[1]/60):
			pcq[1]=0
			kan[1]=kan[1]+1

		if pcq[0]==1:
			if volt1>E:
				if volt1>volt2:
					cq[0]=1
					cq[1]=0
		if pcq[1]==1:
			if volt2>E:
				if volt2>volt1:
					cq[1]=1
					cq[0]=0
		if cq[0]==1:
			if pcq[1]==1:
				return volt2

		if cq[0]==1:
			if volt1<0:
				return 0

		if cq[0]==1:
			return volt1

		if cq[1]==1:
			if pcq[0]==1:
				return volt1

		if cq[1]==1:
			if volt2<0:
				return 0

		if cq[1]==1:
			return volt2
		if cq[0]==0:
			if cq[1]==0:
				return E
	if caso==4:
		volt1=V1*math.sin(w*x)
		volt2=V1*math.sin(w*x+1*pi/3)
		volt3=V1*math.sin(w*x+2*pi/3)
		volt4=V1*math.sin(w*x+3*pi/3)
		volt5=V1*math.sin(w*x+4*pi/3)
		volt6=V1*math.sin(w*x+5*pi/3)





def rk4(f1,f2,f3,a,b,y0,h):
	global cq,E
	x=np.arange(a,b+h,h)
	n=len(x)
	y=np.zeros(n)
	v=np.zeros(n)
	v1=np.zeros(n)
	volts=np.zeros(n)
	torque=np.zeros(n)
	y[0]=y0
	
	v[0]=0
	v1[0]=0
	for i in range(0,n-1):
		k11=f1(x[i],y[i])
		k12=f1(x[i]+h/2,y[i]+k11*h/2)
		k13=f1(x[i]+h/2,y[i]+k12*h/2)
		k14=f1(x[i]+h,y[i]+k13*h)
		y[i+1]=y[i]+(h/6)*(k11+2*k12+2*k13+k14)
		torque=y*K
		v1[i+1]=f2(torque[i],v[i])*paso
		v1[i+1]=v1[i]+v1[i+1]
		volts[i+1]=f3(x[i+1])
		E=v1[i+1]/K
		
		if cq[0]==1:
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				cq[0]=0
		if cq[1]==1:
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				cq[1]=0
		if cq[2]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq3=0
		if cq[3]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq4=0
		if cq[4]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq5=0
		if cq[5]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq6=0

	plt.plot(x,torque)
	plt.plot(x,y)
	plt.plot(x,v1)
	plt.plot(x,volts)
	plt.show()
def main():		
	rk4(f1,f2,f3,0,longitud,0,paso)

if __name__=='__main__':
	main()	






