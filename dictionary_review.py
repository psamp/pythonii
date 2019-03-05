import statistics

def make_dictionary(keys, values):
    # throw an exception if not same no. of keys as values
    if len(keys) != len(values):
        raise Exception('Must have equal number of keys and values')

    dictionary = dict()

    # loop over both lists
    for index in range(len(keys)):
        # pull out corresponding keys and values
        key = keys[index]
        value = values[index]

        # for the key, insert the value into the dict
        dictionary[key] = value
    
    return dictionary

def main():
    names = ['Tonya', 'Mary', 'Alexis', 'Angel']
    scores = [85, 75, 90, 80]

    # create dict from lists
    score_dict = make_dictionary(names, scores)
    
    # print alexis
    print(score_dict['Alexis'])

    # add joshua
    score_dict['Joshua'] = 95

    # sorted list of the scores
    scores_sorted = sorted(score_dict.values())
    print(scores_sorted)

    # avg score
    avg_score = statistics.mean(list(score_dict.values()))
    print(avg_score)

    # remove mary
    score_dict.pop('Mary')
    print(score_dict)

    # print table sorted by name
    for name, score in sorted(score_dict.items()):
        print('%s\t%d' % (name, score))


# call main
main()