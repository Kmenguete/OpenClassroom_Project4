from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tour:
    round_name: str
    start_date: datetime
    matches: list

    def set_matches(self, matches):
        self.matches = matches

    def __str__(self):
        return "round_name: " + self.round_name + ", " + "start_date: " + str(self.start_date) + ", " + "match_list: " \
               + str(self.matches)

    def __repr__(self):
        return "round_name: " + self.round_name + ", " + "start_date: " + str(self.start_date) + ", " + "match_list: " \
               + str(self.matches)
