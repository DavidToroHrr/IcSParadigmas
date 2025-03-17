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


    # Enter a parse tree produced by IcSParser#PrintStatement.
    def enterPrintStatement(self, ctx:IcSParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#PrintStatement.
    def exitPrintStatement(self, ctx:IcSParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#ReadStatement.
    def enterReadStatement(self, ctx:IcSParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#ReadStatement.
    def exitReadStatement(self, ctx:IcSParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#AssignmentStatement.
    def enterAssignmentStatement(self, ctx:IcSParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#AssignmentStatement.
    def exitAssignmentStatement(self, ctx:IcSParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:IcSParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:IcSParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#MusicStatement.
    def enterMusicStatement(self, ctx:IcSParser.MusicStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#MusicStatement.
    def exitMusicStatement(self, ctx:IcSParser.MusicStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#IfStatement.
    def enterIfStatement(self, ctx:IcSParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#IfStatement.
    def exitIfStatement(self, ctx:IcSParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#WhileStatement.
    def enterWhileStatement(self, ctx:IcSParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by IcSParser#WhileStatement.
    def exitWhileStatement(self, ctx:IcSParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by IcSParser#printStmt.
    def enterPrintStmt(self, ctx:IcSParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#printStmt.
    def exitPrintStmt(self, ctx:IcSParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#readStmt.
    def enterReadStmt(self, ctx:IcSParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#readStmt.
    def exitReadStmt(self, ctx:IcSParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#assignStmt.
    def enterAssignStmt(self, ctx:IcSParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#assignStmt.
    def exitAssignStmt(self, ctx:IcSParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#exprStmt.
    def enterExprStmt(self, ctx:IcSParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#exprStmt.
    def exitExprStmt(self, ctx:IcSParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#NumberExpr.
    def enterNumberExpr(self, ctx:IcSParser.NumberExprContext):
        pass

    # Exit a parse tree produced by IcSParser#NumberExpr.
    def exitNumberExpr(self, ctx:IcSParser.NumberExprContext):
        pass


    # Enter a parse tree produced by IcSParser#ArithmeticExpr.
    def enterArithmeticExpr(self, ctx:IcSParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by IcSParser#ArithmeticExpr.
    def exitArithmeticExpr(self, ctx:IcSParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by IcSParser#ParenthesizedExpr.
    def enterParenthesizedExpr(self, ctx:IcSParser.ParenthesizedExprContext):
        pass

    # Exit a parse tree produced by IcSParser#ParenthesizedExpr.
    def exitParenthesizedExpr(self, ctx:IcSParser.ParenthesizedExprContext):
        pass


    # Enter a parse tree produced by IcSParser#VariableExpr.
    def enterVariableExpr(self, ctx:IcSParser.VariableExprContext):
        pass

    # Exit a parse tree produced by IcSParser#VariableExpr.
    def exitVariableExpr(self, ctx:IcSParser.VariableExprContext):
        pass


    # Enter a parse tree produced by IcSParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:IcSParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by IcSParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:IcSParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by IcSParser#musicStmt.
    def enterMusicStmt(self, ctx:IcSParser.MusicStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#musicStmt.
    def exitMusicStmt(self, ctx:IcSParser.MusicStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#ifStmt.
    def enterIfStmt(self, ctx:IcSParser.IfStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#ifStmt.
    def exitIfStmt(self, ctx:IcSParser.IfStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#elseStmt.
    def enterElseStmt(self, ctx:IcSParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#elseStmt.
    def exitElseStmt(self, ctx:IcSParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by IcSParser#whileStmt.
    def enterWhileStmt(self, ctx:IcSParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by IcSParser#whileStmt.
    def exitWhileStmt(self, ctx:IcSParser.WhileStmtContext):
        pass



del IcSParser