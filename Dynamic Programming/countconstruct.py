## Brute Force ##


def countcounstruct(target,wordbank):
    if target=='':
        return 1
    totalcount=0
    for word in wordbank:
        if target.startswith(word):
            suffix=target[len(word):]
            combination=countcounstruct(suffix,wordbank)
            if combination==1:
                totalcount+=1
    return totalcount


## Memoization ##


def countcounstruct_memo(target,wordbank,memo={}):
    if target in memo:
        return memo[target]
    if target=='':
        return 1
    totalcount=0
    for word in wordbank:
        if target.startswith(word):
            suffix=target[len(word):]
            combination=countcounstruct_memo(suffix,wordbank,memo)
            if combination==1:
                totalcount+=1
    memo[target]=totalcount
    return totalcount

# print(countcounstruct('abcd',['a','b']))
# print(countcounstruct('abcd',['ab','cd','abcd']))
# print(countcounstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','ee']))


def countconstruct_tab(target, wordbank):
    table=[0]*(len(target)+1)
    table[0]=1

    for i in range(len(target)+1):
        if table[i] != 0:
            for word in wordbank:
                if target[i:].startswith(word):
                    table[i+len(word)]+=table[i]
    return table[len(target)]


print(countconstruct_tab('abcd',['a','b','cd','abcd','abc','d','ab']))
print(countconstruct_tab('abcd',['ab','cd','abcd']))
print(countconstruct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','ee']))

#time : O(m^2*n)
#space : O(m)
