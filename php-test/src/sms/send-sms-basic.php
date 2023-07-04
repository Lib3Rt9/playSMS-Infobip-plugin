<?php

/**
 * Send an SMS message directly by calling HTTP endpoint.
 *
 * For your convenience, environment variables are already pre-populated with your account data
 * like authentication, base URL and phone number.
 *
 * Please find detailed information in the readme file.
 */

require '../../vendor/autoload.php';

use GuzzleHttp\Client;
use GuzzleHttp\RequestOptions;

$client = new Client([
    'base_uri' => "https://pw9pzm.api.infobip.com/",
    'headers' => [
        'Authorization' => "App 8695e00b99f6a931d239927bb4d52df7-53eb2658-b221-40ac-9f4d-43cc978e2111",
        'Content-Type' => 'application/json',
        'Accept' => 'application/json',
    ]
]);

$response = $client->request(
    'POST',
    'sms/2/text/advanced',
    [
        RequestOptions::JSON => [
            'messages' => [
                [
                    'from' => 'InfoSMS',
                    'destinations' => [
                        ['to' => "84336020181"]
                    ],
                    'text' => 'This is a sample message',
                ]
            ]
        ],
    ]
);

echo("HTTP code: " . $response->getStatusCode() . PHP_EOL);
echo("Response body: " . $response->getBody()->getContents() . PHP_EOL);
