f = open("day7/input.txt", "r")

def get_numbers(line):
    #first number is the result of the equation
    numbers = []
    num = ''
    for c in line:
        if c in '0123456789':
            num += c
        elif len(num) != 0:
            numbers.append(num)
            num = ''
    return numbers

def get_possibilities(numbers):
    numbers = numbers.copy()
    possibilities = []
    num1 = numbers[1]
    num2 = numbers.pop(2)
    for operator in '+*':
        nums_copy = numbers.copy()
        nums_copy[1] = str(eval(num1+operator+num2))
        possibilities.append(nums_copy)
        
    while len(possibilities[0]) > 2:
        possibility = possibilities.pop(0)
        possibilities =  [*possibilities, *get_possibilities(possibility)]
            # possibilities + get_possibilities(possibility)
    # for i in range(len(possibilities)):
    #     if len(possibilities[i]) > 2:
    #         nums = possibilities.pop(i)
    #         possibilities + get_possibilities(nums)
    return possibilities
    
    
res = 0
for line in f:
    numbers = get_numbers(line)
    print(get_possibilities(numbers))
    for possibility in get_possibilities(numbers):
        num1 = possibility[0]
        num2 = possibility[1]
        print(num1, num2, num1 == num2)
        if num1 == num2:
            res += int(num1)
            break
        

print(res) #3749
