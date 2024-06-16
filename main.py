import os
import datetime
import time
import random
import logging
from pathlib import Path

from dotenv import load_dotenv
import slack
import schedule


logging.basicConfig(
    format='[%(asctime)s] :: %(levelname)s : %(message)s',
    encoding="utf-8",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler('kevin.log'),
        logging.StreamHandler()
        ]
)

logger = logging.getLogger(__name__)

try:
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)
    client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
    logger.info("load '.env'")
except:
    logger.error("'.env' or 'SLACK_TOKEN' not found")
    logger.info("stop kevin")
    quit()

topic = "XXX"
recipents = {
    "Alice": "XXX",
    "Bob": "XXX",
    "Charlie": "XXX",
    "David": "XXX",
    "Eve": "XXX",
    "Frank": "XXX"
}
messages = [
    "C'est l'heure de jouer au jardinier pour les plantes ! 🌿💧",
    "Les plantes te lancent un regard assoiffé - à toi de jouer ! 🌱💦",
    "Ne fais pas de chichis, les plantes t'attendent avec impatience ! 🌻🚿",
    "Les plantes ont un message pour toi : 'On a soif, s'il te plaît !' 🌵💧",
    "Les plantes ont besoin de toi pour une séance de rafraîchissement. 🌼💦",
    "Les plantes t'ont désigné comme leur héros de l'hydratation aujourd'hui ! 🌳💦",
    "C'est à toi de jouer au sorcier des plantes et de faire pleuvoir ! 🌱🌧️",
    "Les plantes pensent à toi - surtout à ton arrosoir ! 🌿💦",
    "Oublie les super-héros, aujourd'hui tu es le super-arroseur des plantes ! 🌸💧",
    "Les plantes sont en mode 'Thirsty Thursday' - à toi de jouer ! 🌵🥤",
]
hour = "09:15"

def choose_recipent():
    recipent = random.choice(list(recipents.keys()))
    recipent_id = recipents[recipent]
    logger.info(f"{recipent} is the future recipent")
    return recipent_id

def send_message():
    try:
        message = f"Salut <@{choose_recipent()}> !\n{random.choice(messages)}"
        client.chat_postMessage(channel=topic, text=message)
        logger.info("sending the message")
    except:
        logger.error("unable to send message")

month = datetime.datetime.now().month

if 3 <= month <= 8:
    schedule.every().day.at(hour).do(send_message)
else:
    schedule.every().day.at(hour).do(send_message)

#schedule.every().monday.at("12:40").do(job_1)
#schedule.every().tuesday.at("16:40").do(job_2)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)