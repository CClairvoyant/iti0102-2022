"""MX Auction."""


class PlayerBot:
    """Bot algorithm."""

    @staticmethod
    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        return min(money, last_bid + 2)


if __name__ == '__main__':
    from auction import Auction  # copy the files auction.py and bots.py!

    # play all the example bots against each other.
    Auction(main_player=PlayerBot).simulate(auctions=99, rounds=99)
