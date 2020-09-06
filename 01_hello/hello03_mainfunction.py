#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description='say hello')
    parser.add_argument('-n', '--name', metavar='name', default='world' , help='name to greet')
    args = parser.parse_args()
    name = args.name
    print(f'hello, {name}')

if __name__ == '__main__':
    main()
