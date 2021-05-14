#!/usr/bin/python
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(16, True)

#iemand anders 500
p = GPIO.PWM(16, 35000)

def SpinMotor(direction, num_steps):
    p.ChangeFrequency(35000)
    GPIO.output(18, direction)
    while num_steps > 0:
        p.start(1)
        time.sleep(0.1)
        num_steps -= 1
    p.stop()
    return True

SpinMotor(True,10)
time.sleep(.2)
SpinMotor2(False,10)


#direction_input = input('Please enter direction:')
#num_steps = int(input('Please enter the number of steps: '))
#while(
#if direction_input in ['right','r']:
    #SpinMotor(False, num_steps)
    #p.stop()
    #SpinMotor(True, num_steps)
    
#elif direction_input in ['left','l']:
    #SpinMotor(True, num_steps)

#num_steps=0
