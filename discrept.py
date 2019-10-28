#! /usr/bin/python
import sys
from sys import argv

from discrept_pac.parsetree import Compiler
from discrept_pac.printpdf import print_pdf
from discrept_pac.tokenizer import parse


def main(args):
    i = 0
    file_name = "No File"
    while i < len(args):
        if '-' in args[i]:
            pass
        else:
            file_name = args[0].replace(".dis", "")
        i += 1

    with open(file_name + '.dis', 'r') as file:
        data = file.read()
        token_stream = parse(data)

        compiler = Compiler(token_stream, {'styles': sys.exec_prefix + '\\styles\\'})
        with open(file_name + '.html', 'w') as file_:
            file_.write(compiler.build())

    print_pdf(file_name)


if __name__ == '__main__':
    main(argv[1::])
