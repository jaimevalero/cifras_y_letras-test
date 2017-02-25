#!/usr/bin/python
import pprint
import fnmatch
import os
from random import randint

import itertools

operandos = itertools.product('+-*/',repeat=5)
y = list(itertools.islice(operandos,0,100000000,1))
for j in y:
    print j
