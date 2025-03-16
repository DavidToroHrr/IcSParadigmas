# Generated from IcS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IcSParser import IcSParser
else:
    from IcSParser import IcSParser

# This class defines a complete generic visitor for a parse tree produced by IcSParser.

class IcSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IcSParser#program.
    def visitProgram(self, ctx:IcSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#statement.
    def visitStatement(self, ctx:IcSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#write.
    def visitWrite(self, ctx:IcSParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#instructionBlock.
    def visitInstructionBlock(self, ctx:IcSParser.InstructionBlockContext):
        return self.visitChildren(ctx)



del IcSParser