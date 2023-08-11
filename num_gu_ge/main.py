import random


def win():
  print("You win")

def hilo(a,b):
    while a != b:
        if a > b:
            print('Too high')
        else:
            print('Too low')
        a = int(input())

def hotcold(a,b):
    while a != b:
        if b + 5 > a and b - 5 < a:
            print ('HOT!!')
        elif b + 10 > a and b - 10 < a:
            print ('Warm')
        elif b + 20 > a and b - 20 < a:
            print ('cold')
        elif b + 30 > a and b - 30 < a:
            print ('freezing')
        a = int(input())
    if a == b:
        win()

rand = random.randint(0,100)
rand = 3
print('Enter your guess between 0 and 100:')

inp = int(input())

if inp < 0 or inp > 100:
    print("BETWEEN 0 AND 100! I quit!")
else:
    hotcold(inp,rand)




