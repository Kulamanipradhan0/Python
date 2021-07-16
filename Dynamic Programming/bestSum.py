import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())
## Brute Force ##

def bestSum(targetsum, numbers):
    if targetsum==0 :
        return []
    if targetsum<0 :
        return None
    shortestcombination=None
    for num in numbers:
        reminder=targetsum-num
        combination=bestSum(reminder,numbers)
        if combination is not None:
            combination=combination+[num] #possible combination where reminder is 0
            if (shortestcombination is None or len(combination)<len(shortestcombination)):
                shortestcombination=combination
    return shortestcombination


## Memoization ##

def bestSum_memo(targetsum,numbers,memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0 :
        return []
    if targetsum <0:
        return None
    shortestcombination=None
    for num in numbers:
        reminder=targetsum-num
        combination=bestSum_memo(reminder,numbers,memo)
        if combination is not None:
            combination=combination+[num]
            if shortestcombination is None or len(combination)<len(shortestcombination):
                shortestcombination=combination
    memo[targetsum]=shortestcombination
    return shortestcombination

# print(bestSum_memo(100,[1,2,25,5]))

def bestSum_tab(targetsum,numbers):
     table=[None]*(targetsum+1)
     table[0]=[]
     # table[targetsum]=[]
     for i in range(targetsum+1):
         if table[i] is not None:
             for num in numbers:
                 if i+num < targetsum+1:
                     if table[i+num] is None or len([*table[i],num]) < len(table[i+num]) :
                        table[i+num]=[*table[i],num]

     return table[targetsum]

print(bestSum_tab(6,[1,2,3,5,6]))