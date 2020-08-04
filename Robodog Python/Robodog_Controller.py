import Servo_driver_hat as sd
from inputs import get_gamepad
import keyboard
import math
import time

'''
--2020 April 7--
LOTP RoboDog Project - Leg Controll Module

servo_pos(x,y,z) // Return 3 servo angel to move tiptoe to given 3 vector cordinats (distance from joint shoulder)

updateServos(): // Set all servo angel from fl, fr, rl, rf (Front left, Front right, Rear left, Rear right) arrays

'''

rr=[90]*3
rl=[90]*3
fr=[90]*3
fl=[90]*3

def updateServos():
	for i in range(0,3):
		sd.setServo(i,fl[i])
	for i in range(0,3):
		sd.setServo(i+4,fr[i])
	for i in range(0,3):
		sd.setServo(i+8,rl[i])
	for i in range(0,3):
		sd.setServo(i+12,rr[i])

def acos(x):
	if(x>1):
		res=1
	elif(x<-1):
		res=-1
	else:
		res=x
	return(math.acos(res))

def servo_pos(x,y,z):
	A1=5
	A2=10
	A3=13
	z0=z+A1
	if(z0>0):
		k=1
	else:
		k=-1
	h0=math.sqrt(z0**2+y**2)
	h=math.sqrt(h0**2-A1**2)
	a1= math.degrees(acos( (A1**2+h0**2-h**2) / (2*A1*h0) )) + (math.degrees(math.acos( (h0**2+y**2-z0**2) / (2*h0*y) ))*k)
	hx=math.sqrt(h**2+x**2)
	if(x>0):
		k=-1
	else:
		k=1
	a2=math.degrees(acos( (hx**2+A2**2-A3**2) / (2*hx*A2) )) + (math.degrees(math.acos( (hx**2+h**2-x**2) / (2*hx*h) ))*k )
	a2=90+a2
	#print(math.degrees((A2**2+A3**2-hx**2) / (2*A2*A3)))
	a3=math.degrees(acos( (A2**2+A3**2-hx**2) / (2*A2*A3) ))
	A0=5
	B=1.6
	C=5.2
	D=3
	a=90-a3
	A=D*math.tan(math.radians(abs(a)))
	if(a>0):
		k=1
	else:
		k=-1
	A=A0+(A*k)
	#print(A,B,C)
	a3=math.degrees(acos( (A**2+B**2-C**2) / (2*A*B) ))
	#print(a1,a2,a3)
	return(a1,a2,a3)

if(__name__=="__main__"):
	def Setup():
		sd.setServorot(2,1)
		updateServoS()

	def Line_Demo():
		global rr,rl,fr,fl
		x=-10
		y=15
		z=0
		delay=0.01
		for i in range(0,40):
			x+=0.5
			fl[0],fl[1],fl[2]=servo_pos(x,y,z)
			updateServos()
			time.sleep(delay)
		for i in range(0,40):
			x-=0.5
			fl[0],fl[1],fl[2]=servo_pos(x,y,z)
			updateServos()
			time.sleep(delay)

	def Controller_Demo():
		x=getGamepadvalue("ABS_RX")*10/33000
		#z=getGamepadvalue("ABS_RY")/3000
		print(x)
		#fl[0],fl[1],fl[2]=servo_pos(x,10,0)
		#updateServo()

	Setup()
	while(1):
		pass
		#Line_Demo()
		#Controller_Demo()
