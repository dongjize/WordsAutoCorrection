# Introduction

Approximate string search algorithms are broadly applied as spelling correction methods to resolve typographical errors in languages which are omnipresent. This project works on lists of misspelt words to get them automatically corrected using approximate string search approaches.

## Contents
The major scripts of the project are:
- `ged.py`
Implements Global Edit Distance
- `ngram.py`
Implements N-Gram Distance
- `soundex.py`
Implements Soundex
- `typo_analysis.py`
Analyzes the types of typos in Wiki data

Each script can be run directly by command `python xxx.py`, and will generate a result file in `data` folder and calculate the precision and recall of the prediction, with which we are able to evaluate the performance of a specific spelling correction method.

## External Libraries

This project has included external libraries regarding to the implementation of approximate string matching algorithms, which are:

- **Levenshtein Distance**
library: python-Levenshtein
URL: https://github.com/ztane/python-Levenshtein

- **N-Gram Distance**
library: nltk
URL: http://nltk.org

- **Soundex**
library: fuzzy
URL: https://github.com/yougov/Fuzzy
