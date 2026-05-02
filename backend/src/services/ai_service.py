"""Google Gemini AI service."""


class AIService:
    def chat(self, messages: list[dict], system_prompt: str) -> str:
        raise NotImplementedError

    def build_vps_system_prompt(self, vps: dict) -> str:
        raise NotImplementedError
