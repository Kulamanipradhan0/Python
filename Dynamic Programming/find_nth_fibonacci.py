import  datetime


#recursive call
def fib_rec(n):
    if n<=2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)

#old way
def fib_old(n):
    if n<=2:
        return 1
    else:
        old_0th_value=0
        start=end=1
        for i in range(n-2):
            old_0th_value=start
            start=end
            end=old_0th_value+end
        return end

#Time : O(n)
#Space : O(n)


#memoization
def fib_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        memo[n]=fib_memo(n-1,memo)+fib_memo(n-2,memo)
    return memo[n]




#tabulation


def fib_tab(n):
    table=[0]*(n+1)
    table[0]=0
    table[1]=1
    for i in range(2,n+1):
        table[i]=table[i-1]+table[i-2]
    return table[n]

start=datetime.datetime.now()
print(fib_old(100000))
end=datetime.datetime.now()
print('Time : ',end-start)

start=datetime.datetime.now()
print(fib_memo(100))
end=datetime.datetime.now()
print('Time : ',end-start)

start=datetime.datetime.now()
print(fib_tab(100000))
end=datetime.datetime.now()
print('Time : ',end-start)

start=datetime.datetime.now()
print(fib_rec(100))
end=datetime.datetime.now()
print('Time : ',end-start)