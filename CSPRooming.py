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

    data = open("test.txt", "r")
    lines = data.readlines()
    name = []
    pref = []
    morning = []
    messy = []

    index = 0
    for x in lines:
        row = x.split()
        names = row[0]
        preferences = row[1]
        timeOfDay = row[2]
        cleanliness = row[3]
        name.append(names)
        pref.append(preferences)
        morning.append(timeOfDay)
        messy.append(cleanliness)
        #print(name[index])
        index += 1

    for a in morning:
        if a == "Morning":
            m = a.index("Morning")
            for b in name:
                if b == name[m]:
                    print(name[m])
        else:
            n = a.index("Night")
            for c in name:
                if c == name[n]:
                    print(name[n])

    for d in messy:
        if d == "Messy":
            m2 = d.index("Messy")
            for e in name:
                if e == name[m2]:
                    print(name[m2])
        else:
            n2 = d.index("Neat")
            for f in name:
                if f == name[n2]:
                    print(name[n2])

    print(name)
    print(pref)
    print(morning)
    print(messy)



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
        domains[v] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

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
