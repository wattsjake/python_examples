import numpy as np
import time

def determinant_recursive(A, total=0):    
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
     
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    # Section 3: define submatrix for focus column and 
    #      call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = A*1 # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D) 
 
        for i in range(height): 
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) # F) 
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det 
 
    return total

def cramers_rule(A,b):
    #matrix A needs to be converted to list to work in the determinant function
    A_list = A.tolist()
    #find the determinant of A_list
    detA = determinant_recursive(A_list)
    
    #create a list to hold the results
    result = []
    #iterate through b and create a tempA matrix for each iteration
    for i in range(len(b)):
        #create a tempA matrix
        tempA = A*1
        #replace each position in A with b
        tempA[0:,i] = b[:,0]
        #convert tempA to list
        tempA_list = tempA.tolist()
        #compute result
        result.append(determinant_recursive(tempA_list)/detA)
        print(i)
    return result
    
#Start timer
start_time = time.time()

#create the two matrix
A = np.array([[2,3,-7],
              [4,9,-3],
              [10,1,-4.5]])

b = np.array([[3],
             [9],
             [10]])
# A = np.array([[0,1,2,3,4,5,6,123],
#               [2,5,8,4,5,6,7,34],
#               [7,8,9,4,5,6,8,8],
#               [6,5,2,1,4,5,10,8],
#               [4,2,3,0,5,1,12,1],
#               [0,8,4,9,5,52,2,0],
#               [6,8,4,9,4,524,23,8],
#               [2,82,4,94,5,5,23,4]])
# b = np.array([[10],
#               [1],
#               [1],
#               [8],
#               [6],
#               [4],
#               [6],
#               [9]])


#compute the results using cramer's method
result = cramers_rule(A,b)
#Print the elapsed time
print("elapsed time: %s" % (time.time() - start_time))

for i in range(len(result)):
    print('x[%d]: %f' %(i,result[i]))

#test the determinant with linalg
A_list = A.tolist()
Det = determinant_recursive(A_list)
npDet = np.linalg.det(A_list)
print("Determinant of A is", round(Det,9))
print("The Numpy Determinant of A is", round(npDet,9))

# #create the two matrix
# A = np.array([[0,1,2,3,4,5,6,123,54,2,1],
#               [2,5,8,4,5,6,7,34,43,4,5],
#               [7,8,9,4,5,6,8,75,5,5,3],
#               [6,5,2,1,4,5,10,574,43,2,7],
#               [4,2,3,0,5,1,12,45,1,5,4],
#               [0,8,4,9,5,52,23,5,5,7,8],
#               [6,8,4,9,4,524,23,7,56,5,2],
#               [2,82,4,94,5,5,23,5,76,3,6],
#               [2,5,8,14,5,6,75,4,4,7,6],
#               [2,51,8,14,9,6,5,0,4,7,9],
#               [2,1,8,4,9,6,5,5,4,74,7]])
# b = np.array([[10],
#               [1],
#               [1],
#               [8],
#               [6],
#               [4],
#               [6],
#               [3],
#               [1],
#               [2],
#               [2]])