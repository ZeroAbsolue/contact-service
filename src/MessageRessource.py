import falcon
import json
from .Messenger import Messenger


class MessageRessource:
    def on_post(self, req, resp):
        sender = req.media.get('sender')
        receiver = req.media.get('receiver')
        subject = req.media.get('subject')
        message = req.media.get('message')

        messenger = Messenger(sender, receiver, subject, message)
        try:
            messenger.send_mail()
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({"message": "Succes"})
            return resp

        except Exception as catch_exception:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({catch_exception})
            return resp
