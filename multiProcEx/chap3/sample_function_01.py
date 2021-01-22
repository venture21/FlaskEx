import random

def makeFace():
    fruits = ['apple', 'banana', 'berry', 'grape', 'melon', 'kiwi']
    numFace = len(fruits)
    index = random.randint(0, numFace - 1)
    print(index)
    return fruits[index]

print(makeFace())
