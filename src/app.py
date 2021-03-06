import falcon

from .MessengerRessource import MessengerRessource

app=application =  falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='*'))
sended_mail = MessengerRessource()

app.add_route('/api/send_mail',sended_mail)