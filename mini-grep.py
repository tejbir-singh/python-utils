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
    args_parser.add_argument('-e',
                             metavar='pattern',
                             nargs='*',
                             type=str,
                             help='regex pattern to match',
                             )

    args_parser.add_argument('-q',
                             action='store_true',
                             help='Output lines with regexp match but omit matching line numbers')

    # Execute the parse_args() method
    args = args_parser.parse_args()
    print(vars(args))
    return args


def main():
    parsed_args = parse_arguments()
    # regexp = parsed_args.Pattern
    # file_list = parsed_args.Files


main()