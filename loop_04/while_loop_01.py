i = 0
while i < 5:
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # skip 3
    print(i)