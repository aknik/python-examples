import smtplib
import gnupg

to = "user@8chan.co"  #insert reciever's email id here
user_name = "user@gmail.com" #insert your email id here
appcode = "password" #insert google app code here or you gmail password

smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(user_name,appcode)
subject = "gnupg" #insert subject here
head = 'To:'+to+'\nFrom: '+user_name+'\nSubject : '+subject+'\n'
body = "cuerpo del mensaje" #inser message body here

#set location of  gpg keys
gpg=gnupg.GPG(homedir="~/.gnupg/")
gpg.encoding='utf-8'

#fetch the keys
pub_keys = gpg.list_keys()

for i in pub_keys:
# Busca el email TO dentro de i['uids'][0]     
     if to in i['uids'][0]: 
         print (i['uids'][0],i['fingerprint'])
         fingerprint = i['fingerprint']

#encrypt the message body
enc = gpg.encrypt(body,fingerprint)
encrypted_body = str(enc)

#add the header
msg = head + encrypted_body
#send the mail
smtpserver.sendmail(user_name,to,msg)
print (encrypted_body)
smtpserver.close()

