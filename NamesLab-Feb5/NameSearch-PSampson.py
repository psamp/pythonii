# P Sampson
# Dr. Lawrence - Python 2
# Gendered name search

def main():
    # open file to read feminine names
    feminineGenderedNames = open('GirlNames.txt', 'r')

    # open file to read masculine names
    masculineGenderedNames = open('BoyNames.txt', 'r')

    # storage lists
    fem = []
    masc = []

    # we only need to check against the first 10 names
    for _ in range(0, 10):
        # read in the fem and masc names, strip the newline character
        femName = feminineGenderedNames.readline().rstrip('\n')
        mascName = masculineGenderedNames.readline().rstrip('\n')
        
        # append them to their respective lists
        fem.append(femName)
        masc.append(mascName)

    # user enters a name
    name = input("Enter a name: ")

    if name in fem:
        print("This is a top 10 girl's name.")
    elif name in masc:
        print("This is a top 10 boy's name.")
    else:
        print("This is not a 10 ten name.")

    # close the files
    feminineGenderedNames.close()
    masculineGenderedNames.close()
    
# call main
main()