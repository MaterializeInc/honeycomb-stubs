from typing import Any

class Event:
    def add(self, data=dict[str, Any]) -> None: ...

    def add_field(self, name: str, val: Any) -> None: ...

    def send(self) -> None: ...
