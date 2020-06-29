from random import *
x=randint(1,100)
for i in range(1,11):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")
print("LEVEL 2!!!!!")
x=randint(1,100)
for i in range(1,10):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")
print("LEVEL 3!!!!!")
x=randint(1,100)
for i in range(1,9):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")
print("LEVEL 4!!!!!")
x=randint(1,100)
for i in range(1,8):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")
print("LEVEL 5!!!!!")
x=randint(1,100)
for i in range(1,7):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")
print("MAX LEVEL!!!!!")
for i in range(1,6):
    n=int(input("enter your number"))
    if n==x:    
        print("you are right!!!")
        x=randint(1,100)
        break
    elif n<x:
        print("higher")  
    elif x<n:
        print("lower")

