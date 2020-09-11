#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "sondos with help from gabby and Mike boring"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")

    parser.add_argument(
        'text', type=str, help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')

    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')

    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    # The nargs option instructs the parser to expect 1 or more
    # filenames. It will also expand wildcards just like the shell.
    # e.g. 'baby*.html' will work.
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)
    new_string = ""

    if not ns:
        parser.print_usage()
        sys.exit(1)
    string = args[0]

    if len(args) == 1:
        new_string = string
    if len(args) > 2:
        new_string = string
        for x in args:
            if x == "-u" or "--upper":
                new_string = new_string.upper()
                continue
            if x == "-t" or "--title":
                new_string = new_string.title()
                continue
            if x == "-l" or "--lower":
                new_string = new_string.lower()
                continue
    else:
        if ns.lower:
            new_string = string.lower()
        if ns.upper:
            new_string = string.upper()
        if ns.title:
            new_string = string.title()
        if ns.title is False and ns.upper is False is ns.lower is False:
            new_string = string

    print(new_string)


if __name__ == '__main__':
    main(sys.argv[1:])
