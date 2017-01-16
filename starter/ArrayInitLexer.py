# Generated from ArrayInit.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\7")
        buf.write("\37\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\6\5\25\n\5\r\5\16\5\26\3\6\6\6")
        buf.write("\32\n\6\r\6\16\6\33\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7")
        buf.write("\3\2\4\3\2\62;\5\2\13\f\17\17\"\" \2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2")
        buf.write("\5\17\3\2\2\2\7\21\3\2\2\2\t\24\3\2\2\2\13\31\3\2\2\2")
        buf.write("\r\16\7}\2\2\16\4\3\2\2\2\17\20\7.\2\2\20\6\3\2\2\2\21")
        buf.write("\22\7\177\2\2\22\b\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2\2")
        buf.write("\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\n\3\2\2")
        buf.write("\2\30\32\t\3\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2")
        buf.write("\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\b\6\2\2\36\f\3")
        buf.write("\2\2\2\5\2\26\33\3\b\2\2")
        return buf.getvalue()


class ArrayInitLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    INT = 4
    WS = 5

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "','", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "INT", "WS" ]

    grammarFileName = "ArrayInit.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


