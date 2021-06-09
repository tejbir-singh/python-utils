# mini_ls.py

import argparse
import os
import pathlib
import time
from typing import Union


def process_file_path(f_paths: Union[list, str], run_recursively=True) -> None:
    """
    List owner, permissions, and last modified time information about file paths
    :param f_paths:
    :param run_recursively:
    :return:
    """
    for fpath in f_paths:
        file = pathlib.Path(fpath)
        status = os.stat(file)
        if file.exists():
            print(f"{file.name} {file.owner()} {oct(status.st_mode)[-3:]} {time.ctime(file.stat().st_mtime)}")
        else:
            print('File does not exist')

        if file.is_dir() and run_recursively:
            dir_paths = os.listdir(file)
            print(f"{dir_paths}")
            process_file_path(dir_paths, run_recursively=True)


def init_argparse() -> argparse.ArgumentParser:
    # Create the parser
    parser = argparse.ArgumentParser(prog='mini-ls',
                                     usage='%(prog)s [-r] [FILE...]',
                                     description='List owner, permission, and last modified time about the paths'
                                                 'given in FILE',
                                     add_help=True)
    # Add the arguments
    parser.add_argument('-r', '--recursive',
                        action='store_true',
                        help='run recursively if path is a directory'
                        )

    parser.add_argument('-p', '--File-Path',
                        action='store',
                        type=str,
                        nargs='*',
                        help='One or more files')

    return parser


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    file_path = []

    if not args.File_Path:
        file_path = os.getcwd()
        if args.recursive:
            process_file_path([file_path], run_recursively=True)
        else:
            process_file_path([file_path], run_recursively=False)
    else:
        if args.recursive:
            process_file_path(args.File_Path, run_recursively=True)
        else:
            process_file_path(args.File_Path, run_recursively=False)

    # print(vars(args))


if __name__ == "__main__":
    main()
