import sys, os
import collections
from itertools import groupby
from pybtex.database.input import bibtex
from collections import Counter

parser = bibtex.Parser()

bib_data = parser.parse_file(sys.argv[1])

res = []
for item in bib_data.entries.items():
    if 'journal' in item[1].fields:
        #res.append((item[0],item[1].fields['journal'].lower()))
        res.append(item[1].fields['journal'].lower())

cnt = Counter(res)
cnt_srt = sorted(cnt.items(),key=lambda t:t[::-1])

for cnt in cnt_srt:
    print("%d  %s"%cnt[::-1])
