#!/usr/bin/env python3

import requests

url="https://developer.surveymonkey.com/apps/109210/"

response = requests.get(url)

print(response)