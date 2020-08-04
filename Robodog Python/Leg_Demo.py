import Servo_driver_hat_C as sd
import Robodog_Controller as rc
import time

'''

'''

def Setup():
	# Configure rotations and zero points for servos
 
	sd.setServozero(0,-8)
	sd.setServozero(12,-5)
	sd.setServozero(1,5)
	sd.setServozero(13,-8)

	sd.setServorot(0,1)
	sd.setServorot(8,1)

	sd.setServorot(1,1)
	sd.setServorot(6,1)
	sd.setServorot(10,1)
	sd.setServorot(13,1)
	rc.updateServo()

def XLine_Demo():
	# Move the leg back and front on x axsis. +5 to -5 (defined on distance variable)
	global rr,rl,fr,fl
	distance=5
	x=-distance
	y=12
	z=0
	delay=0.05
	leg='rr'
	for i in range(0,distance*4):
		x+=0.5
		rc.leg_pos(leg,[x,y,z])
		rc.updateServo()
		time.sleep(delay)
	for i in range(0,distance*4):
		x-=0.5
		rc.leg_pos(leg,[x,y,z])
		rc.updateServo()
		time.sleep(delay)

def YLine_Demo():
		# Move the leg left and right on y axsis. +3.5 to -3.5 (defined on distance variable)

        global rr,rl,fr,fl
        distance=3.5
        y=-distance
        x=0
        z=0
        delay=0.05
        for i in range(int(distance*4)):
                y+=0.5
                rc.leg_pos('rr',[x,y+13.5,z])
                rc.updateServo()
                time.sleep(delay)
        for i in range(int(distance*4)):
                y-=0.5
                rc.leg_pos('rr',[x,y+13.5,z])
                rc.updateServo()
                time.sleep(delay)

def ZLine_Demo():
		# Move the leg up and down on z axsis. +6 to -6 (defined on distance variable)

        global rr,rl,fr,fl
        distance=6
        x=0
        y=12
        z=-distance
        delay=0.05
        for i in range(int(distance*4)):
                z+=0.5
                rc.leg_pos('rr',[x,y,z])
                rc.updateServo()
                time.sleep(delay)
        for i in range(int(distance*4)):
                z-=0.5
                rc.leg_pos('rr',[x,y,z])
                rc.updateServo()
                time.sleep(delay)

def Basic_Step(x1,x2,y,k,s0,path,z):
	#                  00000
	#               00   |   00
	#              0     k     0
	#             X1-----+-----X2 

	# Move leg X1 to X2 on parabol with k height
	# k is not cm type, Try to give it a small number (like 0.1)

	if(x1>x2):
		c=-1
	else:
		c=1
	positions=[]
	for i in range(0,round(abs(x2-x1)*path)+1):
		x=x1+(i*c/path)
		a=k/x1*x2
		#print('X : ',x,'    ','Y : ',k/x1*x2*(x-x1)*(x-x2)+y)
		positions.append([x,y-k/x1*x2*(x-x1)*(x-x2),z])
		positions.append(s0*abs(((x1+x2)/2)**2-x))
	return(positions)

def Basic_Move(x1,x2,y,s0,path,z):
				# Move leg X1---to----X2 position
                if(x1>x2):
                        c=-1
                else:
                        c=1
                positions=[]
                for i in range(0,round(abs(x2-x1)*path)+1):
                        x=x1+(i*c/path)
                        positions.append([x,y,z])
                        positions.append(s0*abs(((x1+x2)/2)**2-x))
                return(positions)

Setup()
while(1):
	input()
	for i in range(5):
		p=Basic_Step(7,-7,15,0.1,0.025,2,0)
		#print(p)
		for i in range(0,int(len(p)/2)):
			#print('a',i)
			rc.leg_pos('rr',p[i*2])
			time.sleep(p[i*2+1])
			rc.updateServo()
		p=Basic_Move(-7,7,15,0.01,2,0)
		#print(p)
		for i in range(0,int(len(p)/2)):
                        #print('a',i)
                        rc.leg_pos('rr',p[i*2])
                        time.sleep(p[i*2+1])
                        rc.updateServo()
	input()
	for i in range(5):
		XLine_Demo()
	input()
	for i in range(5):
		YLine_Demo()
	input()
	for i in range(5):
		ZLine_Demo()
