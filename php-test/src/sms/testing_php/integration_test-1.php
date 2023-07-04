<?php

require_once "infobip/ApiClient.php";

class InfobipGatewayPlugin extends GatewayPlugin {

    public function __construct(Config $config) {
        parent::__construct($config);

        $this->username = $config["infobip_username"];
        $this->password = $config["infobip_password"];
        $this->api_key = $config["infobip_api_key"];
    }

    public function sendSms(string $from, string $to, string $text) {
        $client = new ApiClient(
            $this->username,
            $this->password,
            $this->api_key,
        );

        $response = $client->sendSmsMessage(
            $from,
            $to,
            $text,
        );

        if ($response->getStatusCode() == 200) {
            return true;
        } else {
            return false;
        }
    }

}