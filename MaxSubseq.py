prev = int(input())
if prev == 0:
    print(0)
    exit()

max_count = 1
count = 1
x = int(input())
while x != 0:
    if x >= prev:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 1

    prev = x
    x = int(input())

if count > max_count:
    max_count = count

print(max_count)
