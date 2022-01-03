# Description du projet
Ce projet est fait pour ëtre utilisé comme un service permettant d'envoyer des mails en SMTP

# Configuration
Pour pouvoir envoyer les mails il faut:
- Cloner le projet
- installer et pip
- puis taper les commandes:
    pip install flake8 pytest requests falcon virtualenv <br>
    pip3 install falcon<br>
    pip install python-decouple<br>

- Créer un fichier __.env__ à la racine du projet ou renommer le __.env.example__ en .env et le configurer
- Configurer le fichier .env en fonction du serveur SMTP choisi<br>
    APP_ENV = "development"<br>
    SMTP_USER=""<br>
    SMTP_PASSWORD=""<br>
    SMTP_HOST=""<br>
    SMTP_PORT=""<br>
- Lancer votre serveur en local waitress ou gunicorn et tester
  
# Test
Lancer le serveur waitress ou gunicorn
gunicorn --reload src.app
waitress-serve --port=8000 src.app:app

Pour tester exécuter la commande __pytest__<br>
Cette commande execute le test unitaire de la fonction send_email et les tests d'intégration sur la route post qui permet d'envoyer le mail. Pour tester la route, il faut que le serveur soit lancer sur le port 8000


En cas de problème avec la configuration en prod, vous pouvez consulter ce tutoriel qui nous a été d'une grande utilité
Utilise ce tutoriel pour servir l'application en production
https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04