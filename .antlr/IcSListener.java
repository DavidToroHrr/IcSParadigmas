// Generated from c:/ANTLR/IcSParadigmas/IcS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link IcSParser}.
 */
public interface IcSListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link IcSParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(IcSParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(IcSParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PrintStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatement(IcSParser.PrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PrintStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatement(IcSParser.PrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ReadStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReadStatement(IcSParser.ReadStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ReadStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReadStatement(IcSParser.ReadStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AssignmentStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentStatement(IcSParser.AssignmentStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AssignmentStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentStatement(IcSParser.AssignmentStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExpressionStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(IcSParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExpressionStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(IcSParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MusicStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterMusicStatement(IcSParser.MusicStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MusicStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitMusicStatement(IcSParser.MusicStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IfStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(IcSParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IfStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(IcSParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(IcSParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code WhileStatement}
	 * labeled alternative in {@link IcSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(IcSParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(IcSParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(IcSParser.PrintStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#readStmt}.
	 * @param ctx the parse tree
	 */
	void enterReadStmt(IcSParser.ReadStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#readStmt}.
	 * @param ctx the parse tree
	 */
	void exitReadStmt(IcSParser.ReadStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void enterAssignStmt(IcSParser.AssignStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#assignStmt}.
	 * @param ctx the parse tree
	 */
	void exitAssignStmt(IcSParser.AssignStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(IcSParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(IcSParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NumberExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNumberExpr(IcSParser.NumberExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NumberExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNumberExpr(IcSParser.NumberExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArithmeticExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpr(IcSParser.ArithmeticExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArithmeticExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpr(IcSParser.ArithmeticExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenthesizedExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesizedExpr(IcSParser.ParenthesizedExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenthesizedExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesizedExpr(IcSParser.ParenthesizedExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code VariableExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVariableExpr(IcSParser.VariableExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code VariableExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVariableExpr(IcSParser.VariableExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpr(IcSParser.RelationalExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code RelationalExpr}
	 * labeled alternative in {@link IcSParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpr(IcSParser.RelationalExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#musicStmt}.
	 * @param ctx the parse tree
	 */
	void enterMusicStmt(IcSParser.MusicStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#musicStmt}.
	 * @param ctx the parse tree
	 */
	void exitMusicStmt(IcSParser.MusicStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(IcSParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(IcSParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link IcSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(IcSParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link IcSParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(IcSParser.WhileStmtContext ctx);
}