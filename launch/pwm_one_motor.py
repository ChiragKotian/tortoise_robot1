import wiringpi
import time

freq = 15.0
duty = 0.1

speed_pin_right=13 #right_motor
dir1_right=5   #1 for forward
dir2_right=6   #1 for backward
speed_pin_left=12 #left_motor
dir1_left=16   #1 for backward
dir2_left=20   #1 for forward


wiringpi.wiringPiSetupGpio() 

def pwm(duty, freq, pin):

    on_time = duty*(1.0/freq)
    off_time = (1.0-duty)*(1.0/freq)
    wiringpi.digitalWrite(pin, 1)
    time.sleep(on_time)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(off_time)

def set_pins():
    global speed_pin_right, dir1_right, dir2_right, speed_pin_left, dir1_left, dir2_left
    wiringpi.pinMode(speed_pin_right, 1) #1 means output
    wiringpi.pinMode(dir1_right, 1)
    wiringpi.pinMode(dir2_right, 1)
    wiringpi.pinMode(speed_pin_left, 1)
    wiringpi.pinMode(dir1_left, 1)
    wiringpi.pinMode(dir2_left, 1)
    

def set_dir(wheel, dir): 
    global dir1_right, dir2_right, dir1_left, dir2_left
    if(wheel): #1 is left, 1 if forward
        if(dir):
            wiringpi.digitalWrite(dir1_left, 0)
            wiringpi.digitalWrite(dir2_left, 1)
        else:
            wiringpi.digitalWrite(dir1_left, 1)
            wiringpi.digitalWrite(dir2_left, 0)
    else:
        if(dir):
            wiringpi.digitalWrite(dir1_right, 1)
            wiringpi.digitalWrite(dir2_right, 0)
        else:
            wiringpi.digitalWrite(dir1_right, 0)
            wiringpi.digitalWrite(dir2_right, 1)
    



 
while(True):
    set_dir(0,1)
    pwm(duty,freq,speed_pin_right)
