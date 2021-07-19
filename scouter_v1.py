from djitellopy import tello
import keyboard as key
import cv2

drone = tello.Tello()
drone.connect()
drone.streamon()

print(drone.get_battery())

def getInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    x = 60 

    if key.is_pressed('left'): 
        lr = -x
    elif key.is_pressed('right'): 
        lr = x
    
    if key.is_pressed('up'): 
        ud = x
    elif key.is_pressed('down'): 
        ud = -x
    
    if key.is_pressed('w'): 
        fb = x
    elif key.is_pressed("s"): 
        fb = -x
    
    if key.is_pressed('a'): 
        yv = -x
    elif key.is_pressed('d'): 
        yv = x
        
    if key.is_pressed('t'):  
        drone.takeoff()
    elif key.is_pressed('l'): 
        drone.land()
        
    return [lr, fb, ud, yv]

while True:
    val = getInput()
    drone.send_rc_control(val[0], val[1], val[2], val[3])
    frame = drone.get_frame_read().frame
    cv2.imshow("Live Stream", frame)
    cv2.waitKey(1)
