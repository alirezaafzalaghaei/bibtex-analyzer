# bibtex file analyzer
This repository implements some useful utilities to analyze the bib files such as 
- Sort journals by number of references
- Sort authors by number of references
- Plot number of references for each year

# Usage
- Install the requirements

      python -m pip install -r requirements.txt
- journal 
 
      python journal.py /path/to/references.bib

- author : prints all authors where have been cited more than `3` time.

      python author.py /path/to/references.bib 3

- plot

      python plot.py /path/to/references.bib 
