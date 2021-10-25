from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tour:
    round_name: str
    start_date: datetime
    matches: list

    def set_matches(self, matches):
        self.matches = matches

    def show_matches(self):
        print("*********** list of matches in " + self.round_name + " ****************")
        for match in self.matches:
            print(match.display_match())
