import pyautogui as pgui
import sys, time
import requests
pgui.PAUSE = 0.2

EMAIL = "enriquescodeproject@gmail.com"
PASSWORD = "codeproject"


# go = True
# while go:
#     time.sleep(5)
#     try:
#         location = pgui.locateOnScreen('..\\images\\moonshard_accept.png', confidence=0.7)
#         center = pgui.center(location)
#         pgui.moveTo(center)
#         pgui.leftClick()
#         go = False
#     except:
#         print("Accept button not found, trying again")
#







# send discord notifications (too bad it doesn't play nice with being idle and sending them on your phone

# payload = {
#     'content': "Your game is ready"
# }
#
# header = {
#     'authorization': 'MTE2NjI1MjU4NzIyNjQ5NzExNA.Gzsf0d.M-StBu1hIbdvdMOXDyogKA7BzHg1iXqiMTwyfU', ## get this from the network tab header
#     'content-type': 'application/json'
# }
#
# r = requests.post("https://discord.com/api/v9/channels/1166250272499187712/messages", json=payload, headers=header)