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


ACCESS_TOKEN="cMFftolwVdUKH2zJtk2zDOMeAKkYgQk3RxT7usJRmmEjnrLw8YQ52QIhm7OhjibN.Mz86CNoWe1tq06i52S982BC5bqZrzuIykpxGsAxAa2vsOUmnD3vqJUJwObv4ten"




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
    print(survey_id)
    return survey_id

def get_surveys():
    

    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
        }
    URL="https://api.surveymonkey.com/v3/surveys"
    response=requests.get(URL, headers=headers,)

    print(response.json())



postSurvey()

