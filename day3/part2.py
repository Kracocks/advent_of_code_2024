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

def get_doable_mult(line:str)->list:
    pattern = r"(mul\(\d+,\d+\)|don't\(\)|do\(\))"
    liste_trouve = re.findall(pattern, line)
    autoriser = True
    res = []
    
    for token in liste_trouve:
        if token=="don't()":
            autoriser = False
        elif token=="do()":
            autoriser = True
        elif token.startswith("mul") and autoriser == True:
            res.append(token)
    return res

numbers2 = []
the_line = ""
f.seek(0)
for line in f:
    the_line += line

doable_mult = get_doable_mult(the_line)
for mult in doable_mult:
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
            
    numbers2.append(mul(int(num1), int(num2)))

print(additionner(numbers2))