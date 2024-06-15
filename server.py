import smtplib
import csv
from email.message import EmailMessage


def sendMail(subject,sender,receiver_name,receiver_mail,message_to_receiver,sender_password,smtp_server,smtp_port):
    # create the email message
    msg = EmailMessage()

    # set the sender's email
    msg['From'] = sender

    # set the receiver's email
    msg['To'] = receiver_mail

    # set the email's subject
    msg['Subject'] = subject

    # set the email's body
    msg.set_content(message_to_receiver)
    try:
        # connect to the smtp server
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            #start TLS for security
            server.starttls()

            # login to the server
            server.login(sender,sender_password)

            # send the email to recipients
            server.sendmail(sender,receiver_mail,msg.as_string())

        print(f"Email sent to {receiver_name} successfully")

    except Exception as e:
        print(f"failed to send email. Error: {str(e)}")

def load_email_details_from_csv(csv_file):
    email_details = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email_details.append(row)
    return email_details


smtp_server = "smtp.gmail.com"
smtp_port = 587 #for starttls ()
sender = input("enter your  email: ")
sender_password = input("enter your password: ")
subject = "Greetings"
csv_file = "recipients.csv"

recipient_details = load_email_details_from_csv(csv_file)

for detail in recipient_details:
    sendMail(subject,sender,detail["name"],detail["receiver"],detail["message"],sender_password,smtp_server,smtp_port)