import config
import requests
import time
import heroorganizer
import pyautogui as pgui

pgui.PAUSE = 0.2


# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates" ## use this to get the chat id
# print(requests.get(url).json())


def send_alert(message):
    url = f"https://api.telegram.org/bot{config.SETTINGS['token']}" \
          f"/sendMessage?chat_id={config.SETTINGS['chatId']}&text={message}"
    requests.get(url)


def run():
    findPhase = True
    while findPhase:
        print("Looking for game...")
        try:
            # banChoice = pgui.prompt('Who would you like to ban?')
            # heroChoice = pgui.prompt('Who would you like to play?')
            location = pgui.locateOnScreen('..\\images\\moonshard_accept.png', confidence=0.7)
            center = pgui.center(location)
            pgui.moveTo(center)
            pgui.leftClick()
            send_alert("Your game is ready")
            print("Game found!")
            findPhase = False
        except:
            time.sleep(5)

    # stage 2: loading/ban phase
    banPhase = True
    while banPhase:
        try:
            print()
            # pass ban phase image in, look for it
            # once found, do the math to locate the inputted ban hero
        except:
            print()


if __name__ == '__main__':
    # run()
    hero = 'Alchemist'
    x, y = heroorganizer.get_location(hero)
    attribute = heroorganizer.get_main_attr(hero)
    xMovement = 206 + (x * 58) + (x * 10)
    yMovement = 330 + (y * 100) + (y + 10)
    pgui.moveTo(xMovement, yMovement)


# strength: 206, 330
# agility: 1000, 330
# intelligence: 206, 710
# universal: 1000, 710
# 10px space
# width: 58px
# height: 100px
