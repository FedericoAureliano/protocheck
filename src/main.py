import sys
from antlr4 import *
from PParser import PParser
from PLexer import PLexer
from PUclidParserListener import PUclidParserListener
from PModel import *


def main():
    input_stream = FileStream("../examples/pingpong/pingpong.p")
    lexer = PLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PParser(stream)
    tree = parser.program()
    model = PModel()
    listener = PUclidParserListener(parser, model)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


if __name__ == '__main__':
    main()
