arr1 = np.array([1, 2, 3], dtype=np.float64)
#
import numpy as np
#
arr1 = np.array([1, 2, 3], dtype=np.float64)
#
arr1
#
# array([1., 2., 3.])
arr2 = np.array([1, 2, 3], dtype=np.int32)
#
arr2
#
# array([1, 2, 3], dtype=int32)
arr = np.array([1, 2, 3, 4, 5])
#
arr.dtype
#
# dtype('int64')
float_Arr = arr.astype(np.float64)
#
float_Arr
#
# array([1., 2., 3., 4., 5.])
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
#
arr
#
# array([ 3.7, -1.2, -2.6,  0.5, 12.9, 10.1])
arr.astype(np.in32)
#
arr.astype(np.int32)
#
# array([ 3, -1, -2,  0, 12, 10], dtype=int32)
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
#
numeric_strings.dtype
#
# dtype('S4')
numeric_strings
#
# array([b'1.25', b'-9.6', b'42'], dtype='|S4')
numeric_strings.astype(float)
#
# array([ 1.25, -9.6 , 42.  ])
numeric_strings.astype(float).dtype
#
# dtype('float64')
int_array = np.arange(10)
#
int_array
#
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
#
int_array.astype(calibers.dtype)
#
# array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
empty_uint32 = np.empty(8, dtype='u4')
#
empty_uint32
#
# array([ 505876062,          0,          0,          0, 1835347568,
#         679048304, 1679830072, 1701869940], dtype=uint32)
