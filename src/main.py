import config
import requests
import time

import pyautogui as pgui

pgui.PAUSE = 0.2


# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" ## use this to get the chat id
# print(requests.get(url).json())


def send_alert(message):
    url = f"https://api.telegram.org/bot{config.SETTINGS['token']}" \
          f"/sendMessage?chat_id={config.SETTINGS['chatId']}&text={message}"
    requests.get(url)


def run():
    go = True
    while go:
        time.sleep(5)
        try:
            location = pgui.locateOnScreen('..\\images\\moonshard_accept.png', confidence=0.7)
            center = pgui.center(location)
            pgui.moveTo(center)
            pgui.leftClick()
            send_alert("Your game is ready")
            print("Game found!")
            go = False
        except:
            print("Looking for game...")


if __name__ == '__main__':
    run()

