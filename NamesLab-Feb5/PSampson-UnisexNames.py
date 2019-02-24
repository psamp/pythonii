# Princess Sampson
# Dr. Lawrence - Python II
# Use intersection of name sets to find unisex names

def main():
    # open file to read feminine names
    feminineGenderedNames = open('GirlNames.txt', 'r')

    # open file to read masculine names
    masculineGenderedNames = open('BoyNames.txt', 'r')

    # storage lists
    fem = set()
    masc = set()

    #
    femName = None
    mascName = None

    # we only need to check against the first 10 names
    while femName != "" and mascName !="":
        # read in the fem and masc names, strip the newline character
        femName = feminineGenderedNames.readline().rstrip('\n')
        mascName = masculineGenderedNames.readline().rstrip('\n')
        
        # append them to their respective lists
        fem.add(femName)
        masc.add(mascName)

    # the & operator for sets functions as intersection()
    unisex = sorted(fem & masc)

    for name in unisex:
        print(name)

    # close the files
    feminineGenderedNames.close()
    masculineGenderedNames.close()
    
# call main
main()