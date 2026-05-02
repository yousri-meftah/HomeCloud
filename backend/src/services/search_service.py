"""Elasticsearch search service."""


class SearchService:
    def index_event(self, event_type: str, data: dict) -> None:
        raise NotImplementedError

    def search(self, query: str) -> dict:
        raise NotImplementedError
