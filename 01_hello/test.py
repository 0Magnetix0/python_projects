#!/usr/bin/env python3
"""
Author: Sudhanshu Joshi
Purpose: For testing python programs
"""

import os
from subprocess import getstatusoutput, getoutput


prg = './hello.py'


#-----------------------------------------------------------------------------
def text_exists():
    """ exists """

    assert os.path.isfile(prg)


#-----------------------------------------------------------------------------
def test_runnable():
    """ Running using Python3 """

    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'hello, world!'


#-----------------------------------------------------------------------------
def test_executable():
    """ Executable or not """

    out = getoutput(prg)
    assert out.strip() == 'hello, world!'


#-----------------------------------------------------------------------------
def test_usage():
    """ Usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


#-----------------------------------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'hello, {val}!'

