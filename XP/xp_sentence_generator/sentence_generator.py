"""Sentence generator."""


class SentenceGenerator:
    """The main class."""

    def __init__(self, rules_string: str):
        """Initialize the class and save all the rules and indexes for each rule."""
        self.rules = rules_string.strip().split("\n")
        self.rule_dict = {}
        self.indexes = {}

        # Add rules to rule_dict (values as list) and to indexes if they are plain words, only to rule_dict
        # (values as strings) if they contain previously defined rules.
        for rule in self.rules:
            if "|" in rule:
                key = rule.strip().split(" =")[0]
                self.indexes[key] = 0
                self.rule_dict[key] = []
                for word in rule.split("= ")[1].split(" | "):
                    self.rule_dict[key].append(word)
            else:
                key = rule.strip().split(" =")[0]
                self.rule_dict[key] = rule.split("= ")[1]

    def sentence_generator(self, syntax: str):
        """Build the sentence."""
        syntaxes = syntax.split()

        while True:
            result = ""

            # Loop through the given syntaxes and use the saved indexes to build the sentence.
            for syn in syntaxes:
                if isinstance(self.rule_dict[syn], list):
                    result += self.rule_dict[syn][self.indexes[syn] % len(self.rule_dict[syn])] + " "
                    self.indexes[syn] += 1
                else:
                    for word in self.rule_dict[syn].split():
                        if word not in self.rule_dict:
                            result += word + " "
                        else:
                            result += self.rule_dict[word][self.indexes[word] % len(self.rule_dict[word])] + " "
                            self.indexes[word] += 1

            yield result[:-1]


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
    gg = g.sentence_generator("twosentences")
    print(next(gg))
