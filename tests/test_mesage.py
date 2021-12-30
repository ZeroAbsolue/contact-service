import smtplib

from ..src.Messenger import Messenger
# If you want to mock the mail sending, decomment the line above.
# from minimock import Mock


def test_message_send_mail():
    # If you want to mock the mail sending, decomment the two lines above.
    # smtplib.SMTP = Mock('smtplib.SMTP')
    # smtplib.SMTP.mock_returns = Mock('smtp_connection')
    messenger = Messenger('ianb@colorstudy.com',
                      'nkouekamwilfried@gmail.com', 'Test send mail function!', 'How is it going?')
    messenger.send_mail()
