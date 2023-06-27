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

URL="https://developer.surveymonkey.com/apps/109210/"
ACCESS_TOKEN="Yya8.NW4a0iZVuIl3LgNwg3Z59Yoj85b2Nbfu-SQQPOL0VQ37x1gsfb-oCqg.t5i4qNjwDRmJSxxRjZbyRvkIjcCUY-lS1plf7Vo8rc4hx3JZk93NXbRQ0vmsg4lmusj"
SECRET="338261461392545728117431788066757798226"
SURVEY_ID=0


headers = {
    "Authorization": "Bearer " + ACCESS_TOKEN,
    "Content-Type": "application/json"
}

url = f"https://api.surveymonkey.com/v3/surveys/{SURVEY_ID}"

response = requests.get(url, headers=headers,timeout=10)

if response.status_code == 200:
    survey_data = response.json()
    # Process the survey data as needed
else:
    print("Error:", response.text)

print(response)
