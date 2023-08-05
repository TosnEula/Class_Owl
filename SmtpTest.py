"""
python -m smtpd -c DebuggingServer -n localhost:1025
for starting local server
"""

import smtplib, ssl

port = 1025 #465 For SSL(secure socket layer)
smtp_server = "localhost" #"smtp.gmail.com" smtp to send to gmail
sender_email = "my@gmail.com" #input("Please type in the sender's email: ")
receiver_email = "your@gmail.com" #input("Please type in the receiver's email: ")  
#password = input("Type your password and press enter: ")

message = """\
Subject: Hi there

This message is sent from Python."""




server = smtplib.SMTP(smtp_server, port)
#server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()


#SSL email 
"""
#Defines security parameters and configurations
context = ssl.create_default_context() 

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
"""