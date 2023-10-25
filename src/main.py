import pyautogui as pgui
import sys, time, smtplib, requests
from email.message import EmailMessage

TOKEN = '6442084061:AAHszPjHDUr3Ssvm5gs2Nrz9-zQU9E46WEQ'  # bot token
chat_id = 6576780272
pgui.PAUSE = 0.2


# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" ## use this to get the chat id
# print(requests.get(url).json())


def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)


go = True
while go:
    time.sleep(5)
    try:
        location = pgui.locateOnScreen('..\\images\\moonshard_accept.png', confidence=0.7)
        center = pgui.center(location)
        pgui.moveTo(center)
        pgui.leftClick()
        send_alert("Your game is ready")
        go = False
    except:
        print("Accept button not found, trying again")






