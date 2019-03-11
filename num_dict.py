# Princess Sampson
# In-class exercise 3-7-19

import random

# if number is in the dic, increment the count value. otherwise add it.
def add_dict(number, dic):
    if number in dic:
        dic[number] += 1
    else:
        dic[number] = 1

# get and sort keys, print corresponding values.
def look_at(dic):
    sorted_keys = sorted(list(dic))

    for key in sorted_keys:
        print('%d\t%d' % (key, dic[key]))

# find all the values >= 90
def count_a(dic):
    count = 0
    
    for score in dic:
        if score >= 90:
            count += dic[score]

    return count

def main():

    scores = {}

    for _ in range(50):
        new = random.randint(50, 100)
        add_dict(new, scores)

    look_at(scores)
    print('A\'s:', count_a(scores))


# call main
main()