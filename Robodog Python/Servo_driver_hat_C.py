import PCA9685 as d

'''
--2020 April 4--
LOTP RoboDog Project - Servo Driver Module

Servo Driver : Waveshare PCA9685 


setServo(Servo Port , Degree) // Set servo on selected port to given degree

resetServo(Servo Port) // Set servo on selected port to servo's zero degree

resetAllServo(Degree) // Set all servos to given degree

setServozero(Servo Port , Degree) // Set servo's zero degree to given degree

setServomin(Servo Port , Minimum Degree) // Set servo's minimum degree limit on selected port

setServomax(Servo Port , Minimum Degree) // Set servo's maximum degree limit on selected port

setServorot(Servo Port , value) // If value is 1 for selected port, reverse servo rotation
                               Example : If i set servo degree to 50 while servo rotation value 0, servo will go to 50 degree
                                         If rotation value is 1, servo will go to 130 (because 180-50=130)

'''

pwm=d.PCA9685(0x40)

pwm.setPWMFreq(50)
min=[0]*16
max=[180]*16
rotation=[0]*16
zero=[0]*16

def setServo(port,deg):
        deg+=zero[port]
        deg=abs(deg-rotation[port]*180)
        if(deg>=min[port] and deg<=max[port]):
                pwm.setServoPulse(port,500+deg*2000/180)
        elif(deg<min[port]):
                pwm.setServoPulse(port,500+min[port]*2000/180)
        else:
                pwm.setServoPulse(port,500+max[port]*2000/180)

def resetServo(port):
        setServo(port,zero[port])

def resetAllServo(deg):
        for i in range(0,16):
                setServo(i,deg)

def setServozero(port,deg):
        global zero
        zero[port]=deg

def setServomin(port,minDeg):
        global min
        min[port]=minDeg

def setServomax(port,maxDeg):
        global max
        max[port]=maxDeg

def setServorot(port,val):
        global rotation
        rotation[port]=val





if(__name__=="__main__"):
	for i in range(0,16):
		setServozero(i,90)

	resetAllServo(0)
	#setServomin(0,40)
	#setServomax(0,135)
	while(1):
		deg=int(input("Degree : "))
		servo=int(input("Servo : "))
		setServo(servo,deg)
