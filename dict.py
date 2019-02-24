# Princess Sampson
# Python II - Dr. Lawrence


def main():
    # ride or dies
    friends = [
        {"name": "Delayne", "number": "234-897-5565"},
        {"name": "Elsie", "number": "404-411-8669"},
        {"name": "Shay", "number": "773-345-1299"},
        {"name": "Rod", "number": "420-609-6259"},
        {"name": "Jaque", "number": "555-098-1278"}
    ]

    # create a new address book addition
    addition = {"name": input("Enter your friend's name: "),
                "number": input("Enter your friend's number: ")}

    # append the addition to the address book
    friends.append(addition)

    # print out each dictionary in the address book
    for friend in friends:
        print("Name: %s | Number: %s" % (friend["name"], friend["number"]))


# call main
main()
