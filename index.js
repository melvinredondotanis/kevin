const { App } = require('@slack/bolt');
const dotenv = require('dotenv');
const schedule = require('node-schedule');
const fs = require('fs');

dotenv.config();

const studentsAlreadyPassed = [];
const logger = fs.createWriteStream('kevin.log', { flags: 'a' });

const app = new App({
    token: process.env.SLACK_TOKEN,
    signingSecret: process.env.SLACK_SIGNING_SECRET
});

const topic = 'C07S58L52G0';
const recipients = {
    // 'nom': 'id',
};

const messages = [
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
];
const hour = '09:15';

function chooseRecipient() {
    if (studentsAlreadyPassed.length === Object.keys(recipients).length) {
        studentsAlreadyPassed.length = 0;
    }

    let recipient;
    do {
        const keys = Object.keys(recipients);
        recipient = keys[Math.floor(Math.random() * keys.length)];
    } while (studentsAlreadyPassed.includes(recipient));

    studentsAlreadyPassed.push(recipient);
    const recipientId = recipients[recipient];
    logger.write(`[INFO] ${recipient} a été sélectionné pour arroser les plantes\n`);

    return recipientId;
}

async function sendMessage() {
    const message = `Salut <@${chooseRecipient()}> !\n${messages[Math.floor(Math.random() * messages.length)]}\nPour savoir quelles plantes doivent être arrosées aujourd'hui, consulte la fiche de renseignement dans les locaux.`;
    try {
        await app.client.chat.postMessage({
            channel: topic,
            text: message,
        });
        logger.write(`[INFO] Message envoyé dans le canal\n`);
    } catch (error) {
        console.error('Erreur lors de l\'envoi du message:', error);
        logger.write(`[ERROR] Impossible d'envoyer le message: ${error.message}\n`);
    }
}

function scheduleMessages() {
    const now = new Date();
    const month = now.getMonth() + 1;

    const daysToSchedule = (month >= 3 && month <= 8) ? ['Tuesday', 'Wednesday', 'Thursday'] : ['Wednesday'];
    daysToSchedule.forEach(day => {
        schedule.scheduleJob({ hour: 9, minute: 15, dayOfWeek: getDayIndex(day) }, sendMessage);
    });
}

function getDayIndex(dayName) {
    return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'].indexOf(dayName);
}

(async () => {
    await app.start(process.env.PORT || 3000);
    logger.write(`[INFO] ⚡️ Rework Kevin est en cours d'exécution !\n`);
    scheduleMessages();
})();
