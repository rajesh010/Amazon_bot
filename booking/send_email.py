import smtplib
from email.message import EmailMessage
import os



class SendEmail:

  def send_email( subject='check the picture', receiver_email = 'rajesh.gautam010@gmail.com', message= 'check the attachments'):
   email = os.environ.get('EMAIL')
   password = os.environ.get('PASSWORD_GMAIL')

   msg = EmailMessage()
   msg['Subject'] = subject     #adding the subject in the email
   msg.set_content(message)
   msg['From'] = email      #sender email address i.e me
   msg['To'] = receiver_email        # receiver email address
   

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:   #using SSL class to omit some extra lines
    smtp.login(email , password) 
    smtp.send_message(msg)     #giving msg as an argument and sending it

    smtp.quit()    