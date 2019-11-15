from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
import random

NB_SIMULATION = 1000

class HonestPlayer(BasePokerPlayer):

    def declare_action(self, valid_actions, hole_card, round_state):
        community_card = round_state['community_card']
        win_rate = estimate_hole_card_win_rate(
                nb_simulation=NB_SIMULATION,
                nb_player=self.nb_player,
                hole_card=gen_cards(hole_card),
                community_card=gen_cards(community_card)
                )

        print("승률 : ", win_rate)
        i = random.random()
        if win_rate >= 0.99: #승률 99% 이상일 때
            #amount = max(amount["min"], amount["max"]) #올인
            #action = valid_actions[2]['amount'] #레이즈
            return valid_actions[2]['action'], valid_actions[2]['amount']['max']
        elif win_rate >= 0.975: #승률 97.5% 이상일 때
            #betAmount = ( 0.1 * amount["min"]+ 0.9 * max(amount["min"], amount["max"]) )
            #action = valid_actions[2]['amount'] #레이즈
            return valid_actions[2]['action'], valid_actions[2]['amount']['max']
        elif win_rate >= 0.95: #승률 95% 이상일 때
            #betAmount = ( 0.2 * amount["min"]+ 0.8 * max(amount["min"], amount["max"]) )
            #action = valid_actions[2]['amount'] #레이즈
            return valid_actions[2]['action'], valid_actions[2]['amount']['max']
        elif win_rate >= 0.9: #승률 90% 이상일 때
            #betAmount = ( 0.5 * amount["min"]+ 0.5 * max(amount["min"], amount["max"]) )
            #action = valid_actions[2]['amount'] #레이즈
            return valid_actions[2]['action'], valid_actions[2]['amount']['max']
        elif win_rate >= 0.8: #승률 80% 이상일 때
            #amount = ( 0.2 * amount["min"]+ 0.8 * max(amount["min"], amount["max"]) )
            #action = valid_actions[2]['amount'] #레이즈
            return valid_actions[2]['action'], valid_actions[2]['amount']['min']
        elif win_rate >= 0.7: #승률 70% 이상일 때
            #action = valid_actions[1] #콜
            return valid_actions[1]['action'], valid_actions[1]['amount']
        elif win_rate >= 0.6: #승률 60% 이상일 때
            #action = valid_actions[1] #콜
            return valid_actions[1]['action'], valid_actions[1]['amount']
        elif win_rate >= 0.5: #승률 50% 이상일 때
            #action = valid_actions[1] #콜
            return valid_actions[1]['action'], valid_actions[1]['amount']
        else: 
            return valid_actions[0]['action'], valid_actions[0]['amount']
            #if i >= 0.90: #10% 확률로 레이즈 블러핑
                #action = valid_actions[2] #블러핑(레이즈)
            #elif i >= 0.80: #20% 확률로 콜 블러핑
                #action = valid_actions[1] #블러핑(콜)
            #else: 
                #action = valid_actions[0]  #폴드
        #return action['action'], action['amount']

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

