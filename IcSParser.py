# Generated from IcS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,5,3,30,8,3,10,3,12,3,33,9,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,
        0,35,0,8,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,25,1,0,0,0,8,9,5,1,
        0,0,9,13,5,2,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,3,0,0,
        17,1,1,0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,0,0,0,20,19,1,0,
        0,0,21,3,1,0,0,0,22,23,5,4,0,0,23,24,5,6,0,0,24,5,1,0,0,0,25,26,
        5,5,0,0,26,27,5,2,0,0,27,31,5,7,0,0,28,30,5,7,0,0,29,28,1,0,0,0,
        30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,
        0,0,0,34,35,5,3,0,0,35,7,1,0,0,0,3,13,20,31
    ]

class IcSParser ( Parser ):

    grammarFileName = "IcS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Main'", "'{'", "'}'", "'<w>'", "'[:]'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_write = 2
    RULE_instructionBlock = 3

    ruleNames =  [ "program", "statement", "write", "instructionBlock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STRING=6
    ID=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IcSParser.StatementContext)
            else:
                return self.getTypedRuleContext(IcSParser.StatementContext,i)


        def getRuleIndex(self):
            return IcSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IcSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(IcSParser.T__0)
            self.state = 9
            self.match(IcSParser.T__1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(IcSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write(self):
            return self.getTypedRuleContext(IcSParser.WriteContext,0)


        def instructionBlock(self):
            return self.getTypedRuleContext(IcSParser.InstructionBlockContext,0)


        def getRuleIndex(self):
            return IcSParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = IcSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.write()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.instructionBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(IcSParser.STRING, 0)

        def getRuleIndex(self):
            return IcSParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = IcSParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(IcSParser.T__3)
            self.state = 23
            self.match(IcSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IcSParser.ID)
            else:
                return self.getToken(IcSParser.ID, i)

        def getRuleIndex(self):
            return IcSParser.RULE_instructionBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionBlock" ):
                return visitor.visitInstructionBlock(self)
            else:
                return visitor.visitChildren(self)




    def instructionBlock(self):

        localctx = IcSParser.InstructionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instructionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(IcSParser.T__4)
            self.state = 26
            self.match(IcSParser.T__1)
            self.state = 27
            self.match(IcSParser.ID)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 28
                self.match(IcSParser.ID)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(IcSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





