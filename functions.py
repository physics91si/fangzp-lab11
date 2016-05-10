import os
import matplotlib.pyplot as plt

l1st=range(1,11)
squares = [x**2 for x in l1st]
print squares #Creates a list of the first 10 square numbers

product = reduce(lambda x, y: x*y, [1,2,3,4,5]) # Multiplies the numbers from 1 to 5
print product

#files = filestring.split() # From string with list of filenames "test1.py test2.py test3.py...", outputs a list of just filenames without file extension
#stripped_filennames = [os.path.splitext(x)[0] for x in files]

#wordlist = wordstring.split() #Dictionary
#lowercase = [x.lower() for x in wordlist]
#uniquewords = set(lowercase)

squaredict = {l1st, squares} # A graph of the square function, which is a dict that has the first ten integers as its keys and their squares as its items: {1:1,2:4,3:9,...}
plt.plot(squaredict.keys(), squaredict.values())