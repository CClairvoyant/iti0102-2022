"""Janguru task."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """
    Calculate the meeting position of 2 jangurus.

    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet
    """

    time = 0
    while time < 10000000:
        if time % sleep1 == 0:
            pos1 += jump_distance1
        if time % sleep2 == 0:
            pos2 += jump_distance2
        time += 1
        if pos1 == pos2:
            return pos1
    return -1


if __name__ == "__main__":
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))  # => 50
    print(meet_me(1, 1, 1, 1, 1, 1))  # => 2
    print(meet_me(1, 1, 1000, 10, 1, 9000))  # => 12
    print(meet_me(1, 1, 1000, 10, 1, 9001))  # => 11
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 2, 1, 1, 3, 1))  # => -1
    print(meet_me(273, 136, 208, 245, 75, 112))  # => 545
    print(meet_me(262, 228, 163, 295, 15, 11))  # => 490
    print(meet_me(239, 22, 41, 149, 158, 285))  # => 1097
    print(meet_me(250, 35, 26, 284, 149, 111))  # => 880
    print(meet_me(92, 151, 200, 28, 109, 144))  # => 6132
    print(meet_me(201, 87, 209, 118, 107, 257))  # => 5682
