#!/usr/bin/env python3
import smtplib

def send_mail(email_messege, port = 2525, smtp_server = "localhost", sender_email = "my@example.com", receiver_email = "your@example.com"):
    
    message = f"""\
Subject: Survey invite

Please take survey below:
{email_messege}"""
    
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender_email, receiver_email, message)

