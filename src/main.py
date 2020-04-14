import sys
from lark import Lark


class Parser:
    input_files = []

    def __init__(self, files):
        self.input_files = files

    def parse(self):
        for f in self.input_files:
            print("Parsing " + f + "...")
            self.parse_file(f)

    def parse_file(self, filename):
        with open(filename) as fp:
            line = fp.readline()
            while line:
                print(line)
                line = fp.readline()

    def generate_ucl(self):
        return


def main():
    if len(sys.argv) < 2:
        print("Wrong number of arguments!")
    else:
        input_files = sys.argv[1:]
        print("Received files: " + str(input_files))
        parser = Parser(input_files)
        parser.parse()


if __name__ == '__main__':
    main()
