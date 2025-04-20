import numpy as np
#
arr = np.arange(10)
#
arr
#
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[5]
#
# 5
arr[5:8]
#
# array([5, 6, 7])
arr[5:8] = 12
#
arr
#
# array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
arr_slice = arr[5:8]
#
arr_slice
#
# array([12, 12, 12])
arr_slice[1] = 12345
#
arr
#
# array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,
#            9])
arr_slice[:] = 64
#
arr
#
# array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
arr[5:8].copy()
#
# array([64, 64, 64])
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
arr2d[2]
#
# array([7, 8, 9])
arr2d[0][2]
#
# 3
arr2d[0, 2]
#
# 3
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
arr3d
#
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
# 
#        [[ 7,  8,  9],
#         [10, 11, 12]]])
arr3d[0]
#
# array([[1, 2, 3],
#        [4, 5, 6]])
old_values = arr3d[0].copy()
#
arr3d[0] = 42
#
arr3d
#
# array([[[42, 42, 42],
#         [42, 42, 42]],
# 
#        [[ 7,  8,  9],
#         [10, 11, 12]]])
arr3d[0] = old_values
#
arr3d
#
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
# 
#        [[ 7,  8,  9],
#         [10, 11, 12]]])
arr3d[1, 0]
#
# array([7, 8, 9])
x = arr3d[1]
#
x
#
# array([[ 7,  8,  9],
#        [10, 11, 12]])
x[0]
#
# array([7, 8, 9])
