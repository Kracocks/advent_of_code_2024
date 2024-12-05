left_list = []
right_list = []

f = open("day1/input.txt", "r")
for line in f:
    l = line.split()
    left_list.append(l[0])
    right_list.append(l[1])


left_list.sort()
right_list.sort()

res1 = 0
for i in range(len(left_list)):
    res1 += abs(int(left_list[i])-int(right_list[i]))
print(res1)
