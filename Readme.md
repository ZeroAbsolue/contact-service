# Description du projet
Ce projet est fait pour ëtre utilisé comme un service permettant d'envoyer des mails en SMTP

# Configuration
Pour pouvoir envoyer les mails il faut:
- Créer un fichier __.env__ à la racine du projet ou renommer le __.env.example__ en .env et le configurer
- Configurer le fichier .env en fonction du serveur SMTP choisi<br>
    APP_ENV = "development"<br>
    SMTP_USER=""<br>
    SMTP_PASSWORD=""<br>
    SMTP_HOST=""<br>
    SMTP_PORT=""<br>
- Lancer votre serveur en local waitress ou gunicorn et tester
  
# Test
Pour tester, exécuter la commande __pytests -s__<br>
Cette commande execute le test unitaire de la fonction send_email et les tests d'intégration sur la route post qui permet d'envoyer le mail
  

# Configuration en prod
Cloner le projet
installe et pip
puis taper pip install flake8 pytest requests falcon virtualenv 
pip3 install falcon
pip install python-decouple

Utilise ce tutoriel pour servir l'application en production
https://www.digitalocean.com/community/tutorials/how-to-deploy-falcon-web-applications-with-gunicorn-and-nginx-on-ubuntu-16-04