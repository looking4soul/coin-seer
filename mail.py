#!/usr/bin/python
#-*- coding:utf-8 –*-

from email.mime.text import MIMEText
import smtplib

class Mail(object):
    def __init__(self, accountName, password, smtpServer, smtpPort = 25):
        self.accountName = accountName
        self.password = password
        self.smtpServer = smtpServer
        self.smtpPort = smtpPort

    def sendText(self, fromAddr, toAddrs, message):
        messageObject = MIMEText(message, 'plain', 'utf-8')
        messageObject["From"] = "coin-seer %s" % fromAddr
        messageObject["Subject"] = "Coin price report"
        server = smtplib.SMTP(self.smtpServer, self.smtpPort)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.set_debuglevel(1)
        server.login(self.accountName, self.password)
        server.sendmail(fromAddr, toAddrs, messageObject.as_string())
        server.quit()


