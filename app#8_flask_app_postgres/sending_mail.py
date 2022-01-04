import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height, participants_count):
    from_email = 'hlapshun.v@gmail.com'
    from_password = 'Mivin777'
    to_email = email

    subject = 'Height data'
    message = f'Hey there, your height is supposed to be <strong>{height}</strong>. <br>'  \
              f'The average height is <strong>{average_height}</strong>. <br>' \
              f'Total participants: <strong>{participants_count}</strong>'

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
