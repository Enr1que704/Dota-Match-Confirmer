import pyautogui as pgui
import sys, time
pgui.PAUSE = 0.2


go = True
while go:
    time.sleep(5)
    try:
        location = pgui.locateOnScreen('..\\images\\moonshard_accept.png', confidence=0.7)
        center = pgui.center(location)
        pgui.moveTo(center)
        pgui.leftClick()
        go = False
    except:
        print("Accept button not found, trying again")



# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pgui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

