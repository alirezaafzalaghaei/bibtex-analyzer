
import sys, os
import collections
from itertools import groupby
from pybtex.database.input import bibtex
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

os.system('clear')
parser = bibtex.Parser()
bib_data = parser.parse_file(sys.argv[1])
years = []
YEARS = []

print("     Number of all references are: ", len(bib_data.entries.keys()))
for key,entry in bib_data.entries.items():
    years.append((key, int(entry.fields['year'])))
    YEARS.append(int(entry.fields['year']))


years.sort(key=lambda x:x[::-1])
for entry in years:
    print("%d %30s"%entry[::-1])


years = YEARS
years2 = list(map(lambda x:x, years))
t = Counter(years)
x = list(t.keys())
y = list(t.values())
print(y)
colors=['#d2527f', '#22a7f0', '#2ecc71', '#fad859', '#f9690e','#95a5a6','#db0a5b','#013243','#1f3a93','#03c9a9','#00e640','#f7ca18','#d35400','#ffcb05','#67809f']
y2 = list(map(lambda x:x-1,y))
Colors = list(map(lambda i:colors[i],y2))
with plt.xkcd():
    rects = plt.bar(x, y, color=Colors)
    plt.xticks(list(set(years2)),rotation='vertical')
    plt.yticks(list(set(y)))
    ax = plt.gca()
    for rect in rects:
        height = rect.get_height()
        b = rect.get_bbox()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%d' % int(b.y1 + b.y0), ha='center', va='bottom')
    plt.title("total number of references is %d"%len(bib_data.entries.keys()))
    plt.show()

