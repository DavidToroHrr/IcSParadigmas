# Generated from IcS.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,5,1,5,5,5,37,8,5,10,5,12,5,40,9,5,1,5,1,5,1,
        6,1,6,1,7,4,7,47,8,7,11,7,12,7,48,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,
        9,5,11,6,13,7,15,8,1,0,3,1,0,34,34,1,0,65,90,3,0,9,10,13,13,32,32,
        53,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,22,1,0,0,0,5,
        24,1,0,0,0,7,26,1,0,0,0,9,30,1,0,0,0,11,34,1,0,0,0,13,43,1,0,0,0,
        15,46,1,0,0,0,17,18,5,77,0,0,18,19,5,97,0,0,19,20,5,105,0,0,20,21,
        5,110,0,0,21,2,1,0,0,0,22,23,5,123,0,0,23,4,1,0,0,0,24,25,5,125,
        0,0,25,6,1,0,0,0,26,27,5,60,0,0,27,28,5,119,0,0,28,29,5,62,0,0,29,
        8,1,0,0,0,30,31,5,91,0,0,31,32,5,58,0,0,32,33,5,93,0,0,33,10,1,0,
        0,0,34,38,5,34,0,0,35,37,8,0,0,0,36,35,1,0,0,0,37,40,1,0,0,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,34,
        0,0,42,12,1,0,0,0,43,44,7,1,0,0,44,14,1,0,0,0,45,47,7,2,0,0,46,45,
        1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,
        50,51,6,7,0,0,51,16,1,0,0,0,3,0,38,48,1,6,0,0
    ]

class IcSLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    STRING = 6
    ID = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Main'", "'{'", "'}'", "'<w>'", "'[:]'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "STRING", "ID", 
                  "WS" ]

    grammarFileName = "IcS.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


