# Quick Modulo Demo

num_items = 10

for item in range(1, num_items):
    remainder = item % 4
    print(item, end = '\t')
    if remainder == 0:
        print()
