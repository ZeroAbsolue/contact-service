import falcon

from .MessageRessource import MessageRessource

app=application =  falcon.App()
sended_mail = MessageRessource()

app.add_route('/send_mail',sended_mail)