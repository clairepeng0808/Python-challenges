import smtplib
from email.message import EmailMessage
from string import Template  # use .substitute()
from pathlib import Path  # alternative: import os
import config

html = Template(Path('content.html').read_text())

email = EmailMessage()
email['from'] = config.SENDER_EMAIL
email['to'] = config.RECIPIENT_EMAIL
email['subject'] = 'Email Subject'

# content: text, images, html...
email.set_content(html.substitute({'name': config.NAME}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587,) as smtp:
    smtp.ehlo()  # hello message
    smtp.starttls()  # encryption
    smtp.login(config.EMAIL, config.EMAIL_PWD)
    smtp.send_message(email)
    print('All good!')
