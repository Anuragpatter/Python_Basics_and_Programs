import numpy as np
vector_row = np.array([3,4,5])           # Creating a row vector     
print(vector_row)

# The symbol [] represents a row, if we put elements inside the square brackets then
# it represents a row so here in order to create a column vector
# we need three rows to form one column hence every element is in [] notation.

vec_col = np.array([[3],[4],[6]])          # Creating a column vector
print(vec_col)

# Numpy's main data structure is MULTI-DIMENSIONAL ARRAYS.
# To create a vector, simply create 1 dimensional array which can be represented horizontally(rows) and vertically(columns) same as vectors.

matrix = np.array([[1,2],[3,5],[6,3]])   #Creating a Matrix using numpy two dimensional array containing 3 rows and 2 columns.
print(matrix)

# Numpy has dedicated DS for Matrix, that is:-

matrix_obj = np.mat([[1,2],[1,2],[1,2]])
print(matrix_obj)

# This matrix DS is Not recommended:- 
#1. Arrays are de facto DS of Numpy  
#2. Majority Numpy operations returns arrays not matrix objects. 

# Creating a SPARSE matrix.
# Sparse matrix represents data with very few zeros.

from scipy import sparse
matrix = np.array([[0,0],[0,1],[3,0]])
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)
print(matrix)

# The format of sparse matrix is the position of element --  the element itself.
# Sparse matrices only store non-zero elements and assume all other values will be zero, leading to significant computational savings.
# Compressed sparse row matrices (CSR) represents the zero-indexed.