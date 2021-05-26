  import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


def sendMail():
    message = Mail(
    from_email='team@acenmark.co.uk',
    to_emails='ayanshaikh7187@gmail.com',
    subject='Testing Integration',
    html_content='<strong>i will be fucking rich</strong>')
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def SendDynamic(from_email, to_email, template_id, dynamic_data):
    """ Send a dynamic email to a list of email addresses

    :returns API response code
    :raises Exception e: raises an exception """
    # create Mail object and populate
    message = Mail(
        from_email=from_email,
        to_emails=to_email)
    # pass custom values for our HTML placeholders
    message.dynamic_template_data = dynamic_data
    message.template_id = template_id
    # create our sendgrid client object, pass it our key, then send and return our response objects
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        response = 500
    return response.status_code