# Generated from IcS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IcSParser import IcSParser
else:
    from IcSParser import IcSParser

# This class defines a complete listener for a parse tree produced by IcSParser.
class IcSListener(ParseTreeListener):

    # Enter a parse tree produced by IcSParser#program.
    def enterProgram(self, ctx:IcSParser.ProgramContext):
        pass

    # Exit a parse tree produced by IcSParser#program.
    def exitProgram(self, ctx:IcSParser.ProgramContext):
        pass


    # Enter a parse tree produced by IcSParser#statement.
    def enterStatement(self, ctx:IcSParser.StatementContext):
        pass

    # Exit a parse tree produced by IcSParser#statement.
    def exitStatement(self, ctx:IcSParser.StatementContext):
        pass


    # Enter a parse tree produced by IcSParser#write.
    def enterWrite(self, ctx:IcSParser.WriteContext):
        pass

    # Exit a parse tree produced by IcSParser#write.
    def exitWrite(self, ctx:IcSParser.WriteContext):
        pass


    # Enter a parse tree produced by IcSParser#instructionBlock.
    def enterInstructionBlock(self, ctx:IcSParser.InstructionBlockContext):
        pass

    # Exit a parse tree produced by IcSParser#instructionBlock.
    def exitInstructionBlock(self, ctx:IcSParser.InstructionBlockContext):
        pass



del IcSParser