import re

f = open("day3/input.txt", "r")

def is_num(character:str) -> bool:
    flag = True
    try:
        int(character)
    except ValueError:
        flag = False
    return flag

def mul(num1:int, num2:int)->int:
    return num1 * num2

def additionner(liste:list)->int:
    res = 0
    for num in liste:
        res += num
    return res

numbers = []
for line in f:
    liste_trouve = re.findall(r"mul\(\d+,\d+\)", line)
    for mult in liste_trouve:
        num1 = ""
        i = 4
        while is_num(mult[i]):
            num1 += mult[i]
            i += 1
        i += 1
        num2 = ""
        while is_num(mult[i]):
            num2 += mult[i]
            i += 1
        numbers.append(mul(int(num1), int(num2)))
print(additionner(numbers))