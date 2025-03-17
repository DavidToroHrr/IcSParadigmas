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


    # Visit a parse tree produced by IcSParser#PrintStatement.
    def visitPrintStatement(self, ctx:IcSParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#ReadStatement.
    def visitReadStatement(self, ctx:IcSParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx:IcSParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:IcSParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#MusicStatement.
    def visitMusicStatement(self, ctx:IcSParser.MusicStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#IfStatement.
    def visitIfStatement(self, ctx:IcSParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#WhileStatement.
    def visitWhileStatement(self, ctx:IcSParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#printStmt.
    def visitPrintStmt(self, ctx:IcSParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#readStmt.
    def visitReadStmt(self, ctx:IcSParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#assignStmt.
    def visitAssignStmt(self, ctx:IcSParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#exprStmt.
    def visitExprStmt(self, ctx:IcSParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#NumberExpr.
    def visitNumberExpr(self, ctx:IcSParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#ArithmeticExpr.
    def visitArithmeticExpr(self, ctx:IcSParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:IcSParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#VariableExpr.
    def visitVariableExpr(self, ctx:IcSParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:IcSParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#musicStmt.
    def visitMusicStmt(self, ctx:IcSParser.MusicStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#ifStmt.
    def visitIfStmt(self, ctx:IcSParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#elseStmt.
    def visitElseStmt(self, ctx:IcSParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IcSParser#whileStmt.
    def visitWhileStmt(self, ctx:IcSParser.WhileStmtContext):
        return self.visitChildren(ctx)



del IcSParser