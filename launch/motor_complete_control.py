import wiringpi
import time
import threading

freq = 20.0
duty_right = 0.1
duty_left = 0.1

#define pins
speed_pin_right=13 #right_motor
dir1_right=5   #1 for forward
dir2_right=6   #1 for backward
speed_pin_left=12 #left_motor
dir1_left=16   #1 for backward
dir2_left=20   #1 for forward

direct_right = 1 #1 for forward
direct_left = 1 #1 for forward

wiringpi.wiringPiSetupGpio() 

def pwm_right():
    global duty_right,freq, speed_pin_right
    while(True):
        on_time = duty_right*(1.0/freq)
        off_time = (1.0-duty_right)*(1.0/freq)
        wiringpi.digitalWrite(speed_pin_right, 1)
        time.sleep(on_time)
        wiringpi.digitalWrite(speed_pin_right, 0)
        time.sleep(off_time)
def pwm_left():
    global duty_left,freq, speed_pin_left
    while(True):
        on_time = duty_left*(1.0/freq)
        off_time = (1.0-duty_left)*(1.0/freq)
        wiringpi.digitalWrite(speed_pin_left, 1)
        time.sleep(on_time)
        wiringpi.digitalWrite(speed_pin_left, 0)
        time.sleep(off_time)



def set_pins():
    global speed_pin_right, dir1_right, dir2_right, speed_pin_left, dir1_left, dir2_left
    wiringpi.pinMode(speed_pin_right, 1) #1 means output
    wiringpi.pinMode(dir1_right, 1)
    wiringpi.pinMode(dir2_right, 1)
    wiringpi.pinMode(speed_pin_left, 1)
    wiringpi.pinMode(dir1_left, 1)
    wiringpi.pinMode(dir2_left, 1)
    

def set_dir_left(): 
    global dir1_left, dir2_left, direct_left
    while(True):
        #1 if forward
        if(direct_left):
            wiringpi.digitalWrite(dir1_left, 0)
            wiringpi.digitalWrite(dir2_left, 1)
        else:
            wiringpi.digitalWrite(dir1_left, 1)
            wiringpi.digitalWrite(dir2_left, 0)


def set_dir_right(): 
    global dir1_right, dir2_right, direct_right
    while(True):
        #1 if forward
            if(direct_right):
                wiringpi.digitalWrite(dir1_right, 1)
                wiringpi.digitalWrite(dir2_right, 0)
            else:
                wiringpi.digitalWrite(dir1_right, 0)
                wiringpi.digitalWrite(dir2_right, 1)

def check():
    global duty_right, duty_left, direct_right, direct_left
    while(True):
        duty_right=0.8
        duty_left=0.2
        direct_right=1
        direct_left=1
        time.sleep(2)
        duty_right=0.2
        duty_left=0.8
        direct_right=0
        direct_left=0
        time.sleep(2)



set_pins()
right_motor = threading.Thread(target=pwm_right, args=())
direction_right = threading.Thread(target=set_dir_right, args=())
left_motor = threading.Thread(target=pwm_left, args=())
direction_left = threading.Thread(target=set_dir_left , args=())
check = threading.Thread(target=check, args=())

right_motor.start()
check.start()
direction_right.start()
left_motor.start()
direction_left.start()



    
        
