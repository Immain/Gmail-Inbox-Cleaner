<div align="center">
  <img src="https://i.pinimg.com/originals/23/da/b9/23dab92cbddac8b9ae00db6dd345644d.png" alt="Gmail Inbox Cleaner Logo" width="300" height="100">
</div>

# Gmail Inbox Cleaner

This Python script allows you to manage your Gmail inbox by deleting emails from specified senders and marking all unseen emails as read. It utilizes the `imaplib` and `email` libraries to interact with the Gmail IMAP server and `dotenv` to securely manage credentials.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

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

2. **Environment Variables**

   Create a `.env.local` file in the project root directory with the following content:

   ```
   EMAIL=your_email@gmail.com
   PASSWORD=your_app_password
   ```

   Replace `your_email@gmail.com` with your Gmail address and `your_app_password` with an app password generated for your Google account.

3. **Configure Senders**

   Edit the `senders` list in the script to include the email addresses from which you want to delete emails.

## Usage

Run the script using Python:
