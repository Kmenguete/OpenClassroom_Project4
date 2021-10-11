from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tour:
    round_name: str
    start_date: datetime
    matches: list

    def set_matches(self, matches):
        self.matches = matches
