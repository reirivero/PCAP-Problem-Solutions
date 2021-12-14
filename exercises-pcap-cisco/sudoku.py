def isSudoku(sdk):
    # Verify the rows
    rows = sdk.split()
    for row in rows:
        for val in range(1,10):
            if row.count(str(val)) != 1:
                return print("No")
    
    # Verify the columns
    cols = []
    for i in range(9):
        val = ''
        for j in range(9):
            val += rows[j][i]
        cols.append(val)
    
    for col in cols:
        for val in range(1,10):
            if col.count(str(val)) != 1:
                return print("No")
    

    #colrow = [list(col) for col in rows]
    # Verify every square
    sq = 0
    row = 0
    while True:
        colrow = (rows[row][sq : sq + 3] + rows[row+1][sq : sq + 3] + rows[row+2][sq : sq + 3])
        #print(colrow)
        for val in range(1,10):
            if colrow.count(str(val)) != 1:
                return print("No")
        row += 3
        if row == 6 and sq == 6:
            return print("Yes")
        elif row == 6:
            row = 0
            sq += 3



if __name__ == '__main__':
    isSudoku("""295743861
    431865927
    876192543
    387459216
    612387493
    549216738
    763524189
    928671354
    154938672""")

    isSudoku("""295743861
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    154938672""" )

    #isSudoku("""295743861
    #431865927
    #876192543
    #387459216
    #612387495
    #549216738
    #763524189
    #928671354
    #154938672""")
    