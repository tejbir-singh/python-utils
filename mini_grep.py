# mini_grep.py

import os.path
import argparse
import re
import sys
import pathlib


def process_file(files: list, regex: str, skip_line_number=False) -> None:
    """
    Search regex pattern on files and print line and line number if a match is found
    :param files:
    :param regex:
    :param skip_line_number:
    :return:
    """

    for file in files:
        if pathlib.Path(file).exists():
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
        else:
            print("Invalid file path")
            continue


def process_stdin(regex: str) -> None:
    """
    Match regex pattern to input from standard input
    :param regex:
    :return:
    """

    stdin_fileno = sys.stdin
    for line in stdin_fileno:
        regex_match = re.search(regex, line)
        if regex_match:
            print(f"{line.rstrip()}")


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
                        nargs=1,
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
    files_lst = []

    if args.regex and len(args.regex) == 1:
        regex_str = args.regex[0]

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
    elif is_valid_regex and not args.file:
        process_stdin(regex_str)


if __name__ == "__main__":
    main()
