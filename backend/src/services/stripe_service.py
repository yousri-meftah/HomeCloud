"""Stripe service."""


class StripeService:
    def create_checkout_session(self, price_id: str, customer_id: str, user_id: str) -> str:
        raise NotImplementedError

    def handle_webhook(self, payload: bytes, signature: str) -> dict:
        raise NotImplementedError

    def get_subscription(self, customer_id: str) -> dict:
        raise NotImplementedError
