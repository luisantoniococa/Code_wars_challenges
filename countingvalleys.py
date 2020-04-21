def countvall(n,s):
    suma = 0
    valley = 0
    for i in range(n):
        if s[i]== 'D':
            suma -= 1
        else:
            suma += 1
        if suma == 0 and s[i] == 'U':
            valley += 1

string = 'DDUUDDDUDUUDUDDDUUDDUDDDUDDDUDUUDDUUDDDUDDDUDDDUUUDUDDDUDUDUDUUDDUDUDUDUDUUUUDDUDDUUDUUDUUDUUUUUUUUU'
n = 100
print(countvall(n,string))