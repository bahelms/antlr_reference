// Grammars always start with a grammar header that must match the file name
grammar ArrayInit;

// A rule called 'init' that matches csvs between {...}
init : '{' value (',' value)* '}' ;  // must match at least one value

// A value can be either a nested array/struct or a simple integer
value : init
      | INT
      ;

// Parser rules start with lowercase letters, lexer rules with uppercase
INT : [0-9]+ ;              // Define token INT as one or more digits
WS  : [ \t\r\n]+ -> skip ;  // Define whitespace rule and skip it
