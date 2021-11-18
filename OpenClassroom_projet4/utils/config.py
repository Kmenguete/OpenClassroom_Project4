from tinydb import TinyDB


class Config:
    DEFAULT_PLAYERS_NUMBER = 8
    PLAYER_A_EXPECTED_INPUT = 'A'
    PLAYER_B_EXPECTED_INPUT = 'B'
    NO_WINNER_EXPECTED_INPUT = 'None'
    DATABASE = TinyDB('database.json')
