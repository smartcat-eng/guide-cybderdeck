from machine import ADC, Pin
import time
import usb.device
from usb.device.mouse import MouseInterface

mouse = MouseInterface()
usb.device.get().init(mouse, builtin_driver=True)

xPin = Pin(26)
vX = ADC(xPin)
yPin = Pin(27)
vY = ADC(yPin)

clickL = Pin(2, Pin.IN, Pin.PULL_UP)
clickR = Pin(7, Pin.IN, Pin.PULL_UP)
print(clickL.value())

deadzones = [.1, .25, .4]
sensitivity = 3
speedX = 0
speedY = 0

def findSpeed(value):
    if abs(value) >= deadzones[2]:
        return 3 * (value/ abs(value))
    elif abs(value) >= deadzones[1]:
        return 2 * (value/ abs(value))
    elif abs(value) >= deadzones[0]:
        return 1 * (value/ abs(value))
    elif abs(value) < deadzones[0]:
        return 0

while not mouse.is_open():
    time.sleep_ms(100)

while True:
    press = False
    if(clickL.value() == 0):
        press = True
    
    xValue = (vX.read_u16() / 65536) - .5
    yValue = (vY.read_u16() / 65536) - .5
    
        
    speedX = int(findSpeed(xValue)) * sensitivity
    speedY = int(findSpeed(yValue)) * -sensitivity

    mouse.move_by(speedX, speed
    mouse.click_left(press)
    time.sleep_ms(5)
