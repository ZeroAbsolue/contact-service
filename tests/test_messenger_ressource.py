import requests
import falcon

def test_messenger_ressource_post():
    payload = {
        'sender': 'ianb@colorstudy.com',
        'receiver': 'nkouekamwilfried@gmail.com',
        'subject': 'Test api function',
        'message': 'How is it going?'}
    response = requests.post('http://localhost:8000/send_mail',json=payload)
    assert response.status_code == 200
    assert response.json()['message'] == 'Succes'
