import smtplib

to = input("Enter the email address of the receiver;-")

message = input("Enter the message:-")

def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('kodlamahesabimdir@gmail.com', 'iudx xgph crkm dteb')
    server.sendmail('kodlamahesabimdir@gmail.com', to, message)
    server.close()


sendEmail(to, message)
