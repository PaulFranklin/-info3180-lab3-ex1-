import smtplib

from_name = 'Paul'
from_addr = 'yourusername@gmail.com'
to_name='Stefan'
to_addr = 'pscf-jr@hotmail.com'
subject = 'Info 3180 lab 3 email test'
message = """From: {} <{}>
To: {} <{}> 

Subject: Email Test
You are the man Paul.Great things are ahead of you.
"""
message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, message)
# Credentials (if needed)
username = 'yourusername@gmail.com'
password = '{youremailapppassword}' 
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
