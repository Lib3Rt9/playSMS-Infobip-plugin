import http.client

"""
 * Send an sms message by using Infobip API.
 *
 * This example is already pre-populated with your account data:
 * 1. Your account Base URL
 * 2. Your account API key
 * 3. Your recipient phone number
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send sms API reference: https://www.infobip.com/docs/api#channels/sms/send-sms-message
 * See Readme file for details.
"""

BASE_URL = "pw9pzm.api.infobip.com"
API_KEY = "App 8695e00b99f6a931d239927bb4d52df7-53eb2658-b221-40ac-9f4d-43cc978e2111"

SENDER = "InfoSMS"
RECIPIENT = "84336020181"
MESSAGE_TEXT = "This is a sample message"

conn = http.client.HTTPSConnection(BASE_URL)

payload1 = "{\"messages\":" \
          "[{\"from\":\"" + SENDER + "\"" \
          ",\"destinations\":" \
          "[{\"to\":\"" + RECIPIENT + "\"}]," \
          "\"text\":\"" + MESSAGE_TEXT + "\"}]}"

headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload1, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
