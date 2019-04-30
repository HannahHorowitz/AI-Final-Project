from CSP import *


def readFromFile(filename):
    board = ""
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        board =line.replace("\n", "")
    return board


def main():
    lines = readFromFile("preferences.txt") #reading in text file of preferences

    variables =[] #list of all variables, in this case the names entered
    domains ={}
    mornings = []
    nights = []
    messys = []
    neats = []
    for line in lines: #foor loop to separate elements of the string in lines
        #figure out how to separate the inputs based on comma and tab - separate into strings
        #variables to save values into
        # name
        # roommate
        # morning
        # messy
        # conflict
        if morning == "Morning":
            mornings.append(name)
        elif morning == "Night":
            nights.append(name)
        if messy == "Messy":
            messys.append(name)
        elif messy == "Neat":
            neats.append(name)

        variables.append(name)

    # set up the variables and domains in the Australia example so it can be solved with AC3
    for v in variables:
        domains[v] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # variables.append("South Australia")
    # domains["South Australia"] = ["red"]
    # variables.append("Western Australia")
    # domains["Western Australia"] = ["blue"]
    # variables.append("Tasmania")
    # domains["Tasmania"] = ["red"]

    myCSP = CSP(variables, domains)

    for name in mornings:
        for person in nights:
            myCSP.addConstraint(name, person)

    for n in messys:
        for p in neats:
            myCSP.addConstraint(n, p)


    myCSP.ac3()
    myCSP.print()

main()
