"""Results of some made up games."""


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        """Class constructor."""
        self.filename = filename

    @property
    def rows(self):
        """Rows of content."""
        with open(self.filename) as file:
            content = file.read()
        return content.split("\n")

    @property
    def players(self):
        """Return list of player objects."""

        def func(name: str):
            """Find a player object by name."""
            return list(filter(lambda x: x.name == name, players))[0]

        players = list(map(lambda x: Player(x, 0, 0, []), self.get_player_names()))
        for match in self.matches:
            if match.result_type == "winner":
                func(match.players[0]).wins += 1
            elif match.result_type == "places":
                func(match.players[0]).wins += 1
                func(match.players[-1]).losses += 1
            elif match.result_type == "points":
                max_position = match.result.index(max(match.result))
                winner = match.players[max_position]
                func(winner).wins += 1
                min_position = match.result.index(min(match.result))
                loser = match.players[min_position]
                func(loser).losses += 1
            for player in match.players:
                func(player).games_played.append(match.game)
        return players

    @property
    def matches(self):
        """Return list of matches."""
        matches = []
        for row in self.rows:
            if ";" in row:
                data = row.split(";")
                matches.append(Match(data[0], data[1].split(","), data[2], data[3].split(",")))
        return matches

    def __get_person_with_name(self, name: str):
        """Return the Player object with the given name."""
        return list(filter(lambda x: x.name == name, self.players))[0] if list(
            filter(lambda x: x.name == name, self.players)) else None

    def __get_matches(self, game):
        """Return the matches of mentioned game."""
        return list(filter(lambda x: x.game == game, self.matches))

    def get_player_names(self) -> list[str]:
        """Return player names."""
        player_names = set()
        for match in self.matches:
            for player in match.players:
                player_names.add(player)
        return list(player_names)

    def get_game_names(self) -> list[str]:
        """Return game names."""
        game_names = set()
        for match in self.matches:
            game_names.add(match.game)
        return list(game_names)

    def get_games_played_amount(self) -> int:
        """Return the amount of matches played by players."""
        return len(self.matches)

    def get_games_played_of_type(self, result_type: str) -> int:
        """Return the amount of matches played of result type (points, places, winner)."""
        return len(list(filter(lambda x: x.result_type == result_type, self.matches)))

    def get_games_amount_played_by(self, player_name: str) -> int:
        """Return amount of matches played by a certain player."""
        return len(self.__get_person_with_name(player_name).games_played) if list(
            filter(lambda x: x.name == player_name, self.players)) else None

    def get_favourite_game(self, player_name: str) -> str:
        """Return the game of which the player has played the most times."""
        games = self.__get_person_with_name(player_name).games_played
        return max(games, key=lambda x: games.count(x))

    def get_amount_of_games_won(self, player_name: str) -> int:
        """Return amount of games won."""
        return self.__get_person_with_name(player_name).wins

    def get_games_played_of_name(self, game_name: str) -> int:
        """Return the amount of times a game has been played."""
        return len(self.__get_matches(game_name))

    def get_amount_of_players_most_often_played_with(self, game_name: str) -> int:
        """Return amount of players the game is most commonly played with."""
        player_counts = []
        matches = self.__get_matches(game_name)
        for match in matches:
            player_counts.append(len(match.players))
        return max(player_counts, key=lambda x: player_counts.count(x))

    def __get_wins_and_losses(self, game_name: str):
        """Return wins, losses and total games played by player in dictionaries."""
        wins = {}
        losses = {}
        total_played = {}
        matches = self.__get_matches(game_name)
        if matches[0].result_type == "points":
            for match in matches:
                winner = match.players[match.result.index(max(match.result, key=int))]
                wins[winner] = wins.get(winner, 0) + 1
                loser = match.players[match.result.index(min(match.result, key=int))]
                losses[loser] = losses.get(loser, 0) + 1
        elif matches[0].result_type in ["places", "winner"]:
            for match in matches:
                winner = match.result[0]
                wins[winner] = wins.get(winner, 0) + 1
            if matches[0].result_type == "places":
                for match in matches:
                    loser = match.result[-1]
                    losses[loser] = losses.get(loser, 0) + 1
        for match in matches:
            for player in match.players:
                total_played[player] = total_played.get(player, 0) + 1
        return wins, losses, total_played

    def get_player_with_most_amount_of_wins(self, game_name: str) -> str:
        """Return name of the player who has won the game the most times."""
        wins = self.__get_wins_and_losses(game_name)[0]
        return max(wins, key=lambda x: wins[x])

    def get_most_frequent_winner(self, game_name: str) -> str:
        """Return name of the player whose winning % is the highest in the game."""
        wins = self.__get_wins_and_losses(game_name)[0]
        total_matches = self.__get_wins_and_losses(game_name)[2]
        ratios = {}
        for player in wins:
            ratios[player] = wins[player] / total_matches[player]
        return max(ratios, key=lambda x: ratios[x])

    def get_player_with_most_amount_of_losses(self, game_name: str) -> str:
        """Return name of the player who has lost the game the most times."""
        losses = self.__get_wins_and_losses(game_name)[1]
        return max(losses, key=lambda x: losses[x])

    def get_most_frequent_loser(self, game_name: str) -> str:
        """Return name of the player whose losing % is the highest in the game."""
        losses = self.__get_wins_and_losses(game_name)[1]
        total_matches = self.__get_wins_and_losses(game_name)[2]
        ratios = {}
        for player in losses:
            ratios[player] = losses[player] / total_matches[player]
        return max(ratios, key=lambda x: ratios[x])

    def get_record_holder(self, game_name: str) -> str:
        """
        Return name of the player who has the highest score in the given game.

        Can only be used on game with the points result type.
        """
        highest_score = 0
        record_holder = ""
        matches = self.__get_matches(game_name)
        for match in matches:
            for score in match.result:
                if int(score) > highest_score:
                    highest_score = int(score)
                    record_holder = match.players[match.result.index(score)]
        return record_holder


class Match:
    """Match class."""

    def __init__(self, game, players, result_type, result):
        """Class constructor."""
        self.game = game
        self.players = players
        self.result_type = result_type
        self.result = result

    def __repr__(self):
        """Class representation."""
        return self.game


class Player:
    """Player class."""

    def __init__(self, name: str, wins: int, losses: int, games_played: list[str]):
        """Class constructor."""
        self.name = name
        self.wins = wins
        self.losses = losses
        self.games_played = games_played

    def __repr__(self):
        """Class representation."""
        return self.name


if __name__ == '__main__':
    stat = Statistics("game_results.txt")
    print(
        stat.get_player_names())  # ['ago', 'jan', 'jaak', 'mati', 'mart', 'ekke', 'gregor', 'kati', 'riho', 'kristjan', 'hans', 'joosep']
    print(stat.get_game_names())  # ['7 wonders', 'terraforming mars', 'chess', 'game of thrones']
    print(stat.get_games_played_amount())  # 5
    print(stat.get_games_played_of_type("places"))  # 1
    print(stat.get_games_amount_played_by("joosep"))  # 4
    print(stat.get_favourite_game("joosep"))  # terraforming mars
    print(stat.get_games_played_of_name("terraforming mars"))  # 2
    print(stat.get_most_frequent_winner("terraforming mars"))
    print(stat.get_record_holder("terraforming mars"))
    print(stat.get_most_frequent_loser("terraforming mars"))
