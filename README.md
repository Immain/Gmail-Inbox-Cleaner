# Gmail Inbox Cleaner

This Python script allows you to manage your Gmail inbox by deleting emails from specified senders and marking all unseen emails as read. It utilizes the `imaplib` and `email` libraries to interact with the Gmail IMAP server and `dotenv` to securely manage credentials.

## Features

- **Delete Emails from Specific Senders**: Remove all emails from a list of specified senders.
- **Mark All Unseen Emails as Read**: Update the status of all unread emails to read.

## Requirements

- Python 3.10 or greater
- `imaplib` (Standard Library)
- `email` (Standard Library)
- `python-dotenv` (To load environment variables)

## Setup

1. **Install Dependencies**

   Ensure you have the required Python packages. You can install `python-dotenv` using pip:

   ```bash
   pip install python-dotenv
   ```
