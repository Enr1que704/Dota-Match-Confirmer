import pyautogui as pgui
import sys
pgui.PAUSE = 0.2

location = pgui.locateOnScreen('..\\images\\accept.png')
center = pgui.center(location)
pgui.moveTo(center)

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pgui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

