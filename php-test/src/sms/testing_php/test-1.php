<?php

require_once "infobip/ApiClient.php";

$client = new ApiClient(
    "YOUR_USERNAME",
    "YOUR_PASSWORD",
    "YOUR_API_KEY",
);

$response = $client->sendSmsMessage(
    "YOUR_SENDER_ID",
    "+1234567890",
    "This is an SMS message.",
);

if ($response->getStatusCode() == 200) {
    echo "SMS message sent successfully.";
} else {
    echo "Error sending SMS message: " . $response->getBody();
}

?>