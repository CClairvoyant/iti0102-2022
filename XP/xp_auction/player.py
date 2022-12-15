"""MX Auction."""
from auction import Auction  # copy the files auction.py and bots.py!


class PlayerBot:
    """Bot algorithm."""

    def __init__(self):
        """Initialize the class, put all the variables that you want to save here."""
        pass

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return min(money, last_bid + 1)  # example algorithm that bids up to 15 every round


if __name__ == '__main__':
    # play all the example bots against each other
    Auction(main_player=PlayerBot).simulate(auctions=99, rounds=99)
