import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

public class ExtractInterfaceTool {
  public static void main(String[] args) throws Exception {
		String inputFile = null; 
		InputStream inStream = System.in;

		if (args.length > 0) inputFile = args[0];
		if (inputFile != null) inStream = new FileInputStream(inputFile);

    ANTLRInputStream input = new ANTLRInputStream(inStream);
    JavaLexer lexer = new JavaLexer(input);
    CommonTokenStream tokens = new CommonTokenStream(lexer);
    JavaParser parser = new JavaParser(tokens);
    ParseTree tree = parser.compilationUnit();

    ParseTreeWalker walker = new ParseTreeWalker();
    ExtractInterfaceListener extractor = new ExtractInterfaceListener(parser);
    walker.walk(extractor, tree);
  }
}
