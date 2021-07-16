from datetime import  datetime as dt


#Recursive
def grid_traversal_rec(maxrow,maxcol):
    a=2*[[0]*3]
    rowcol=str(maxrow)+','+str(maxcol)
    if maxrow==0 or maxcol==0:
        return 0
    if maxrow==1 and maxcol==1:
        return 1
    else:
        return grid_traversal_rec(maxrow-1,maxcol)+grid_traversal_rec(maxrow,maxcol-1)

#Memoization

def grid_traversal_memo(maxrow,maxcol,grid_arr={}):
    a=2*[[0]*3]
    rowcol=str(maxrow)+','+str(maxcol)
    if maxrow==0 or maxcol==0:
        return 0
    if maxrow==1 and maxcol==1:
        return 1
    if rowcol in grid_arr:
        return grid_arr[rowcol]
    else:
        grid_arr[rowcol]=grid_traversal_memo(maxrow-1,maxcol,grid_arr)+grid_traversal_memo(maxrow,maxcol-1,grid_arr)
    return grid_arr[rowcol]

print(grid_traversal_memo(18,18))

## Tabular Method

def grid_traversal_tab(row,col):
    table=[[0]*(col+1) for _ in range(row+1)]
    table[1][1] = 1
    for i in range(row+1):
        for j in range(col+1):
             if j+1 < col+1:
                table[i][j+1]+=table[i][j]
             if i+1 < row+1:
                table[i+1][j]+=table[i][j]
    return table[row][col]
    # #Printing the array
    #
    # for i in range(row+1):
    #     for j in range(col+1):
    #         print(table[i][j],end=" ")
    #     print("\n")

start=dt.now()
print(grid_traversal_tab(18,18))
end=dt.now()
print('Tabular Fun Duration : ',end-start)

start=dt.now()
print(grid_traversal_memo(18,18))
end=dt.now()
print('Memoization Fun Duration : ',end-start)

start=dt.now()
print(grid_traversal_rec(18,18))
end=dt.now()
print('Recursive Fun Duration : ',end-start)