"""Email service."""


class EmailService:
    def send_verification_email(self, to_email: str, token: str) -> None:
        raise NotImplementedError

    def send_password_reset_email(self, to_email: str, token: str) -> None:
        raise NotImplementedError
