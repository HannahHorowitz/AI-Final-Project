from CSP import *

#why is everything so weird 
def readFromFile(filename):
    board = ""
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        board =line.replace("\n", "")
    return board


def main():

    data = open("preferences.txt", "r")
    lines = data.readlines()
    # name = []
    # pref = []
    # morning = []
    # messy = []

    # index = 0
    # for x in lines:
    #     row = x.split()
    #     names = row[0]
    #     preferences = row[1]
    #     timeOfDay = row[2]
    #     cleanliness = row[3]
    #     name.append(names)
    #     pref.append(preferences)
    #     morning.append(timeOfDay)
    #     messy.append(cleanliness)
    #     #print(name[index])
    #     index += 1

    variables = []
    domain = []
    domains ={}
    mornings = []
    nights = []
    messys = []
    neats = []
    for line in lines:
        row = line.split()
        name = row[0]
        morning = row[1]
        messy = row[2]
        conflict = row[3]
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
        domains[v] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    # variables.append("South Australia")
    domains["JosieBauer"] = [1]
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

    for line in lines:
        row = line.split()
        name = row[0]
        conflict = row[3]
        if conflict != "None":
            myCSP.addConstraint(name, conflict)



    myCSP.search()
    myCSP.print()

main()
