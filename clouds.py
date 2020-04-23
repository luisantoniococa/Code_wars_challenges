def cloudsmin(c):
    n = len(c)
    steps = {}
    # count = 0
    print(n)
    for x in range(n-2):
        ar = [c[x],c[x+1],c[x+2]]
        # if c[n-1-x] + c[n-2-x] + c[n-3-x] == 0:
        #     print ('yei')  
        steps[x] = ar
    print(steps)
cloudsmin([0,0,0,0,1,0,0])