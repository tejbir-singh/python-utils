"""
"mini-grep"
-----------

Usage:

    ./mini-grep [-q] -e PATTERN [FILE...]

`mini-grep` goes through every argument in FILE and prints the whole
line in which PATTERN is found. By default `mini-grep` also outputs
the line number of each printed line.

- PATTERN has to be a valid regex
- FILE can be zero or more arguments. If zero args are given,
  `mini-grep` will parse entries from the standard input.
- If given, the `-q` options only outputs lines but omits the matching
  line numbers.
"""

import os
import argparse


def parse_arguments():
    # Create the parser
    args_parser = argparse.ArgumentParser(prog='mini-grep',
                                          usage='%(prog)s [-q] -e PATTERN [FILE...]',
                                          description='Find regex PATTERN in files and output line number '
                                                      'for each line where match is found',
                                          add_help=True)
    # Add the arguments
    args_parser.add_argument('PATTERN',
                             metavar='-e PATTERN',
                             type=str,
                             help='regex pattern to match',
                             )

    args_parser.add_argument('-q',
                             action='store_true',
                             help='Output lines with regexp match but omit matching line numbers')

    args_parser.add_argument('-e',
                             action='append',
                             type=list,
                             help='list of input to search for regexp, either a file(s) or standard input',
                             )

    # Execute the parse_args() method
    args = args_parser.parse_args()
    return args


def main():
    parsed_args = parse_arguments()
    regexp = parsed_args.Pattern
    file_list = parsed_args.Files


main()