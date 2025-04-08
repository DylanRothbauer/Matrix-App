import math as math 
import rowReducedSteps as rrefSteps
matrix = [[1, 2, 3], [1, 5, 6], [1, 8, 9]]

def rref(matrix):
    # Check if the first pivot is non-zero
    if rrefSteps.isFirstPivotnoneZero(matrix):
        # Perform row reduction steps

        print(matrix)
    
    
# Def findRowReductionSubtract(matrix):
#     for i in range(0, len(matrix)-1):
#         if matrix[0][0]-matrix[0][i]==1:

#chec a11 not equal zero then divide row by a11 to get 1 for pivot
# for i>1 if is not equal to 0 then 
            
rref(matrix)