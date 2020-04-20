import sys, os
import collections
from itertools import groupby
from pybtex.database.input import bibtex

os.system('clear')
parser = bibtex.Parser()
bib_data = parser.parse_file(sys.argv[1])
years = []

print("     Number of all references are: ", len(bib_data.entries.keys()))

import re
tex = open(sys.argv[2]).read()
x =re.findall(r'\\cite\{([\w\d:,]+)\}',tex)
u = set(sum([t.split(',') for t in x],[]))
print(set(bib_data.entries.keys()) - u)
