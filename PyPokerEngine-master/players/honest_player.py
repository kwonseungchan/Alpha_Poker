from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
import random as rand
import time
from pypokerengine.engine.tts import tts

NB_SIMULATION = 1000

class HonestPlayer(BasePokerPlayer):

    limit = 0

    def declare_action(self, valid_actions, hole_card, round_state):
        community_card = round_state['community_card']
        win_rate = estimate_hole_card_win_rate(
                nb_simulation=NB_SIMULATION,
                nb_player=self.nb_player,
                hole_card=gen_cards(hole_card),
                community_card=gen_cards(community_card)
                )
        choice = self.__choice_action(valid_actions, win_rate)
        action = choice["action"]
        amount = choice["amount"]
        
        if action == "raise":
            maxAmount = amount["max"]
            minAmount = amount["min"]
            self.limit = 37 - maxAmount
            i = rand.random()

            if win_rate < 0.8: # 70% ~ 80%
                if i < 0.7: # 0% ~ 70%
                    amount = amount["min"]
                elif i < 0.8: # 70% ~ 80%
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )
                else : # 98% ~ 100%
                    amount = amount["max"]

            elif win_rate < 0.9: # 80% ~ 90%
                if i < 0.7: # 0% ~ 70%
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.8: # 70% ~ 80%
                    amount = amount["min"]
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )
                else : # 98% ~ 100%
                    amount = amount["max"]

            elif win_rate < 0.95: # 90% ~ 95%
                if i < 0.7: # 0% ~ 70%
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.8: # 70% ~ 80%
                    amount = amount["min"]
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )
                else : # 98% ~ 100%
                    amount = amount["max"]

            elif win_rate < 0.975: # 95% ~ 97.5%
                if i < 0.7: # 0% ~ 70%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                elif i < 0.8: # 70% ~ 80%
                    amount = amount["min"]
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )
                else : # 98% ~ 100%
                    amount = amount["max"]

            elif win_rate < 0.99: # 97.5% ~ 99%
                if i < 0.7: # 0% ~ 70%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )
                elif i < 0.8: # 70% ~ 80%
                    amount = amount["min"]
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                else : # 90% ~ 100%
                    amount = amount["max"]

            else: # 99% ~
                if i < 0.7: # 0% ~ 70%
                    amount = amount["max"]
                elif i < 0.8: # 70% ~ 80%
                    amount = amount["min"]
                elif i < 0.9 : # 80% ~ 90%    
                    amount = int (maxAmount * 0.2 + minAmount * 0.8 )
                elif i < 0.95 : # 90% ~ 95%
                    amount = int (maxAmount * 0.4 + minAmount * 0.6 )
                elif i < 0.98 : # 95% ~ 98%
                    amount = int (maxAmount * 0.6 + minAmount * 0.4 )
                else : # 98% ~ 100%
                    amount = int (maxAmount * 0.8 + minAmount * 0.2 )

            if amount >= self.limit:
                amount = self.limit

        if action == "fold":
            quote = ( "인공지능이 폴드를 선언했습니다." )
            tts.playTts(tts, quote)
            time.sleep(2)
        elif action == "call":
            quote = ( "인공지능이 콜을 선언했습니다." )
            tts.playTts(tts, quote)
            time.sleep(2)
        elif action == "raise":
            if amount == -1:
                tts.playTts(tts, "인공지능이 폴드를 선언했습니다.")
            else:
                quote = ( "인공지능이" + str(amount) +"만큼 레이즈를 선언했습니다." )
                tts.playTts(tts, quote)
            time.sleep(3)
        else:
            quote = ( "error" + str(action) )
            tts.playTts(tts, quote)
            time.sleep(3)
        return action, amount

    def __choice_action(self, valid_actions, win_rate):
        i = rand.random()
        if win_rate <= 0.5:
            if i < 0.7:
                return valid_actions[0]
            elif i < 0.9:
                return valid_actions[1]
            else:
                return valid_actions[2]
        elif win_rate <= 0.7:
            if i < 0.7:
                return valid_actions[1]
            else:
                return valid_actions[2]
        else:
            return valid_actions[2]


    def receive_game_start_message(self, game_info):
        self.nb_player = game_info['player_num']

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

