#!/usr/bin/env python3
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
# Terminating a Program with an Error Message
# import sys
# sys.stderr.write('It failed!\n')
# raise SystemExit(1)
