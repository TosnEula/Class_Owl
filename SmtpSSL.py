import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465 #For SSL(secure socket layer)
smtp_server = "smtp.gmail.com" #smtp to send to gmail
sender_email = input("Please type in the sender's email: ")
receiver_email = input("Please type in the receiver's email: ")  
password = input("Type your password and press enter: ")

#Defining class information
classTest = ["math", "english","pych"]
status = ["open", "closed", "open"]
courses = 3

"""
#use this for formatting
htmlContent = <p style="font-size: 16px;"> {message} </p>
part = MIMEText(html_content, 'html') #converts to MIME text which handles the formatting
actualMsg.attach(part) #Combines the plain text and HTML

"""
tempMessage = ""

message = MIMEMultipart("alternative")
message["Subject"] =  "Subject: Class Status"

for course in range(courses):
    tempMessage += f"""\
Class: {classTest[course]}
status: {status[course]}
avaliable seats: /30 
        
"""


htmlContent = <p style="font-size: 16px;"> {tempMessage} </p>
part = MIMEText(html_content, 'html')
actualMsg.attach(part)


server = smtplib.SMTP(smtp_server, port)


#Defines security parameters and configurations
context = ssl.create_default_context() 

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
