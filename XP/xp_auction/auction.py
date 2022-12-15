"""Auction simulator."""
from __future__ import annotations
import itertools as it
from typing import Protocol, Type, Optional


class Bot(Protocol):
    """Bot protocol. Used instead of ABCs to simplify PlayerBot."""

    def play(self, money: int, opponent_money: int, last_bid: int) -> int:
        """Play a round in the auction."""
        ...


class Auction:
    """Auction simulator."""

    class Player:
        """A player in an auction."""

        __slots__ = 'player', 'name', 'score', 'money', 'salary', 'last_bid'

        def __init__(self, player: Bot, money: int = 100, salary: int = 10):
            """Initialize the player."""
            self.player = player
            self.name = type(player).__name__
            self.score = 0  # each item bought grants a point
            self.money = money
            self.salary = salary
            self.last_bid = -1

        def play(self, opponent: Auction.Player) -> int:
            """Play a round in the auction."""
            bid = self.player.play(self.money, opponent.money, opponent.last_bid)
            assert self.money >= bid, f"{self.name}'s bid of {bid} exceeds their balance of {self.money}"
            assert bid >= 0, f"{self.name}'s bid of {bid} is negative"
            return bid

        def bid(self, bid: int):
            """Process the bid finances."""
            self.money -= bid  # bid sum is withdrawn
            self.money += self.salary  # both players receive money each round
            self.last_bid = bid  # set last bid for the next play() round

    def __init__(self, bots: Optional[list[Type[Bot]]] = None, *, main_player: Optional[Type[Bot]] = None):
        """Initialize the auction."""
        from bots import active_bots_list

        default_bots = active_bots_list
        self.bots = bots or default_bots
        self.main_player = main_player
        if main_player is not None:
            self.bots.append(main_player)

    def simulate(self, auctions: int, rounds: int, *, print_scoreboard: bool = True) -> dict[str, int]:
        """Simulate a game."""
        scoreboard = {bot.__name__: 0 for bot in self.bots}
        player_stats = scoreboard.copy()

        for _ in range(auctions):
            for player_a, player_b in it.combinations(self.bots, 2):  # pair all the players against each other
                player_a, player_b = self.Player(player_a()), self.Player(player_b())  # wrap classes
                auction_winner = self._simulate_auction(rounds, player_a, player_b)  # play out the auction

                if auction_winner is None:
                    continue  # no one gets a point in case of a draw

                scoreboard[auction_winner.name] += 1  # winner receives a point
                if self.main_player in (type(player_a.player), type(player_b.player)):
                    player_stats[auction_winner.name] += 1  # main player stats
                    # print(f'{player_a.name:<27} vs {player_b.name:>27} -> {auction_winner.name}')

        max_points = auctions * (len(self.bots) - 1)  # max points that a player could've won
        if self.main_player is not None:
            print(player_stats)

        if print_scoreboard:
            self._print_scoreboard(scoreboard, max_points)
        return scoreboard

    @staticmethod
    def _simulate_auction(rounds: int, player_a: Player, player_b: Player) -> Optional[Player]:
        """Simulate an auction."""
        for _ in range(rounds):  # each auction lasts a certain number of rounds
            # both players place their bids
            bid_a, bid_b = player_a.play(opponent=player_b), player_b.play(opponent=player_a)
            player_a.bid(bid_a)
            player_b.bid(bid_b)

            if bid_a != bid_b:  # if the bids are equal, no one wins
                higher_bidder = player_a if bid_a > bid_b else player_b  # higher bidder wins the auction
                higher_bidder.score += 1

        if player_a.score == player_b.score:
            return None  # in case of draw, neither player gets a point
        return player_a if player_a.score > player_b.score else player_b  # player with most bought items wins

    def _print_scoreboard(self, scoreboard: dict[str, int], max_points: int):
        """Print the scoreboard."""
        for bot in sorted(self.bots, key=lambda a: scoreboard[a.__name__]):
            name = bot.__name__
            print(f'{name:>27}: {scoreboard[name]:>4}/{max_points:<4} points')

        winners = (winner for winner, score in scoreboard.items() if score == max(scoreboard.values()))
        print(f'Winners: {", ".join(winners)}')  # bots with most auctions won are considered the winners


if __name__ == '__main__':
    from bots import active_bots_list
    from secret_bots import active_secret_bots_list  # for the tester's eyes only!

    auction = Auction(bots=active_bots_list + active_secret_bots_list)
    auction.simulate(auctions=99, rounds=99)
