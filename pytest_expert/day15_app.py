# Day 15: Mock Payment Application

class GatewayClient:
    def charge(self, amount, token):
        """Simulates network communication. Raises NotImplementedError in test environment."""
        raise NotImplementedError("Network integration is offline during test sweeps!")

class PaymentProcessor:
    def __init__(self, gateway_client):
        self.gateway_client = gateway_client

    def process_payment(self, amount, card_token):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero")
        try:
            status = self.gateway_client.charge(amount, card_token)
            if status == "SUCCESS":
                return True
            return False
        except Exception as e:
            raise RuntimeError(f"Payment failed due to gateway error: {e}")
