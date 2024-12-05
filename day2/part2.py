def is_good(line, prec_num, actual_num):
    if line:
        if ((prec_num + 1) == actual_num):
            return True
        elif ((prec_num + 2) == actual_num):
            return True
        elif ((prec_num + 3) == actual_num):
            return True
    elif not line:
        if ((prec_num - 1) == actual_num):
            return True
        elif ((prec_num - 2) == actual_num):
            return True
        elif ((prec_num - 3) == actual_num):
            return True
    return False

def is_list_good(l)->bool:
    for i in range(1, len(l)):
        actual_num = int(l[i])
        precedent_num = int(l[i-1])
        
        if i == 1:
            if actual_num > precedent_num:
                line_increasing = True
            else:
                line_increasing = False
        
        safe = is_good(line_increasing, precedent_num, actual_num)
        
        if not safe:
            return False
    return True

def is_list_good2(l):
    if is_list_good(l):
        return True
    
    for i in range(len(l)):
        modified_list = l[:i] + l[i+1:]
        if is_list_good(modified_list):
            return True
    return False

f =  open('day2/input.txt', 'r')
num_safe = 0
for line in f:
    l = line.split()
    is_safe = is_list_good2(l)
    if is_safe:
        num_safe += 1
        
print(num_safe)