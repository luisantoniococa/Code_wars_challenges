# n is representing the number of single values in the array
# ar represents the array
def countpairs(n, ar):
    count = 0
    # pointer = 0
    diction = {}
    temp_ar = ar
    # index  = []
    for i in range(n):
        if ar[i] in diction:
            diction[ar[i]] += 1
        else:
            diction[ar[i]] = 1
    for x in diction:
        print(f"thi is the value in dict {x}")
        print(f" count of the key above {diction[x]}")
        if (diction[x] % 2) == 0:
            print(f" count of the key above {diction[x]}")
            count = count + diction[x]//2
        else:
            count = count + diction[x]//2
    print(diction)
    print(count)  
    return count

arr = [1,3,3,1,1,1,1]
n = 7

countpairs(n,arr)
