left_list = []
right_list = []

f = open("day1/input.txt", "r")
for line in f:
    l = line.split()
    left_list.append(l[0])
    right_list.append(l[1])


left_list.sort()
right_list.sort()

res2 = 0
for l_num in left_list:
    nb_num = 0
    for r_num in right_list:
        if l_num == r_num:
            nb_num += 1
    res2 += int(l_num)*nb_num

print(res2)