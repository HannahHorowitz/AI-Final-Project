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
        var1 = row[0]
        var2 = row[1]
        var3 = row[2]
        var4 = row[3]
        name.append(var1)
        pref.append(var2)
        morning.append(var3)
        messy.append(var4)
        #print(name[index])
        index += 1
    for a in morning:
        if a == "Morning" or a == "Night":
            m = a.index("Morning")
            n = a.index("Night")
            for b in name:
                if b == name[m] or b == name[n]:
                    print(name[m])
                    print(name[n])
    for c in morning:
        if c == "Night":
            n = c.index("Night")
            for d in name:
                if d == name[n]:
                    print(name[n])

    for e in messy:
        if e == "Messy":
            m2 = e.index("Messy")
            for f in name:
                if f == name[m2]:
                    print(name[m2])

    for g in messy:
        if g == "Neat":
            n2 = g.index("Neat")
            for h in name:
                if h == name[n2]:
                    print(name[n2])



    #print(name)
    #print(pref)
    #print(morning)
    #print(messy)


main()