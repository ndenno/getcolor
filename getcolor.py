# A program to get the RGB color value of the current mouse position
#**Note** DO NOT run in IDLE, as it doesn't print backslash characters

import pyautogui as p

def getColor():
    '''Gets the RGB color value of the current mouse position'''
    try:
        while True:
            x, y = p.position()
            r, g, b = p.pixel(x,y)

            #The .rjust on the next line is necessary for the last digits to diplay properly
            # while using the backslash character in the second print() command
            s = "RGB color value of current mouse position: " + str(r).rjust(3) + ", " + str(g).rjust(3) + ", " + str(b).rjust(3) 
            print(s, end='') 
            print('\b'*len(s), end = '', flush=True) 

    except KeyboardInterrupt:
        print('\nFinished')

getColor()

