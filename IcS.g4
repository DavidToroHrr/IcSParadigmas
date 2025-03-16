grammar IcS;

program  : 'Main' '{' statement* '}' ;
statement: write | instructionBlock ;

write    : '<w>' STRING ;
instructionBlock : '[:]' '{' ID (ID)* '}' ;

STRING   : '"' ~["]* '"' ;
ID       : [A-G] ('#'| 'b')? ; // Ahora reconoce sostenidos (#) y bemoles (b)
WS       : [ \t\r\n]+ -> skip ;
