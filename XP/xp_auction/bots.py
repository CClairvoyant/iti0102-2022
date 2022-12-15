"""Bot classes."""

import random
from typing import Type

from auction import Bot


class GreedyBot:
    """The greedy bot always bids all of their money."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return money


class ModerateBot:
    """The moderate bot always bids half of their money."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return min(int(money * 0.5), money)


class MoodyBot:
    """The moody bot does whatever they want."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return min(random.choice((money // 2, money // 3, 20, 10, 5)), money)


class RandomBot:
    """The random bot always bids randomly with a uniform distribution."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return random.randrange(money + 1)


class GaussianBot:
    """The Gaussian bot always bids randomly with a normal distibution (m, sd)."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        x = random.gauss(36, 20)
        return min(abs(int(x)), money)


class CopycatBot:
    """The copycat bot always bids what their opponent bid on the last round."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return min(max(last_bid, 0), money)


class DeepCopycatBot:
    """The deep copycat bot always bids what their opponent bid two rounds ago."""

    def __init__(self):
        """Initialize the class, put all the variables that you want to save here."""
        self.old_bid = 0

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        self.old_bid = max(last_bid, 0)
        return min(self.old_bid, money)


class IndecisiveBot:
    """The indecisive bot alternates between bidding 0 and all of their money."""

    def __init__(self):
        """Initialize the class, put all the variables that you want to save here."""
        self.bid_high = True

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        self.bid_high = not self.bid_high  # switch between True/False each round
        if self.bid_high:
            return money
        return 0


active_bots_list: list[Type[Bot]] = [
    GreedyBot,
    ModerateBot,
    MoodyBot,
    RandomBot,
    GaussianBot,
    CopycatBot,
    DeepCopycatBot,
    IndecisiveBot,
]
