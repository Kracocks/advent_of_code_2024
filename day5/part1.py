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

def is_valid_update(update, rules):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):  # a must precede b
                return False
    return True

def find_middle_page(update):
    n = len(update)
    return update[n // 2]

# Process updates
valid_middle_pages = []

rules, updates = get_ordering_rules_updates(file)
print(rules)
print(updates)
for update in updates:
    if is_valid_update(update, rules):
        valid_middle_pages.append(find_middle_page(update))

# Calculate the sum of middle pages
sum = 0
for num in valid_middle_pages:
    sum += int(num)
print(sum)
