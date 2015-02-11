import smtplib

fromaddr = 'kevyg123@gmail.com'
toaddr = 'kevyg123@gmail.com'
toname = 'kevy'
fromname= 'kevy'
subject = 'GAZA'
msg = 'gg'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'kevyg123@gmail.com'

password = 'ceoyvgipsirwanti'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()