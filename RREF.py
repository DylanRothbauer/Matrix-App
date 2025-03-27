import math as math 

matrix = [[0, 2, 3], [0, 5, 6], [0, 8, 9]]
def isOneInOtherRow(matrix):
    for i in range(0, len(matrix)-1):
        if matrix[0][0]-matrix[0][i]==1:
            return True
        else:
            return False
def  isFirstPivotIsOne(matrix):
    if matrix[0][0]==1:
        return True   
    else:
        return False 
def findFirstNonZero(matrix):
    for j in range(0, len(matrix)-1):
        for i in range(0, len(matrix)-1):
            if matrix[0][i]!=0:
                return j, i
def rref(matrix):
    currentPivot = []

    if isFirstPivotIsOne(matrix):
        print("1.pass")
    elif isOneInOtherRow(matrix):
        print("2.pass")
    else:
        #findRowReductionSubtract(matrix)
        print(findFirstNonZero(matrix))
        currentPivot = findFirstNonZero(matrix)
        print(currentPivot)
        print("fail")
# Def findRowReductionSubtract(matrix):
#     for i in range(0, len(matrix)-1):
#         if matrix[0][0]-matrix[0][i]==1:

            
rref(matrix)