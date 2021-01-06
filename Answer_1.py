#1: Write a Python program to read a file line by line and store it into a list

def ReadLines(fname):
    with open(fname) as f:
        lst=f.readlines()
        print(lst)
ReadLines("amitshah.txt")