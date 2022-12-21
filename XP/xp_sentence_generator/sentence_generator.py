"""Sentence generator."""


class SentenceGenerator:
    """A class for generating sentences based on a set of rules."""

    def __init__(self, rules_string: str):
        """Initialize the class and save all the rules and indexes for each rule.

        :param rules_string: A string containing the rules for generating sentences.
        """
        self.rule_dict = {}
        self.indexes = {}
        self.construct_dictionary(rules_string)

    def construct_dictionary(self, rules_string: str):
        """Process the rules string and populate the rule_dict dictionary.

        :param rules_string: A string containing the rules for generating sentences.
        """
        for rule in rules_string.split("\n"):
            if "|" in rule:
                key = rule.split(" =")[0]
                self.indexes[key] = 0
                self.rule_dict[key] = []
                for value in rule.split("= ")[1].split(" | "):
                    if key != value:
                        value = self.check_punctuation(value)
                        self.rule_dict[key].append(value)
            elif "=" in rule:
                key, value = rule.split(" = ")
                value = self.check_punctuation(value)
                if key not in self.rule_dict:
                    self.rule_dict[key] = value
                elif isinstance(self.rule_dict[key], list):
                    self.rule_dict[key].append(value)
                else:
                    self.indexes[key] = 0
                    self.rule_dict[key] = [self.rule_dict[key], value]
                if self.rule_dict[key] == key:
                    self.rule_dict[key] = "???"

    @staticmethod
    def check_punctuation(value: str):
        """Check if a value contains punctuation and add a placeholder if it does.

        :param value: The value to check for punctuation.

        :return: The value with a placeholder added if it contains punctuation, or the original value if it does not.
        """
        if any(["." in value, "," in value, "!" in value, "?" in value]):
            punctuation_indexes = []
            if "." in value:
                punctuation_indexes.append(value.index("."))
            if "," in value:
                punctuation_indexes.append(value.index(","))
            if "!" in value:
                punctuation_indexes.append(value.index("!"))
            if "?" in value:
                punctuation_indexes.append(value.index("?"))
            index = min(punctuation_indexes)
            value = value[:index] + " temp " + value[index:]
        return value

    def sentence_generator(self, syntax: str):
        """Generate a sentence based on the provided syntax.

        :param syntax: The syntax to use for generating the sentence.

        :return: The generated sentence.
        """
        syntaxes = syntax.split(" ")

        while True:
            result = ""

            # Loop through the given syntaxes and use the saved indexes to build the sentence.
            for syn in syntaxes:
                if syn not in self.rule_dict:
                    result += syn + " "
                elif isinstance(self.rule_dict[syn], list):
                    result += self.rule_dict[syn][self.indexes[syn] % len(self.rule_dict[syn])] + " "
                    self.indexes[syn] += 1
                else:
                    for word in self.rule_dict[syn].split(" "):
                        result += "".join(self.get_word(word))

            for word in result.split(" "):
                if word in self.rule_dict:
                    result = result[:result.index(word)] + next(self.sentence_generator(word)) + \
                        result[result.index(word) + len(word):]

            if " temp " in result:
                result = result.replace(" temp ", "")

            yield result[:-1]

    def get_word(self, word: str) -> str | list:
        """Use a rule to get a word.

        :param word: The rule to use for getting the word.

        :return: The generated word.
        """
        if word in self.indexes:
            self.indexes[word] += 1
            return self.rule_dict[word][(self.indexes[word] - 1) % len(self.rule_dict[word])] + " "
        something = []
        if word not in self.rule_dict:
            return word + " "
        else:
            for i in range(len(self.rule_dict[word].split(" "))):
                something.append(self.get_word(self.rule_dict[word].split(" ")[i]))
        return something


if __name__ == '__main__':
    rules = """
noun = koer | porgand | madis | kurk | tomat
target = koera | porgandit | madist | kurki | tomatit
verb = sööb | lööb | jagab | tahab | ei taha
adjective = ilus | kole | pahane | magus | sinu
targetadjective = ilusat | koledat | pahast | magusat | sinu
sentence = noun verb target .
beautifulsentence = adjective noun verb targetadjective target .
twosentences = sentence sentence
"""

    g = SentenceGenerator(rules)
    gg = g.sentence_generator("noun")
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    gg = g.sentence_generator("beautifulsentence noun")
    print(next(gg))
    print(next(gg))
    print(next(gg))

    rules = """
a = 1 2 3 4 5 | 6 7 8 9 0
b = 12 a a 13 | 14 a a a 14
c = b 20 b 21 | b 22 23 b
d = c c c c | c c c | c b c
aa = a b c d | d d c b a
bb = aa 100 | 101 aa aa
cc = aa bb aa | bb bb bb
dd = cc bb bb bb cc
aaa = aa bb cc dd cc dd | dd dd aa cc bb
"""
    g = SentenceGenerator(rules)
    gg = g.sentence_generator("aaa")
    print(next(gg))
