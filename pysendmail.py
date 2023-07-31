import smtplib, ssl


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "lab814reservatiosystem@gmail.com"  # Enter your address
receiver_email = "olivereddie1996.mg10@nycu.edu.tw"  # Enter receiver address
password = "elqskdpnokjjwzoi"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)