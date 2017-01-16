import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from JavaLangLexer import JavaLangLexer
from JavaLangParser import JavaLangParser
from translator import Translator


def translate_java(file_name):
    """Translates Java code in file to Python code

    :file_name: str
    :returns: None
    """
    input = FileStream(file_name)
    lexer = JavaLangLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = JavaLangParser(tokens)
    tree = parser.compilationUnit()

    walker = ParseTreeWalker()
    listener = Translator()
    walker.walk(listener, tree)


if __name__ == '__main__':
    translate_java(sys.argv[1])
