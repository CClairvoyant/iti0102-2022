"""Sentence generator."""


class SentenceGenerator:
    """The main class."""

    def __init__(self, rules_string: str):
        """Initialize the class and save all the rules and indexes for each rule."""
        self.rules = rules_string.split("\n")
        self.rule_dict = {}
        self.indexes = {}

        # Add rules to rule_dict (values as list) and to indexes if they are plain words, only to rule_dict
        # (values as strings) if they contain previously defined rules.
        for rule in self.rules:
            if "|" in rule:
                key = rule.split(" =")[0]
                self.indexes[key] = 0
                self.rule_dict[key] = []
                for word in rule.split("= ")[1].split(" | "):
                    if key != word:
                        self.rule_dict[key].append(word)
            else:
                key = rule.split(" =")[0]
                # test_lines_with_some_rules
                try:
                    self.rule_dict[key] = rule.split("= ")[1]
                    if self.rule_dict[key] == key:
                        self.rule_dict[key] = "???"
                except IndexError:
                    pass
        print(self.rule_dict)

    def sentence_generator(self, syntax: str):
        """Build the sentence."""
        count = 0
        if "." in syntax:
            count = syntax.count(".")
            syntax = syntax.strip(".")

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

            yield result[:-1] + "." * count

    def get_word(self, word):
        """Use a rule to get a word."""
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
a = tere
b = b | 2 | 3
    """

    g = SentenceGenerator(rules)
    gg = g.sentence_generator("a b")
    print(next(gg))
    print(next(gg))
    print(next(gg))


