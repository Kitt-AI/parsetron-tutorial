from parsetron import Set, Regex, Optional, OneOrMore, Grammar, RobustParser


class LightGrammar(Grammar):

    action = Set(['change', 'flash', 'set', 'blink'])
    light = Set(['top', 'middle', 'bottom'])
    color = Regex(r'(red|yellow|blue|orange|purple|...)')
    times = Set(['once', 'twice', 'three times']) | Regex(r'\d+ times')
    one_parse = action + light + Optional(times) + color
    GOAL = OneOrMore(one_parse)

    @staticmethod
    def test():
        parser = RobustParser((LightGrammar()))
        sents = [
            "set my top light to red",
            "set my top light to red and change middle light to yellow",
            "set my top light to red and change middle light to yellow and "
            "flash bottom light twice in blue"
        ]
        for sent in sents:
            tree, result = parser.parse(sent)
            print '"%s"' % sent
            print "parse tree:"
            print tree
            print "parse result:"
            print result
            print


if __name__ == "__main__":
    LightGrammar.test()