/* Convert short array inits like {1,2,4} to "\u0001\u0002\u0004" */
public class ShortToUnicodeString extends ArrayInitBaseListener {

  /* Translate { to " */
  @Override
  public void enterInit(ArrayInitParser.InitContext ctx) {
    System.out.println('"');
  }

  /* Translate } to " */
  @Override
  public void exitInit(ArrayInitParser.InitContext ctx) {
    System.out.println('"');
  }

  /* Translate integers to 4-digit hexadecimal strings prefixed with \\u */
  public void enterValue(ArrayInitParser.ValueContext ctx) {
    // Assumes no nested array inits
    int value = Integer.valueOf(ctx.INT().getText());
    System.out.printf("\\u%04x", value);
  }
} 
