import wiringpi
import time

freq = 10000.0
duty = 0.5



def pwm(duty, freq, pin):

    on_time = duty*(1.0/freq)
    off_time = (1.0-duty)*(1.0/freq)
    wiringpi.digitalWrite(pin, 1)
    time.sleep(on_time)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(off_time)


wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(13, 1)       
wiringpi.digitalWrite(13, 1) 
wiringpi.pinMode(5, 1)       
wiringpi.digitalWrite(5, 1) 
wiringpi.pinMode(6, 1)       
wiringpi.digitalWrite(6, 0) 
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