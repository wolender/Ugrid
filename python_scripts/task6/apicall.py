#!/usr/bin/env python3

"""
Practical tasks (Part 2)

Create a script that uses the Survey Monkey (https://www.surveymonkey.com) service,
creates a survey, and sends an invitation to go through it.


PREREQUISITES:

Sign up at https://www.surveymonkey.com 

Create a draft application at https://developer.surveymonkey.com   

No need to deploy your application.
It's just for testing. Do not forget to set permissions for your application.

After creating a draft application you will obtain an ACCESS_TOKEN,
which is needed to do API requests from your script.


REQUIREMENTS:

The script should accept a JSON file with questions for the survey,
and a text file with a list of email addresses.

The structure of a JSON file with questions:

{

   "Survey_Name": {

      "Page_Name": {

          "Question1_Name": {

              "Description" : "Description of question",

              "Answers" : [

                  "Answer1",

                  "Answer2",

                  "Answer3"

              ]

          },

          "Question2_Name": {

              "Description" : "Description of question",

              "Answers" : [

                  "Answer1",

                  "Answer2",

                  "Answer3"

              ]

          }

          . . .

      }

   }

}

There should be at least 3 questions and 2 recipients.
"""

from email.message import EmailMessage
import requests
import json
from googleapiclient.discovery import build
import base64
from google_auth_oauthlib.flow import InstalledAppFlow


ACCESS_TOKEN="cMFftolwVdUKH2zJtk2zDOMeAKkYgQk3RxT7usJRmmEjnrLw8YQ52QIhm7OhjibN.Mz86CNoWe1tq06i52S982BC5bqZrzuIykpxGsAxAa2vsOUmnD3vqJUJwObv4ten"



def send_invitations(messege_string):
  SCOPES = ['https://www.googleapis.com/auth/gmail.send']
  

  # Create the flow for handling OAuth authentication
  flow = InstalledAppFlow.from_client_secrets_file(
      'cred.json',
      SCOPES
  )
  credentials = flow.run_local_server(port=0)

  # Build the Gmail service
  service = build('gmail', 'v1', credentials=credentials)

  # Compose the email message
  message = EmailMessage()
  message.set_content('This is automated draft mail')

  message['To'] = 'wiktorqwe1234@gmail.com'
  message['From'] = 'msurvey203@gmail.com'
  message['Subject'] = 'Automated draft'
  encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

  create_message = {
      'message': {
          'raw': encoded_message
      }
  }
  # Send the email
  draft = service.users().drafts().create(userId="me",body=create_message).execute()

def getErrorr():
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response=requests.get("GET", "/v3/errors", headers=headers)

    print(response.json())

def postSurvey():
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    URL="https://api.surveymonkey.com/v3/surveys"
    with open("questions.json") as f:
        data = json.load(f)
    body=json.dumps(data)
    response=requests.post(URL, headers=headers,data=body)
    print(response.json())
    survey_id=response.json()["id"]
    return survey_id

def get_survey(id):
    

    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
        }
    URL=f"https://api.surveymonkey.com/v3/surveys/{id}"
    response=requests.get(URL, headers=headers,)

    print(response.json())




#get_survey(postSurvey())
send_invitations("Hello")
