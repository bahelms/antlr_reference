import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Translate {
  public static void main(String[] args) throws Exception {
    // Create a CharStream that reads from stdin
    ANTLRInputStream input = new ANTLRInputStream(System.in);

    // Create a lexer that feeds off of input CharStream
    ArrayInitLexer lexer = new ArrayInitLexer(input);

    // Create a buffer of tokens pulled from the lexer
    CommonTokenStream tokens = new CommonTokenStream(lexer);

    // Create a parser that feeds off the tokens buffer
    ArrayInitParser parser = new ArrayInitParser(tokens);

    // begin parsing at init rule
    ParseTree tree = parser.init();

    // Create a generic parse tree walker that triggers callbacks
    ParseTreeWalker walker = new ParseTreeWalker();

    // Walk the tree created during parse, trigger callbacks
    walker.walk(new ShortToUnicodeString(), tree);
    System.out.println();  // print \n after translation
  }
}
