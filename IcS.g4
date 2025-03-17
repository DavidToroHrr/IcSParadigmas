// Definimos la gramática para el lenguaje IcS
grammar IcS;

// Reglas principales
program: 'Main' '{' statement* '}' ;

statement
    : printStmt SEMICOLON   # PrintStatement
    | readStmt SEMICOLON    # ReadStatement
    | assignStmt SEMICOLON  # AssignmentStatement
    | exprStmt SEMICOLON    # ExpressionStatement
    | musicStmt SEMICOLON   # MusicStatement
    | ifStmt               # IfStatement
    | whileStmt            # WhileStatement
    ;

// Instrucciones básicas
printStmt: '<w>' STRING | '<w>' expr;
readStmt: '<r>' ID;
assignStmt: ID ':=' expr;
exprStmt: expr;

// Expresiones aritméticas y lógicas
expr: expr ('+'|'-'|'*'|'/') expr  # ArithmeticExpr
    | expr ('=='|'!='|'<'|'>'|'<='|'>=') expr  # RelationalExpr
    | '(' expr ')' # ParenthesizedExpr
    | ID          # VariableExpr
    | NUMBER      # NumberExpr
    ;

// Instrucción para generar música
musicStmt: '[:]' '{' ID (ID)* '}';

// Condicionales e iteraciones
ifStmt: 'If' expr '::' statement* elseStmt?;
elseStmt: 'else' '::' statement*;
whileStmt: 'While' expr '::' statement*;

// Tokens básicos
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' .*? '"';
SEMICOLON: ';';  // Definiendo ';' como token
WS: [ \t\r\n]+ -> skip;
COMMENT: '***' .*? '\n' -> skip;
