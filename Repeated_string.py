def repeatedString(s,n):
    count=[1 for i in s if i == 'a']
    the_mod = len(s)
    modee= n % the_mod 
    possible = n// the_mod
    print(sum(count))
    print(f'the leng of the string is:{the_mod}')
    print(f"the mod is: {modee}")
    extra = [1 for i in range(modee) if s[i]=='a']
    print (f'the extra a are {sum(extra)}')
    total = sum(count)*possible+ sum(extra)
    return total
def main():
    print(repeatedString('ada',10))

if __name__ == '__main__': main()
