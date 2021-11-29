
class Config:
    """ The Config object store every constant variables of the application, except the DEFAULT_ROUNDS_NUMBER which is
    an attribute of the tournament object.
    """

    DEFAULT_PLAYERS_NUMBER = 8
    PLAYER_A_EXPECTED_INPUT = 'A'
    PLAYER_B_EXPECTED_INPUT = 'B'
    NO_WINNER_EXPECTED_INPUT = 'None'

    PLAYER_TABLE_NAME = "players"
    MATCH_TABLE_NAME = "matches"
    ROUND_TABLE_NAME = "rounds"
    TOURNAMENT_TABLE_NAME = "tournaments"

    DATE_STRING_FORMAT = "%m/%d/%Y, %H:%M:%S"

    DATABASE_NAME = "../database/db.json"
