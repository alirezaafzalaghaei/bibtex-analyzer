import sys, os
import collections
from itertools import groupby
from pybtex.database.input import bibtex

os.system('clear')
parser = bibtex.Parser()
bib_data = parser.parse_file(sys.argv[1])
all_authors = []
min_ref = 2 if len(sys.argv) == 2 else int(sys.argv[2])

print("     Number of all references are: ", len(bib_data.entries.keys()))
for article in bib_data.entries.values():
    #authors = article.persons['author'][0].last_names[0]
    authors = ["%s"%str(author) for author in article.persons['author']]
    all_authors.extend(authors)

counts = collections.Counter(all_authors)
counts = sorted(counts.items(),key=lambda x:(x[1],x[0]))
with open('references.txt','w') as f:
    print('|','-'*44,'|')
    print('|','-'*44,'|',file=f)
    
    for key, group in groupby(counts, lambda x: x[1]):
        for thing in group:
            if key >= min_ref:
                print("| %-30s cited %d times |" % (thing[0], key))
            print("| %-30s cited %d times |" % (thing[0], key),file=f)
        if key >= min_ref:
            print('|','-'*44,'|')
        print('|','-'*44,'|',file=f)
