#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='say hello')
parser.add_argument('name', help='name to greet')
args = parser.parse_args()
name = args.name

print(f'hello, {name}')
