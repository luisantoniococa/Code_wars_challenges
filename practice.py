def jumpingClouds(c):
    the_sum = 0
    # print(the_sum)
    result = len(c)//2
    count = 0
    # print(len(c))
    # print(len(c)//2)
    for i in range(0,len(c),2): 
        if c[i] == 1 and sum(c) > 1: 
            count += 1
    result = len(c)//2 + count
    
    print(f"the min amount of steps are: {result}")

def jumpingClouds2(c):
    i = 0
    count = 0
    limit = int(len(c))
    print ('this is before the loop:',  i)
    while (i < limit-2):
        print('this is in the loop ', i)
        # print('this is the limit',limit)
        print(int(c[i+1]) == 0) and (int(c[i+2]) == 0)
        if (int(c[i+1]) == 0) and (int(c[i+2]) == 0):
            print('it got to the if')
            count += 1
            i += 2
        elif (c[i+1] == 1 and c[i+2]== 0):
        # else:
            # print('it got to the elif')
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    if c[limit-1] == 0 and c[limit-2] == 0 and c[limit -3]== 0 : return count
    if c[limit-1] == 0 and c[limit-2] == 0: return count + 1
    
        # if i > 3: 
        #     break
    return count





def main():
    string = '0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0'
    li = list(string.split(" "))
    li2 = [int(x) for x in li]
    print (li2)
    print(jumpingClouds2(li2))

if __name__ == '__main__': main()