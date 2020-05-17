from string import ascii_uppercase
from operator import itemgetter
from collections import defaultdict
import textwrap,fileinput,collections
import sys
import string


filename = sys.argv[1]
print("NAZWA PLIKU: ", filename)

try:
    file = open(filename)
    filetest = file.read()
except FileNotFoundError:
    print('IO ERROR')
    sys.exit(0);

letters = ascii_uppercase
data = len(filetest);
lettercount = 0;

test1= defaultdict(int)
for line in filetest:
    for character in line:
        if character.upper() in letters:
            test1[character.upper()] += 1
            lettercount = lettercount +1

sortedtest = sorted(test1.items(), key=itemgetter(1),reverse=True)
st = dict(sortedtest)
      
for value in st:
    percentage = ((float(st[value]) / float(lettercount)) * 100).__round__(2)
    print(value, ":",st[value],":",percentage,"%")
print(lettercount)
file.close()


print("/////////// ZADANIE 2 ////////////////")

try:
    cipher=open('cipher.txt')
except FileNotFoundError:
    print('IO ERROR CIPHER')
    sys.exit(0);

cipherdict = defaultdict(int)
frequency1 = cipher.readline()
frequency1 = frequency1[:-1]
text = cipher.read()

for line in text:
    for character in line:
        if character.upper() in letters:
            cipherdict[character.upper()] += 1

sortedtest2 = sorted(cipherdict.items(), key=itemgetter(1),reverse=True)
st2 = dict(sortedtest2)

frequency2 = ""
for value in st2.keys():
    frequency2 +=value

frlist1= list(frequency1)
frlist2= list(frequency2)
keyMap = dict(zip(frlist1, frlist2))

decrypted=[]

for values in text:
    for characters in values:
        if characters in frlist1:
                temp = keyMap[characters]
                decrypted.append(temp)
        else:
                decrypted.append(characters)

print(''.join(decrypted))
print(frequency1)
print(frequency2)




