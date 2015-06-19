from parsetron import Set, Regex, Optional, OneOrMore, Grammar, RobustParser


def regex2int(result):
    # result holds Regex(r'\d+ times') lexicon
    num = int(result.get().split()[0])
    result.set(num)


def times2int(result):
    r = result.get().lower()
    mapper = {"once": 1, "twice": 2, "three times": 3}
    num = mapper[r]
    result.set(num)


def color2rgb(result):
    r = result.get().lower()
    # r now holds color lexicons
    mapper = {
        "red": (255, 0, 0),
        "yellow": (255, 255, 0),
        "blue": (0, 0, 255),
        "orange": (255, 165, 0),
        "purple": (128, 0, 128)
    }
    color = mapper[r]
    result.set(color)


class LightAdvancedGrammar(Grammar):

    action = Set(['change', 'flash', 'set', 'blink'])
    light = Set(['top', 'middle', 'bottom'])

    color = Regex(r'(red|yellow|blue|orange|purple|...)').\
        set_result_action(color2rgb)
    times = Set(['once', 'twice', 'three times']).\
        set_result_action(times2int) | \
        Regex(r'\d+ times').set_result_action(regex2int)

    one_parse = action + light + Optional(times) + color
    GOAL = OneOrMore(one_parse)

    @staticmethod
    def test():
        parser = RobustParser((LightAdvancedGrammar()))
        tree, result = parser.parse("flash my top light twice in red and "
                                    "blink middle light 20 times in yellow")
        print tree
        print result
        assert result.one_parse[0].color == (255, 0, 0)
        assert result.one_parse[0].times == 2
        assert result.one_parse[1].color == (255, 255, 0)
        assert result.one_parse[1].times == 20
        print



if __name__ == "__main__":
    LightAdvancedGrammar.test()