import requests
import os
"""
 * Send an email message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient email
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send email API reference: https://www.infobip.com/docs/api#channels/email/send-email
 * See Readme file for details.
"""

BASE_URL = "https://pw9pzm.api.infobip.com"
API_KEY = "App 8695e00b99f6a931d239927bb4d52df7-53eb2658-b221-40ac-9f4d-43cc978e2111"

SENDER_EMAIL = "phamgiaphuc011709@selfserviceib.com"
RECIPIENT_EMAIL = "phamgiaphuc011709@gmail.com"
EMAIL_SUBJECT = "This is a sample email subject"
EMAIL_TEXT = "This is a sample email message."

BASE_FILE_PATH = "/home/infobip/project/src/email/files"

file_name = "infobip.png"

file = open(os.path.join(BASE_FILE_PATH, file_name), 'rb')
files = {'attachment': (file_name, file)}

form_data = {
    "from": SENDER_EMAIL,
    "to": RECIPIENT_EMAIL,
    "subject": EMAIL_SUBJECT,
    "text": EMAIL_TEXT
}

all_headers = {
    "Authorization": API_KEY
}

response = requests.post(BASE_URL + "/email/3/send", data=form_data, files=files, headers=all_headers)

file.close()

print("Status Code: " + str(response.status_code))
print(response.json())
