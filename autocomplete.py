from Term import *
from SearchDelux import *

def impl(file,word):

    cities = (open(f"/home/danesh/QimiaDirectory/autocomplete/old/{file}.txt")).readlines()
    terms = []
    i = -1
    # reading files and make terms list of object which contains terms.query(names) and terms.weight(weight)
    for line in cities:
        i += 1
        words = line.split('\t')
        term = Term(words[1].strip(), words[0].strip())
        terms.append(term)

    # sorting all texts by terms.query alphabetic order
    terms.sort(key=lambda t: t.query)

    search_term=word.lower()

    searched_list = SearchDelux(terms, search_term)

    searched_list.sort(key=lambda t: t.weight, reverse=True)

    # printing the weight sorted list of the searched list include terms.query and terms.weight
    for i in range(len(searched_list)):
        print(searched_list[i].query, searched_list[i].weight)

file=input('cities , wiktionary\nfile dir>')
word=input('search word>')
#
impl(file, word)