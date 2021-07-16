def howSum(n,a,memo={}):
    #n -> targetSum
    #a -> Numbers array
    ans=[]
    if n in memo:
        return memo[n]
    if n==0:
        return []
    if n<0:
        return None
    for i in a:
            remainder=n-i
            remresult=howSum(remainder,a,memo)
            if remresult is not None:
                memo[n]= [*remresult,i]
                return memo[n]
    memo[n]=None
    return None
# print(howSum(5,[1,2,3,4]))

## tabular method

def howsum_tab(targetsum,numbers):
    table=[None]*(targetsum+1)
    table[0]=[]

    for i in range(targetsum+1):
        if table[i] is not None:
            for num in numbers:
                if i+num < targetsum+1:
                    table[i+num]=[*table[i], num]

    print(table)
    return table[targetsum]
print(howsum_tab(4,[4,2]))