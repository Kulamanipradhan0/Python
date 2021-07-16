## Brute Force ##
def allconstruct(target, wordbank):
    if target=='':
        return [[]]
    possibleways=[]
    for word in wordbank:
        if target.startswith(word):
            suffix=target[len(word):]
            ways=allconstruct(suffix,wordbank)
            targetways=[[word]+way for way in ways]
            if targetways:
                possibleways.extend(targetways)
    return possibleways


## Memoization ##

def allconstruct_memo(target, wordbank,memo={}):
    if target in memo:
        return memo[target]
    if target=='':
        return [[]]
    possibleways=[]
    for word in wordbank:
        if target.startswith(word):
            suffix=target[len(word):]
            ways=allconstruct_memo(suffix,wordbank,memo)
            targetways=[[word]+way for way in ways]
            if targetways:
                possibleways.extend(targetways)
    memo[target]=possibleways
    return possibleways
# #print(allconstruct('abcd',['a','b']))
# print(allconstruct('abcd',['ab','cd','abcd']))
# print(allconstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eef']))


def allconstruct_tab(target, wordbank):
    table = [None]*(len(target)+1)
    table[0]=[[]]

    for i in range(len(target)+1):
        if table[i] is not None:
            for word in wordbank:
                if target[i:].startswith(word):
                    ways=[i+[word] for i in table[i]]
                    if table[i+len(word)] is not None:
                        table[i+len(word)]+=ways
                    else:
                        table[i+len(word)]=ways

    return table[len(target)]

print(allconstruct_tab('abcd',['a','b']))
print(allconstruct_tab('abcd',['ab','cd','abcd']))
print(allconstruct_tab('eeeeeeeeeeeeeeeeeef',['e','ee','eef']))

