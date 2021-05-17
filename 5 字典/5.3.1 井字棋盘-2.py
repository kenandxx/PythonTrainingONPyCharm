# 允许输入着法的棋盘

theborad = {'Top-L': '', 'Top-M': '', 'Top-R': '',
            'Mid-L': '', 'Mid-M': '', 'Mid-R': '',
            'Low-L': '', 'Low-M': '', 'Low-R': '', }
def printboard(board):
    print(theborad['Top-L'] + '|' + theborad['Top-M'] + '|' + theborad['Top-R'] + '|'  )
    print('-+-+-')
    print(theborad['Mid-L'] + '|' + theborad['Mid-M'] + '|' + theborad['Mid-R'] + '|'  )
    print('-+-+-')
    print(theborad['Low-L'] + '|' + theborad['Low-M'] + '|' + theborad['Low-R'] + '|'  )
    print('-+-+-')

turn = 'X'
for i in range(9):
    printboard(theborad)
    print('Turn for ' + turn + '. Move on which space?' )
    move = input()
    theborad[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printboard(theborad)