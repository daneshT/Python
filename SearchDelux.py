from Term import Term


def SearchDelux(terms, search_term):
    firstindex = -1
    lastindex = -1
    searched_list = []
    for i in range(0, len(terms)):
        if (terms[i].query[0:len(search_term)]).lower() == search_term:
            firstindex = i
            break
    if (firstindex == -1):
        print("noting found.")
        exit()
    for j in range(len(terms) - 1, -1, -1):
        if (terms[j].query[0:len(search_term)]).lower() == search_term:
            lastindex = j
            break
    if (j == -1):
        print("noting found.")
        exit()
    for ii in range(firstindex, lastindex + 1):
        searched_list.append(terms[ii])
    print(f'number of matches:{lastindex - firstindex + 1}')
    return searched_list
