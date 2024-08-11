import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv('.env.local')

# Your email address and password
email = os.getenv('EMAIL')
pwd = os.getenv('PASSWORD')

# IMAP server for Gmail
imapserver = 'imap.gmail.com'

def deleteEmail(mail, senders):
    mail.select('inbox')

    for sender in senders:
        typ, data = mail.search(None, f'FROM "{sender}"')
        for num in data[0].split():
            mail.store(num, '+FLAGS', r'(\Deleted)')
        print(f"Deleted emails from {sender}")

    mail.expunge()

def markAllAsRead(mail):
    mail.select('inbox')

    typ, data = mail.search(None, 'UNSEEN')
    for num in data[0].split():
        mail.store(num, '+FLAGS', r'(\Seen)')
    
    print("Marked all messages as read")

# List of senders to delete emails from
senders = ["", "", "",]

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imapserver)
mail.login(email, pwd)
print(f"Logged in as {email}")

# Run both functions
deleteEmail(mail, senders)
markAllAsRead(mail)

# Close the connection and log out
mail.close()
mail.logout()
print("Logged out and closed the connection.")
