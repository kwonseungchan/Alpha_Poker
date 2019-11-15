from pypokerengine.api.game import setup_config, start_poker
from players.fish_player import FishPlayer
from players.console_player import ConsolePlayer
from players.random_player import RandomPlayer
from players.honest_player import HonestPlayer
from players.emulator_player import EmulatorPlayer

config = setup_config(max_round=30, initial_stack=1000, small_blind_amount=20)
config.register_player(name="Player", algorithm=HonestPlayer())
config.register_player(name="ConsolePlayer", algorithm=ConsolePlayer())
game_result = start_poker(config, verbose=1)
