import wiringpi
import time

freq = 10000.0
duty = 0.5

speed_pin_right=13
dir1_right=5   #1 for forward
dir2_right=6   #1 for backward
speed_pin_left=12
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
    wiringpi.pinMode(speed_pin_right, 1)
    

def set_dir(wheel, dir):
    if(wheel):
        wheel = true



 

wiringpi.pinMode(16, 1)       
wiringpi.digitalWrite(16, 0) 
wiringpi.pinMode(20, 1)       
wiringpi.digitalWrite(20, 1) 
wiringpi.pinMode(12, 1)       # Set pin 6 to 1 ( OUTPUT )
wiringpi.digitalWrite(12, 1) 
print("high")
time.sleep(5)
wiringpi.digitalWrite(6, 0) 
wiringpi.digitalWrite(13, 0)
wiringpi.digitalWrite(5, 0)
wiringpi.digitalWrite(16, 0)
wiringpi.digitalWrite(20, 0)
wiringpi.digitalWrite(12, 0)
print("low")