#!/usr/bin/env python3.7

"""
Handles Gmail auth and api calls
"""
import base64
from email.message import EmailMessage
import os.path
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def gmail_send_message(content,email):
    """Create and send an email message, 
    content is the email messege and email is the address that gets the email.
    Returns: Message object, including message id
    """
    api_scopes = ['https://www.googleapis.com/auth/gmail.send']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', api_scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        #If token has expired it gets refreshed so no further login are needed
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'cred.json', api_scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w',encoding="UTF-8") as token:
            token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content(content)

        message['To'] = f'{email}'
        message['From'] = 'msurvey203@gmail.com'
        message['Subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message
