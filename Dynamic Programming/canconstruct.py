
## Brute Force ##
def canconstruct(target, wordbank):
    if target=='':
        return True
    for word in wordbank:
        if target.startswith(word):
            reminder=target[len(word):]
            if canconstruct(reminder,wordbank)==True:
                return True
    return False


## Memoization ##
def canconstruct_memo(target, wordbank,memo={}):
    if target in memo:
        return memo[target]
    if target=='':
        return True
    for word in wordbank:
        if target.startswith(word):
            reminder=target[len(word):]
            if canconstruct_memo(reminder,wordbank,memo)==True:
                memo[target]=True
                return True
    memo[target]=False
    return False
#
# print(canconstruct('abcd',['ab','c','d']))
# print(canconstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','ee']))

## Tabular method

def canconstruct_tab(target, wordbank):
    table = [False]*(len(target)+1)
    table[0]=True

    for i in range(len(target)+1):
        if table[i] == True:
            for word in wordbank:
                # print(target[i:])
                if target[i:].startswith(word):
                    table[i+len(word)]=True
    return table[len(target)]
print(canconstruct_tab('abcd',['a','bc','d','cd']))
print(canconstruct_tab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','ee']))

#Time Complexity : O(m^2*n)
#Space Complexity : O(m)