import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

public class CalcJoyRide {
	public static void main(String[] args) throws Exception {
		String inputFile = null; 
		InputStream is = System.in;

		if (args.length>0) inputFile = args[0];
		if (inputFile!=null) is = new FileInputStream(inputFile);

		ANTLRInputStream input = new ANTLRInputStream(is); 
		CalcLexer lexer = new CalcLexer(input); 
		CommonTokenStream tokens = new CommonTokenStream(lexer); 
		CalcParser parser = new CalcParser(tokens); 

		// parse; start at prog
		ParseTree tree = parser.prog(); 

		// print tree as text
		System.out.println(tree.toStringTree(parser)); 
	}
}
