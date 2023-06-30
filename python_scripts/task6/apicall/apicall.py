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

import requests
import json
import emailbot

ACCESS_TOKEN="cMFftolwVdUKH2zJtk2zDOMeAKkYgQk3RxT7usJRmmEjnrLw8YQ52QIhm7OhjibN.Mz86CNoWe1tq06i52S982BC5bqZrzuIykpxGsAxAa2vsOUmnD3vqJUJwObv4ten"

def getErrorr():
    """returns list of errors pulled from survey monkey api"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response=requests.get("GET", "/v3/errors", headers=headers)

    print(response.json())

def postSurvey():
    """posts survey located in questions.json file to surveymonkey api"""
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
    survey_id=response.json()["id"]
    return survey_id

def get_survey(id):
    """gets survey fom the api based on survey id"""

    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
        }
    URL=f"https://api.surveymonkey.com/v3/surveys/{id}"
    response=requests.post(URL, headers=headers,)

    print(response.json())

def create_weblink(id):
  """creates invite link for created survey and returns link that gets sent out"""
  headers = {
  'Content-Type': "application/json",
  'Accept': "application/json",
  'Authorization': f"Bearer {ACCESS_TOKEN}"
  }
  body={
      'type': 'weblink',
      'name': 'Web Link 1'
  }
  data=json.dumps(body)
  URL=f"https://api.surveymonkey.com/v3/surveys/{id}/collectors"
  response=requests.post(URL, headers=headers, data=data)
  return response.json()["url"]

def get_collectors(id):
    """returns collectors for survey, can get weblink for instance"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    URL=f"https://api.surveymonkey.com/v3/surveys/{id}/collectors"
    response=requests.get(URL, headers=headers)
    print(response.json())
    return response.json()['id']

def get_collector(id):
    """returns specifiic collector"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    URL=f"https://api.surveymonkey.com/v3/collectors/{id}"
    response=requests.get(URL, headers=headers)
    print(response.json()['url'])
    return response.json()['url']

def parse_reps():
  """returns list of email adresses from recipients.txt file"""
  reps=[]
  with open("recipients.txt","r",encoding="UTF-8") as f:
      for line in f:
        reps.append(line.replace("\n",""))
  return reps


if __name__ == '__main__':
  webllink=create_weblink(postSurvey())
  email_list=parse_reps()
  for email in email_list:
     #sends emails with survey
     emailbot.gmail_send_message(content=webllink,email=email)
