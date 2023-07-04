import infobip

client = infobip.ApiClient(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    api_key="YOUR_API_KEY",
)

response = client.send_sms_message(
    from_="YOUR_SENDER_ID",
    to="+1234567890",
    text="This is an SMS message.",
)

if response.status_code == 200:
    print("SMS message sent successfully.")
else:
    print("Error sending SMS message: " + response.text)