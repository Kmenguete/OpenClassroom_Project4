from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tour:
    """ The round model is the class that let the application to create a round object(and their corresponding matches
    object). When the application creates a round, it automatically creates matches object (from match model) with
    players (from player model). Of course, players object are players that have been created by the user when we asked
    him/her to create players.
    """
    round_id: str
    round_name: str
    start_date: datetime
    matches: list

    def set_matches(self, matches):
        """ The set_matches method let to attach a match_list to Tour object.
            """
        self.matches = matches

    def __str__(self):
        """ The str method gives a string representation of Tour object when it is printed.
                    """
        return "round_id: " + self.round_id + ", " + "round_name: " + self.round_name + ", " + "start_date: " + \
               str(self.start_date) + ", " + "match_list: " + str(self.matches)

    def __repr__(self):
        """ The repr method gives a representation of Tour object when it is printed.
                            """
        return "round_id: " + self.round_id + ", " + "round_name: " + self.round_name + ", " + "start_date: " + \
               str(self.start_date) + ", " + "match_list: " + str(self.matches)
