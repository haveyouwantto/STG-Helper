import time

import keyboard
import mouse
import os
import math

def v3():
    posx,posy=mouse.get_position()
    lastx, lasty = mouse.get_position()
    angle = 0
    while True:
        if(keyboard.is_pressed('w') and keyboard.is_pressed('F8')):
            print("关闭")
            break

        currentx, currenty = mouse.get_position()

        distancex = currentx-lastx
        distancey = currenty-lasty

        dx = abs(currentx-lastx)/250
        dy = abs(currenty-lasty)/250
        timepause = (dx**2+dy**2)**(1/2)

        if(timepause > 0.1):
            timepause = 0.1

        if distancex != 0:

            angle = (math.atan(distancey/distancex)/math.pi*180)+90
            mouse.move(posx,posy)
            lastx,lasty=posx,posy
            currentx,currenty=posx,posy

            if(distancex < 0):
                angle = angle+180

        elif distancex == 0 and distancey > 0:

            angle = 180.0

        elif distancex == 0 and distancey < 0:
            angle = 0.0

        elif distancex == 0 and distancey == 0:
            angle = -1.0

        if(angle >= 337.5 or (angle < 22.5 and angle >= 0)):
            keyboard.press('up')
            time.sleep(timepause)
            keyboard.release('up')
        elif(angle >= 22.5 and angle < 67.5):
            keyboard.press('up')
            keyboard.press('right')
            time.sleep(timepause)
            keyboard.release('up')
            keyboard.release('right')
        elif(angle >= 67.5 and angle < 112.5):
            keyboard.press('right')
            time.sleep(timepause)
            keyboard.release('right')
        elif(angle >= 112.5 and angle < 157.5):
            keyboard.press('down')
            keyboard.press('right')
            time.sleep(timepause)
            keyboard.release('down')
            keyboard.release('right')
        elif(angle >= 157.5 and angle < 202.5):
            keyboard.press('down')
            time.sleep(timepause)
            keyboard.release('down')
        elif(angle >= 202.5 and angle < 247.5):
            keyboard.press('down')
            keyboard.press('left')
            time.sleep(timepause)
            keyboard.release('down')
            keyboard.release('left')
        elif(angle >= 247.5 and angle < 292.5):
            keyboard.press('left')
            time.sleep(timepause)
            keyboard.release('left')
        elif(angle >= 292.5 and angle < 337.5):
            keyboard.press('up')
            keyboard.press('left')
            time.sleep(timepause)
            keyboard.release('up')
            keyboard.release('left')


        lastx, lasty = currentx, currenty

def callback():
    os._exit(0)

string=r'''

   _____ _______ _____      _    _      _                 
  / ____|__   __/ ____|    | |  | |    | |                
 | (___    | | | |  __     | |__| | ___| |_ __   ___ _ __ 
  \___ \   | | | | |_ |    |  __  |/ _ \ | '_ \ / _ \ '__|
  ____) |  | | | |__| |    | |  | |  __/ | |_) |  __/ |   
 |_____/   |_|  \_____|    |_|  |_|\___|_| .__/ \___|_|   
                                         | |              
                                         |_|              


按 F8 + E 开启，按 F8 + W 关闭
'''

print(string)


while True:
    if(keyboard.is_pressed('e') and keyboard.is_pressed('F8')):
        print("开启")
        v3()
    time.sleep(0.001)