from CSP import *
def readFromFile(filename):
    board = ""
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        board =line.replace("\n", "")
    return board

