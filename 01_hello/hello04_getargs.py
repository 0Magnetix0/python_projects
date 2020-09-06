#!/usr/bin/env python3

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='say hello')
    parser.add_argument('-n', '--name', metavar='name', default='world',
                        help='name to greet')
    return parser.parse_args()


def main():
    args = get_args()
    name = args.name
    print(f'hello, {name}')


if __name__ == '__main__':
    main()
