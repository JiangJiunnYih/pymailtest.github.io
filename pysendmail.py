import smtplib
import ssl

def send_email(sender_email, sender_password, receiver_email, subject, body):
    port = 465
    smtp_server = "smtp.gmail.com"

    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()

    server = None

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        server.quit()

# Example usage:
sender_email = "lab814reservatiosystem@gmail.com"
receiver_email = "olivereddie1996.mg10@nycu.edu.tw"
sender_password = "elqskdpnokjjwzoi"
subject = "Test Email"
body = "This is a test email sent using Python."

send_email(sender_email, sender_password, receiver_email, subject, body)
