import pprint
theBorad = {'Top-L': 'X', 'Top-M': 'X', 'Top-R': 'O',
            'Mid-L': 'X', 'Mid-M': 'O', 'Mid-R': 'O',
            'Low-L': 'O', 'Low-M': 'X', 'Low-R': 'X', }
def printboard(board):
    print(theBorad['Top-L'] + '|' + theBorad['Top-M'] + '|' + theBorad['Top-R'] + '|'  )
    print('-+-+-')
    print(theBorad['Mid-L'] + '|' + theBorad['Mid-M'] + '|' + theBorad['Mid-R'] + '|'  )
    print('-+-+-')
    print(theBorad['Low-L'] + '|' + theBorad['Low-M'] + '|' + theBorad['Low-R'] + '|'  )
    print('-+-+-')

print(theBorad)
pprint.pprint(theBorad)
print()
printboard(theBorad)