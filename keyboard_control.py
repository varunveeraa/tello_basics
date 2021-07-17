from djitellopy import tello
from time import sleep
import keyboard as key

drone = tello.Tello()
drone.connect()

print(drone.get_battery())

def getInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    if key.is_pressed('left'): 
        lr = -50
    elif key.is_pressed('right'): 
        lr = 50
    
    if key.is_pressed('up'): 
        ud = 50
    elif key.is_pressed('down'): 
        ud = -50
    
    if key.is_pressed('w'): 
        fb = 50
    elif key.is_pressed("s"): 
        fb = -50
    
    if key.is_pressed('a'): 
        yv = -50
    elif key.is_pressed('d'): 
        yv = 50
        
    if key.is_pressed('t'):  
        drone.takeoff()
    elif key.is_pressed('l'): 
        drone.land()
        
    return [lr, fb, ud, yv]

while True:
    val = getInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])
    sleep(0.05)
