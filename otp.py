import random
import smtplib
from email.message import EmailMessage

# Generate a otp
otp=""
for i in range(6):
    otp+=str(random.randint(0,9))

# Send the otp to the user
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
from_mail = 'garvitakesharwani22@gmail.com'
server.login('your_email@gmail.com','your_app_password')
to_mail = input("Enter your email: ")
msg = EmailMessage()
msg['Subject'] = "OTP Verification"
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content("Your OTP is: "+otp)
server.send_message(msg)

# Verification of the OTP
a = input("Provide with the OTP you received : ")
if a == otp:
    print("Correct! OTP Verified")
else:
    print("Incorrect! Wrong OTP")




