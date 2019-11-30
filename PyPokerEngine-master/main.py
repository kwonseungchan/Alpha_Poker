from pypokerengine.api.game import setup_config, start_poker
from players.fish_player import FishPlayer
from players.console_player import ConsolePlayer
from players.random_player import RandomPlayer
from players.honest_player  import HonestPlayer
from players.emulator_player import EmulatorPlayer
from pypokerengine.engine.tts import tts
import time


config = setup_config(max_round=10, initial_stack=20, small_blind_amount=1)
config.register_player(name="인공지능", algorithm=HonestPlayer())
config.register_player(name="플레이어", algorithm=ConsolePlayer())
#config.register_player(name="EmulatorPlayer", algorithm=EmulatorPlayer())
#config.register_player(name="FishPlayer", algorithm=FishPlayer())
game_result = start_poker(config, verbose=1)
quote = ( "게임이 종료되었습니다." )
tts.playTts(tts, quote)
time.sleep(3)
