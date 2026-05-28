from framework.models import EventPayload
from framework.sources.base import EventSource, event_source


@event_source(source_id="example", enabled=True)
class ExampleSource(EventSource):

    def fetch(self):
        return [
            {"name": "Evento de ejemplo", "url": "https://ejemplo.com", "location": "Ciudad"},
        ]

    def parse(self, raw):
        return [
            EventPayload(
                type_="event",
                name=item["name"],
                url=item["url"],
                source=self.source_id,
                data={"location": item["location"]},
            )
            for item in raw
        ]