grammar IcS;

program  : 'Main' '{' statement* '}' ;
statement: write | instructionBlock ;

write    : '<w>' STRING ;
instructionBlock : '[:]' '{' ID (ID)* '}' ;

STRING   : '"' ~["]* '"' ;
ID       : [A-Z] ;
WS       : [ \t\r\n]+ -> skip ;



