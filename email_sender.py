import smtplib
to = "" #insert reciever's email id here
user_name = "" #insert your email id here
appcode = "" #insert google app code here or you gmail password
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user_name,appcode)
subject = "" #insert subject here
head = 'To:'+to+'\nFrom: '+user_name+'\nSubject : '+subject+'\n'
body = "" #inser message body here
msg = head + body
smtpserver.sendmail(user_name,to,msg)
print "done!!"
smtpserver.close()

