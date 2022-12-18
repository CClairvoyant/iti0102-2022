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
            else:
                # test_lines_with_some_rules
                if "=" in rule:
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
    rules = 'a = 1' + "\n" + \
            'a = 2' + "\n" + \
            'a = 3' + "\n" + \
            'b = a' + "\n" + \
            'b = 4' + "\n" + \
            'd = a a' + "\n" + \
            'd = b'
    g = SentenceGenerator(rules)
    gg = g.sentence_generator("d")
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
