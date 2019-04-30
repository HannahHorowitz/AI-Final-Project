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
    for line in lines: #foor loop to separate elements of the string in lines
        #figure out how to separate the inputs based on comma and tab - separate into strings
        #variables to save values into
        # name
        # roommate
        # morning
        # messy
        # conflict
        variables.append(name)
        domains[name] =

    # set up the variables and domains in the Australia example so it can be solved with AC3
    variables = ["Northern Territory", "Queensland", "New South Wales", "Victoria"]
    domains = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]

    variables.append("South Australia")
    domains["South Australia"] = ["red"]
    variables.append("Western Australia")
    domains["Western Australia"] = ["blue"]
    variables.append("Tasmania")
    domains["Tasmania"] = ["red"]

    myCSP = CSP(variables, domains)
    myCSP.addConstraint("Western Australia", "Northern Territory")
    myCSP.addConstraint("Western Australia", "South Australia")
    myCSP.addConstraint("South Australia", "Northern Territory")
    myCSP.addConstraint("Queensland", "Northern Territory")
    myCSP.addConstraint("Queensland", "South Australia")
    myCSP.addConstraint("Queensland", "New South Wales")
    myCSP.addConstraint("New South Wales", "South Australia")
    myCSP.addConstraint("Victoria", "South Australia")
    myCSP.addConstraint("Victoria", "New South Wales")

    myCSP.ac3()
    myCSP.print()

main()
