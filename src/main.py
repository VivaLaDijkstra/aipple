""" Entry point for the application """

import argparse
import os
import sys


def parse_args(args):
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="")
    subparsers = parser.add_subparsers(dest="command")

    check_parser = subparsers.add_parser("review", help="Review the syntax of a code file")
    check_parser.add_argument("--file_path", help="The code file to review")
    check_parser.add_argument("--reviewer", nargs="*", help="reviewer name")
    check_parser.add_argument("--opt", nargs="*", help="The output filename")
    check_parser.add_argument("--md", nargs="*", help="The output markdown")

    format_parser = subparsers.add_parser("revise", help="Format a file")
    format_parser.add_argument("--file_path", type=str, help="The file to revise")
    check_parser.add_argument("--reviewer", nargs="*", help="reviewer name")
    format_parser.add_argument("--revisor", nargs="*", help="revisor name")
    format_parser.add_argument("--md", nargs="*", help="The output markdown")


def main():
    args = parse_args()


if __name__ == "__main__":
    SystemExit(main())