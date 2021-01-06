'''5: Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space.'''

def no_of_words(fname):
    with open(fname) as f:
        a=f.read()
        a.replace(" ,"," ")
        return len(a.split())
print(no_of_words("amitshah.txt"))
