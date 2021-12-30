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
  