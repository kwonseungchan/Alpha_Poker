import pypokerengine.utils.visualize_utils as U
from pypokerengine.players import BasePokerPlayer
from pypokerengine.engine.tts import tts
import time

class ConsolePlayer(BasePokerPlayer):

  def __init__(self, input_receiver=None):
    self.input_receiver = input_receiver if input_receiver else self.__gen_input_wrapper()

  def declare_action(self, valid_actions, hole_card, round_state):
    print(U.visualize_declare_action(valid_actions, hole_card, round_state, self.uuid))
    action, amount = self.__receive_action_from_console(valid_actions)
    return action, amount

  def receive_game_start_message(self, game_info):
    print(U.visualize_game_start(game_info, self.uuid))
    quote = "게임이 시작되었습니다."
    ##여기에 게임 정보 받아서 입력
    tts.playTts(tts, quote)
    self.__wait_until_input()

  def receive_round_start_message(self, round_count, hole_card, seats):
    print(U.visualize_round_start(round_count, hole_card, seats, self.uuid))
    quote = ( str(round_count) + "라운드가 시작되었습니다." )
    tts.playTts(tts, quote)
    time.sleep(2)
    if round_count%2 == 1: #홀수라운드
      tts.playTts(tts, "플레이어가 5만큼 스몰블라인드, 인공지능이 10만큼 빅블라인드입니다.")
      time.sleep(3)
    elif round_count%2 == 0: #짝수라운드
      tts.playTts(tts, "플레이어가 10만큼 빅블라인드, 인공지능이 5만큼 스몰블라인드입니다.")
      time.sleep(3)
    else: #에러
      tts.playTts(tts, "블라인드 정보 음성출력 에러입니다.")
    self.__wait_until_input()

  def receive_street_start_message(self, street, round_state):
    print(U.visualize_street_start(street, round_state, self.uuid))
    quote = ( str(street) + "입니다." )
    tts.playTts(tts, quote)
    self.__wait_until_input()

  def receive_game_update_message(self, new_action, round_state):
    print(U.visualize_game_update(new_action, round_state, self.uuid))
    self.__wait_until_input()

  def receive_round_result_message(self, winners, hand_info, round_state):
    print(U.visualize_round_result(winners, hand_info, round_state, self.uuid))
    self.__wait_until_input()

  def __wait_until_input(self):
    time.sleep(3)
    #input("Enter some key to continue ...")

  def __gen_input_wrapper(self):
    return lambda msg: input(msg)

  def __receive_action_from_console(self, valid_actions):
    quote = ( "폴드, 레이즈, 콜 중에 결정해주세요." )
    tts.playTts(tts, quote)
    time.sleep(2)
    flg = self.input_receiver('Enter /(fold), *(call), -(raise).\n >> ')
    if flg in self.__gen_valid_flg(valid_actions):
      if flg == '/':
        quote = ( "폴드 했습니다." )
        tts.playTts(tts, quote)
        time.sleep(2)
        return valid_actions[0]['action'], valid_actions[0]['amount']
      elif flg == '*':
        quote = ( "콜 했습니다." )
        tts.playTts(tts, quote)
        time.sleep(2)
        return valid_actions[1]['action'], valid_actions[1]['amount']
      elif flg == '-':
        valid_amounts = valid_actions[2]['amount']
        time.sleep(3)
        tts.playTts(tts, quote)
        raise_amount = self.__receive_raise_amount_from_console(valid_amounts['min'], valid_amounts['max'])
        quote = ( str(raise_amount) + "만큼 레이즈 했습니다." )
        tts.playTts(tts, quote)
        time.sleep(3)
        return valid_actions[2]['action'], raise_amount
    else:
      return self.__receive_action_from_console(valid_actions)

  def __gen_valid_flg(self, valid_actions):
    flgs = ['/', '*']
    is_raise_possible = valid_actions[2]['amount']['min'] != -1
    if is_raise_possible:
      flgs.append('-')
    return flgs

  def __receive_raise_amount_from_console(self, min_amount, max_amount):
    quote = ( str(min_amount) + "에서" + str(max_amount) + "사이에서 레이즈 가능합니다.")
    tts.playTts(tts, quote)
    raw_amount = self.input_receiver("valid raise range = [%d, %d]" % (min_amount, max_amount))
    try:
      amount = int(raw_amount)
      if min_amount <= amount and amount <= max_amount:
        return amount
      else:
        print("Invalid raise amount %d. Try again.")
        return self.__receive_raise_amount_from_console(min_amount, max_amount)
    except:
      print("Invalid input received. Try again.")
      return self.__receive_raise_amount_from_console(min_amount, max_amount)

