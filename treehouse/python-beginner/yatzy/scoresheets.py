# import yatzy.hands
# import yatzy.dice
import logging

logging.basicConfig(filename='yatzy.log', level=logging.DEBUG)

class YatzyScoreSheet:

    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_one_triple(self, hand):
        return self._score_set(hand, 3)

    def score_one_quad(self, hand):
        return self._score_set(hand, 4)

    def score_one_quint(self, hand):
        return self._score_set(hand, 5)

    def score_chance(self, hand):
        return sum(hand)

    def score_yatzy(self, hand):
        check = hand[0]
        for values in hand:
            if values != check:
                return 0
        else:
            return 50


logging.debug("this is a test")
logging.info("this is a butt")
print("butts")