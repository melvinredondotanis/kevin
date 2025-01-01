# Kévin

> [!CAUTION]
> The project continue on: <a href="https://github.com/melvinredondotanis/Bobby">Bobby</a>

<img src="img/kevin.webp" alt="Image de plante chère" width="150" height="auto">

Kévin est un bot Slack conçu pour le campus Holberton de Fréjus, qui vous rappelle quand il est temps d'arroser vos plantes.

---

### Exemple

<img src="img/example.png" alt="Image de plante chère" width="500" height="auto">

---

### Installation

**Linux**

1. Cloner le dépôt
```bash
cd ~
git clone https://github.com/melvinredondotanis/kevin
```

2. Créer un environnement

> Pensez bien à entrer vos informations dans le fichier ```kevin.service```
```bash
mkdir .kevin && cp kevin/main.py .kevin
echo "SLACK_TOKEN=your_token" > .kevin/.env
sudo cp kevin/kevin.service /etc/systemd/system
cd .kevin
python3 -m venv env
source env/bin/activate
pip install -r ../kevin/requirements.txt
deactivate
cd ~ && rm -rf kevin
```

3. Activer le service
```bash
sudo systemctl daemon-reload
sudo systemctl start kevin.service
sudo systemctl enable kevin.service
```
