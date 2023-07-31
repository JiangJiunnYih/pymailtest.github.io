import smtplib, ssl
                    
port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "lab814reservatiosystem@gmail.com"
receiver_email = "olivereddie1996.mg10@nycu.edu.tw"
password = "elqskdpnokjjwzoi"
message = """\
            Subject: Hi there

            This message is sent from Python."""

context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Mail send Successed")
except:
        print("Mail send failed")
