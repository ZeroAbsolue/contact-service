# Description du projet
Ce projet est fait pour ëtre utilisé comme un service permettant d'envoyer des mails en SMTP

# Configuration
Pour pouvoir envoyer les mails il faut:
- Créer un fichier __.env__ à la racine du projet
- Configurer le fichier .env en fonction du serveur SMTP choisi
    APP_ENV = "development"
    SMTP_USER=""
    SMTP_PASSWORD=""
    SMTP_HOST=""
    SMTP_PORT=""
- Lancer votre serveur en local waitress ou gunicorn et tester
  
# Test
Pour tester, exécuter la commande __pytests -s__
Cette commande execute le test unitaire de la fonction send_email et les tests d'intégration sur la route post qui permet d'envoyer le mail
  