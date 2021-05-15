#!/usr/bin/env python3
import imaplib
import smtplib
import yaml
import ssl
import time

CONFIG_FILE_PATH = 'config.yaml'

def ConfigLoader(requested_part):
    global CONFIG_FILE_PATH
    loaded_config = yaml.load(open(CONFIG_FILE_PATH, 'r'), Loader=yaml.FullLoader)
    for config_parts in loaded_config.items():
        if config_parts[0] == requested_part:
            return config_parts[1]

def sendMail(email_data, from_address, to_address):
    smtp_host = ConfigLoader('smtp')[0]['host']
    smtp_username = ConfigLoader('smtp')[0]['username']
    smtp_password = ConfigLoader('smtp')[0]['password']
    smtp_connection = smtplib.SMTP_SSL(smtp_host, 465, context=ssl.create_default_context())
    smtp_connection.login(smtp_username, smtp_password)
    smtp_connection.sendmail(from_address, to_address, email_data)

def GetNewMails():
    imap_host = ConfigLoader('imap')[0]['host']
    imap_username = ConfigLoader('imap')[0]['username']
    imap_password = ConfigLoader('imap')[0]['password']
    imap_connection = imaplib.IMAP4(imap_host)
    imap_connection.starttls(ssl_context=ssl.create_default_context())
    imap_connection.login(imap_username, imap_password)
    imap_connection.select('INBOX')
    while True:
        status, response = imap_connection.uid('search', None, '(UNSEEN)')
        unread_msg_nums = response[0].split()
        for mail_id in unread_msg_nums:
            status, response = imap_connection.uid('fetch', mail_id, '(RFC822)')
            mail_data = response[0][1]
            from_address = ConfigLoader('addresses')[0]['from']
            to_address = ConfigLoader('addresses')[0]['to']
            sendMail(mail_data, from_address, to_address)
            imap_connection.uid('store', mail_id, '+FLAGS', '\Seen')
        time.sleep(10)

def main():
    GetNewMails()

if __name__ == "__main__":
    main()
