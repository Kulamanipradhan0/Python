def cansum(n,a,memo={}):
    #n -> targetSUm to check
    #a -> array
    if n in memo:
        return memo[n]
    if n==0:
        return True
    if n<0:
        return False
    for i in a:
        print(n,i)
        remainder=n-i
        if cansum(remainder,a,memo)==True:
            memo[n]=True
            return True
    memo[n]=False
    print(memo)
    return False

# print(cansum(5,[2,4]))

#tabulr method

def cansum_tab(targetsum,numbers):
    table=[False]*(targetsum+1)
    newposition=0
    table[newposition]=True
    for i in range(targetsum+1):
        if table[i]==True:
            for num in numbers:
                newposition=i+num
                if newposition < targetsum+1:
                    table[newposition]=True
    print(table)
    return table[targetsum]
print(cansum_tab(8,[2,4]))