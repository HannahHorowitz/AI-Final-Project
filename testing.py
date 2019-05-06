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


main()