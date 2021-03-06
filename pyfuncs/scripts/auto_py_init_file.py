# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import  # noqa
# import re
import sys
import argparse
from os import walk
from os.path import abspath, join, isdir, exists


# SUFFIX_REGIX = re.compile(r'^\*[\w\W]{1,}$')


def main():
    parser = argparse.ArgumentParser(
        description='auto_py_init_file.')
    parser.add_argument('path', nargs='?', help='file path default "./"')
    parser.add_argument(
        '--suffix', help='suffix filter(ex: .git,.svn) '
        'default(.git,.svn,.vscode,__pycache__)')
    args = parser.parse_args()

    if not args.path:
        args.path = './'

    if args.path != './' and not isdir(args.path):
        print('You must supply a path[{}][{}]\n'.format(
            args.path, isdir(args.path)), file=sys.stderr)
        parser.print_help()
        return

    defult_suffix = ['.git', '.svn', '.vscode', '__pycache__']
    if not args.suffix:
        args.suffix = defult_suffix
    else:
        args.suffix = args.suffix.split(',') + defult_suffix
        # args.suffix = [val[val.rfind('.'):] for val in args.suffix
        #                if re.match(SUFFIX_REGIX, val) is not None]

    for root, dirs, _ in walk(args.path):
        for key in args.suffix:
            if key in dirs:
                dirs.remove(key)

        for name in dirs:
            root = abspath(root)
            filepath = join(root, name)

            filepath += '/__init__.py'
            if exists(filepath):
                continue

            try:
                print(filepath)
            except IOError as ex:
                print('ioerrir', ex)

            open(filepath, 'w').close()


if __name__ == '__main__':
    main()
