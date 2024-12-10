file = open("day5/input.txt", "r")

def get_ordering_rules_updates(file)->tuple:
    ordering_rule = []
    updates = []
    updates_part = False
    file.seek(0)
    for line in file:
        line = line.strip()
        if len(line) != 0:
            # Ordering rules
            if not updates_part:
                ordering_rule.append((line[0:2], line[3:5]))
            # Updates
            else:
                line = line.split(",")
                updates.append(line)
        else:
            updates_part = True
    return (ordering_rule, updates)

def is_wrong_update(update, rules):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return True
    return False

def find_middle_page(update):
    n = len(update)
    return update[n // 2]

def reorder(wrong_update, rules):
    reordered = wrong_update.copy()
    for a, b in rules:
        for a,b in rules:
            if a in reordered and b in reordered:
                index_a = reordered.index(a)
                index_b = reordered.index(b)
                if not (index_a < index_b):
                    reordered[index_a] = b
                    reordered[index_b] = a
    print(reordered)    
    return reordered

valid_middle_pages = []

rules, updates = get_ordering_rules_updates(file)
print(rules)
print(updates)
for update in updates:
    if is_wrong_update(update, rules):
        reordered_update = reorder(update, rules)
        print(is_wrong_update(reordered_update, rules))
        valid_middle_pages.append(find_middle_page(reordered_update))

# Calculate the sum of middle pages
sum = 0
for num in valid_middle_pages:
    sum += int(num)
print(sum)
