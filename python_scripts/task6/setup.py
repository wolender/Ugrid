from setuptools import setup, find_packages

setup(
    name='SurveyMonkey',
    version='1.0.0',
    packages=find_packages(),
    author='Wiktor Olender',
    author_email='wikto.olender1@gmail.co',
    description='Create a survey and send it to list of emails',
    install_requires=[
        "requests",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib"
    ]
)
