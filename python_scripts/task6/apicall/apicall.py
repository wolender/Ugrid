#!/usr/bin/env python3


"""
Module handles SurveyMonkey API
"""

import json
import requests


ACCESS_TOKEN="cMFftolwVdUKH2zJtk2zDOMeAKkYgQk3RxT7usJRmmEjnrLw8YQ52QIhm7OhjibN.Mz86CNoWe1tq06i52S982BC5bqZrzuIykpxGsAxAa2vsOUmnD3vqJUJwObv4ten"

def get_error():
    """returns list of errors pulled from survey monkey api"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    response=requests.get("GET", "/v3/errors", headers=headers, timeout=10)

    print(response.json())

def post_survey():
    """posts survey located in questions.json file to surveymonkey api"""
    headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    post_survey_url="https://api.surveymonkey.com/v3/surveys"
    with open("questions.json",encoding="UTF-8") as survey_file:
        data = json.load(survey_file)
    body=json.dumps(data)
    response=requests.post(post_survey_url, headers=headers,data=body, timeout=10)
    survey_id=response.json()["id"]
    return survey_id

def get_survey(survey_id):
    """gets survey fom the api based on survey id"""

    headers = {
        'Accept': "application/json",
        'Authorization': f"Bearer {ACCESS_TOKEN}"
        }
    get_survey_url=f"https://api.surveymonkey.com/v3/surveys/{survey_id}"
    response=requests.post(get_survey_url, headers=headers, timeout=10)

    print(response.json())

def create_weblink(survey_id):
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
    create_weblink_url=f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors"
    response=requests.post(create_weblink_url, headers=headers, data=data, timeout=10)
    return response.json()["url"]

def get_collectors(survey_id):
    """returns collectors for survey, can get weblink for instance"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    get_collectors_url=f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors"
    response=requests.get(get_collectors_url, headers=headers, timeout=10)
    print(response.json())
    return response.json()['id']

def get_collector(collector_id):
    """returns specifiic collector"""
    headers = {
    'Accept': "application/json",
    'Authorization': f"Bearer {ACCESS_TOKEN}"
    }
    get_collector_url=f"https://api.surveymonkey.com/v3/collectors/{collector_id}"
    response=requests.get(get_collector_url, headers=headers, timeout=10)
    print(response.json()['url'])
    return response.json()['url']

def parse_reps():
    """returns list of email adresses from recipients.txt file"""
    reps=[]
    with open("recipients.txt","r",encoding="UTF-8") as recipients_file:
        for line in recipients_file:
            reps.append(line.replace("\n",""))
    return reps
