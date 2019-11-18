# starting at 0 will print all 3 options so we start at 1
j = 1
while j < 101:
    if j % 3 == 0 and j % 5 == 0:
        print("ThreeFive")
    if j % 5 == 0:
        print("Five")
    if j % 3 == 0:
        print("Three")
    else:
        print(j)
    j += 1