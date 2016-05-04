from string import ascii_lowercase

#Returns a list of the first 10 letters of the alphabet
L=[i for i in ascii_lowercase[:10]] # alphabet
print L

#Returns a list of the first 10 letters of the alphabet except the sixth one.
L2=[i for i in L if i != 'f']
print L2

#Returns a list of the first 10 letters of the alphabet except the sixth one, each repeated each 1 , 2, and 3 times: ['a', 'aa','aaa','b',...,'c',...]
numbers=[1,2,3]
L3 =[i*n for i in L2 for n in numbers]
print L3

#Returns a list like the above, but in a grid: [['a','aa','aaa'], ['b',...],['c',...],...]
L4=[L3[n:n+3] for n in range(0, len(L3), 3)]
print L4

#Returns a list like the above, but if the number matches the index of the character mod 3 (e.g. 'c' and 3, instead print a single capitalized version of that character: [['A','aa', 'aaa'],['b','B','bbb'],['c','cc','C'],['D',...],...]
L5=[n[0].upper() if i.index(n)==ascii_lowercase.find(n[0])%3 else n for i in L4 for n in i]
print L5