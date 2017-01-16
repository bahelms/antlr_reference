from JavaLangListener import JavaLangListener


class Translator(JavaLangListener):
    """Translates Java code into Python code"""

    def enterClassDeclaration(self, ctx):
        """Convert Java class declaration into Python

        :ctx: ClassDeclarationContext
        :returns: None
        """
        parent_class = ctx.entityType().getText()
        print('class {}({}):'.format(ctx.Identifier(), parent_class))

    def exitClassDeclaration(self, ctx):
        print()
        print()

    def enterMethodDeclaration(self, ctx):
        print('    ', end='')
        print('def {}(self):'.format(ctx.Identifier()))
        print('        ', end='')
        print('body')
        print(ctx.formalParameters().getText())
