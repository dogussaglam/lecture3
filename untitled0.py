# -*- coding: utf-8 -*-
"""


@author: dogus

#function definition
def myprint(str):
    print(str)
    return

#function call
myprint("barcelona")
myprint("real madrid")


def Fun(x, y):
    result = x + y
    return result

print(Fun(5, 3))


def ChangeRefer(mylist):
    mylist = [1, 2, 3, 4]
    print("first values: ", mylist)

    
mylist =[10, 20, 30]
ChangeRefer(mylist)
print("second values: ", mylist)

def printInfo(name, age = 23):
    print("name: ", name)
    print("age: ", age)

printInfo(age=19, name="abc")
printInfo(name= "xyz")


from random import randint
print(randint(0,100))

import random
print(random.randint(0,100))

import random
print("randrange(100, 1000, 2) :", random.randrange(100, 1000, 2))
print("randrange(100, 1000, 2) :", random.randrange(100, 1000, 3))
print("random float uniform (18,81)", random.uniform(18,81))
print("random float uniform (19,38)", random.uniform(19,38))

import sys
print(sys.path)


from math import pi
print(pi)
import math
def area_of_circle(r):
    a = r**2 * math.pi
    return a
print(area_of_circle(3))


f = open("test.txt", "w")
print(f)

f.write("now is the time")
f.write("to close the file")
f.write(" but first let me take a selfie")

f.close()

f = open("test.txt", "r")
text = f.read()
print(text)

f = open("test.txt","r")

print(f.read())

f=open("test.txt","r")
print(f.read(3))
print(f.read(1000006))


fo = open("foo.txt", "w")
fo.write("Phyton is a great language babe.\nyeah it's great!\n")

fo= open("foo.txt", "r+")
str = fo.read(17)
print("our string is: ",str)

position = fo.tell()
print("current file position: ", position)


str = fo.read(17)
print("again our string is: ",str)
str = fo.read(17)
print("again our string is: ",str)
#2 kez 17 saydı, şimdi pozisyonu başa alacaz

position = fo.seek(0,0)
str = fo.read(17)
print("our now position return start:", str)
fo.close()





try:
    fh= open("testfile", "r")
    fh.write("This is my test file for exception handling!")
except IOError:
    print("Error : can\'t find file or read data")
else:
    print("Written content in the file successfully")

try:
    fh= open("testfile", "w")
    fh.write("This is my test file for exception handling!")
except IOError:
    print("Error : can\'t find file or read data")
else:
    print("Written content in the file successfully")


try:
    fh= open("testfile", "w")
    fh.write("This is my test file for exception handling!")
finally: #finally her koşulda mutlaka çalışır
    print("Error : can\'t find file or read data")

print(list('cat')) #list fonk farklı türlerdeki argümanları listeye çevirir

list = ['physics', 'chemistry', '2017', '1923.2023']
print("3. elaman: ", list[2])


a_tuple = ('ready', 'fire', 'aim')

print(list(a_tuple))

tup1 = ('physics', 'chemistry', '2017', '1923.2023')
tup2 = (1,2,3,4,5,6,7)
print("tup1[3]: ",tup1[3])
print("tup2[2:6]: ",tup2[2:6])

list1 =['python', 'java', 2017, 2023]
print(list1)
#del list1[1]
#print(list1)
print(list1.pop(1))


list1 =['python', 'java', 2017, 2023]
print(list1[3])
list1[3]= 5000
print(list1[3])
print(list1)

txt = 'but soft what light in window breaks'
words = txt.split()
print(words)

#list comprehensions
pow2 = [2 ** x for x in range(10) if x >5]
print(pow2)


pow2 = []
for x in range(10):
    pow2.append(print(2**x))
   

langs = []
langs.append('Phyton')
langs.append('Perl')
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")    
print(langs)

langs.extend(("Javascript", "Actionscript"))
print(langs)


newlist = [x.upper() for x in langs]
print(newlist)

newlist1 = [x.lower() for x in langs]
print(newlist1)


langs = ["Python", "Ruby", "Perl", "Lua", "Javascript"]
print(langs)
print(langs.pop(2))

del langs[:]
del langs
print(langs)


import random

class Coin:
    
    #__init__ metodu ile bozuk paranın ilk hali heads olarak başlatılır
    
    def __init__(self):
        self.sideup = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
            
    def get_sideup(self):
        return self.sideup

#the main function
def main():
    my_coin = Coin()
    
    print('This side is up: ', my_coin.get_sideup())
        
#parayı sallama

    print("I am tossing the coin... ")
    my_coin.toss()
    
    print('this side is up: ', my_coin.get_sideup())
    
main()
"""




























































































































