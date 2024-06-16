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
    "Les feuilles te saluent bien bas et te demandent une petite gorgée. 🌿🍶",
    "Les racines t'appellent en urgence : 'H2O requis !' 🌱💧",
    "Les plantes ont une requête spéciale : de l'eau fraîche et pure. 🌻💦",
    "Les fleurs ont soif d'amour et d'eau fraîche - à toi de jouer ! 🌼💧",
    "Il est temps de transformer ton jardin en oasis. 🌿💧",
    "Les plantes te supplient : 'Pas de sécheresse aujourd'hui, s'il te plaît !' 🌵💦",
    "Les plantes t'attendent pour une danse de la pluie improvisée ! 🌳🌧️",
    "Les bourgeons t'envoient des ondes positives - avec une petite demande d'arrosage. 🌸💦",
    "Les plantes te regardent avec des yeux pétillants d'espoir ! 🌼💧",
    "Les plantes murmurent : 'Une gorgée de plus et nous serons heureuses !' 🌿💦",
    "Les feuilles frémissent à l'idée de recevoir de l'eau - c'est à toi de jouer ! 🌱💧",
    "Les plantes organisent une fête de l'eau - et tu es l'invité d'honneur ! 🌻💧",
    "Les tiges te tendent les bras pour une pluie bienfaisante. 🌿🌧️",
    "Les plantes te disent : 'Merci d'avance pour ce rafraîchissement tant attendu !' 🌳💦",
    "Les fleurs t'offrent leurs plus beaux pétales en échange d'un peu d'eau. 🌼💧",
    "Les plantes rêvent d'une douche rafraîchissante - fais leur ce plaisir ! 🌿🚿",
    "Les racines chantent 'Sous la pluie' - aide-les à réaliser leur rêve ! 🌱🌧️",
    "Les plantes se languissent de ton arrosoir magique. 🌿💧",
    "Les bourgeons sont prêts à éclore, juste une goutte d'eau de plus ! 🌸💦",
    "Les plantes préparent une symphonie de gratitude pour ton prochain arrosage. 🌿🎶💧"
]
hour = "09:15"

def choose_recipent():
    recipent = random.choice(list(recipents.keys()))
    recipent_id = recipents[recipent]
    logger.info(f"{recipent} is the future recipent")
    return recipent_id

def send_message():
    try:
        message = f"Salut <@{choose_recipent()}> !\n{random.choice(messages)}\nPour savoir quelles plantes doivent être arrosées aujourd'hui, consulte la fiche de renseignement dans les locaux. Si tu es absent aujourd'hui, demande à quelqu'un de le faire à ta place."
        client.chat_postMessage(channel=topic, text=message)
        logger.info("sending the message")
    except:
        logger.error("unable to send message")

month = datetime.datetime.now().month

if 3 <= month <= 8:
    schedule.every().tuesday.at(hour).do(send_message)
    schedule.every().wednesday.at(hour).do(send_message)
    schedule.every().thursday.at(hour).do(send_message)
else:
    schedule.every().wednesday.at(hour).do(send_message)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)