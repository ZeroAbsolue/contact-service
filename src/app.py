import falcon

from .MessengerRessource import MessengerRessource

app=application =  falcon.App()
sended_mail = MessengerRessource()

app.add_route('/send_mail',sended_mail)