"""Caesar cipher."""


def encode_letter(message: str, shift: int) -> str:
    if message.isalpha():
        old_pos = ord(message) - ord("a")
        new_pos = (old_pos + shift) % 26
        return chr(new_pos + ord("a"))
    else:
        return message


def encode(message: str, shift: int) -> str:
    coded_text = ""
    for character in message:
        coded_text += encode_letter(character, shift)
    return coded_text


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.
