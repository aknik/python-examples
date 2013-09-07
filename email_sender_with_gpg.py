import smtplib
import gnupg
to = ""  #insert reciever's email id here
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
#set location of  gpg keys
gpg=gnupg.GPG(gnupghome="/path/to/.gnupg/")
gpg.encoding='utf-8'
#fetch the keys
pub_keys = gpg.list_keys()
#removing other data from keys info fetched, need only fingerprint and email
#thanks to sant0sh for helping me figure out how to do this
new={}
for i in pub_keys:
     new.update({i['uids'][0]:i['fingerprint']})
#TODO : insert logic for selecting which key to use, for now use some key
#encrypt the message body
enc = gpg.encrypt(body,new["insert key uid here"])
#add the header
msg = head + enc
#send the mail
smtpserver.sendmail(user_name,to,msg)
print "done!!"
smtpserver.close()


