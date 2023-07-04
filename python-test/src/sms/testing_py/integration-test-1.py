from playsms.gateway import GatewayPlugin

class InfobipGatewayPlugin(GatewayPlugin):

    def __init__(self, config):
        super().__init__(config)

        self.username = config["infobip_username"]
        self.password = config["infobip_password"]
        self.api_key = config["infobip_api_key"]

    def send_sms(self, from_, to, text):
        client = infobip.ApiClient(
            username=self.username,
            password=self.password,
            api_key=self.api_key,
        )

        response = client.send_sms_message(
            from_=from_,
            to=to,
            text=text,
        )

        if response.status_code == 200:
            return True
        else:
            return False