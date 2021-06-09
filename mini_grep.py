# mini_grep.py

import os.path
import argparse
import re
import sys


def process_file(files: list, regex: str, skip_line_number=False) -> None:
    for file in files:
        if os.path.isfile(file):
            with open(file) as f:
                lines = f.readlines()
                try:
                    for idx, line in enumerate(lines):
                        regex_match = re.search(regex, line)
                        if regex_match and not skip_line_number:
                            print(f"{idx + 1, line.rstrip()}")
                        elif regex_match and skip_line_number:
                            print(f"{line.rstrip()}")
                except():
                    print('Match not found')


def process_stdin(stdin: str, regex: str) -> None:
    pass

def init_argparse() -> argparse.ArgumentParser:
    # Create the parser
    parser = argparse.ArgumentParser(prog='mini-grep',
                                          usage='%(prog)s [-q] -e PATTERN [FILE...]',
                                          description='Find regex PATTERN in files and output line number '
                                                      'for each line where match is found',
                                          add_help=True)
    # Add the arguments
    parser.add_argument('-e', '--regex',
                        type=str,
                        nargs='+',
                        action='store',
                        help='regex pattern to match'
                        )

    parser.add_argument('-q', '--skip-line-number',
                        action='store_true',
                        help='Output lines with regexp match but omit matching line numbers')

    parser.add_argument('-f', '--file',
                        action='store',
                        type=str,
                        nargs='*',
                        help='One or more files')

    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    regex_str = ''
    std_input = ''
    files_lst = []
    # print(vars(args))

    if args.regex and len(args.regex) == 1:
        regex_str = args.regex[0]
    elif len(args.regex) > 1:
        regex_str = args.regex[0]
        std_input = args.regex[1:]

    if args.file:
        files_lst = args.file

    try:
        re.compile(regex_str)
        is_valid_regex = True
    except re.error:
        print('Invalid regex. Exiting.')
        sys.exit(1)

    if is_valid_regex and args.file:
        if args.skip_line_number:
            process_file(files_lst, regex_str, skip_line_number=True)
        else:
            process_file(files_lst, regex_str, skip_line_number=False)
    if is_valid_regex and std_input:
        process_stdin(std_input, regex_str)


if __name__ == "__main__":
    main()
