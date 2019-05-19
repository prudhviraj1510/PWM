import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

led = 11
GPIO.setup(led, GPIO.OUT)
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 25
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def checkdist():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

pwm = GPIO.PWM(led, 80)



pwm.start(0)
 
#if __name__ == '__main__':
try:
    while True:
        dist = checkdist()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)
        if 45<checkdist()<50:
            pwm.ChangeDutyCycle(10)
        elif 40<checkdist()<45:
            pwm.ChangeDutyCycle(20)
        elif 35<checkdist()<40:
            pwm.ChangeDutyCycle(30)
        elif 30<checkdist()<35:
            pwm.ChangeDutyCycle(40)
        elif 25<checkdist()<30:
            pwm.ChangeDutyCycle(60)
        elif 20<checkdist()<25:
            pwm.ChangeDutyCycle(70)
        elif 15<checkdist()<20:
            pwm.ChangeDutyCycle(80)
        elif 10<checkdist()<15:
            pwm.ChangeDutyCycle(90)
        elif 5<checkdist()<10:
            pwm.ChangeDutyCycle(100)
        else:
            pwm.ChangeDutyCycle(0)
        
        
    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    #time.sleep(1)
pwm.stop()

GPIO.cleanup()        

        
