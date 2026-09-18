import numpy as np

# a = np.array([3,4])
# print(a)

# b = [1,2,3,4]
# c = np.array([b])
# print(c)
# print(type(c))

# #Can be created by both 

# #User entered value-----------------------------------------------------------------------

# l = []

# for i in range(4):

#     a = int(input("Enter: "))
#     l.append(a)

# arr = np.array(l)
# print(arr)
# print(type(arr))

#Dimensiton also asked to user-------------------------------------------------------------

# num = int(input("Enter the number of array you need: "))
# l = []

# for i in range(num):
#     val = int(input(f"Enter value of for number {i + 1}: "))
#     l.append(val)

# y = np.array([[l]])
# print(y.ndim)

# [[]] - 2D Array
# [[[]]] - 3D Array

# d2arr = np.array([[1,2,3,4],[1,2,3,4]])
# d3arr = np.array([[[1,2,3],[1,2,3],[1,2,3]]])

# print(d3arr)
# print(d2arr)
# print(d2arr.ndim)
# print(d3arr.ndim)

# To Create Array of Random Dimension

# d3arr = np.array([1,2,3,4],ndmin = 10)
# print(d3arr)
# print(d3arr.ndim)
# print(d3arr.shape)

# SHAPE AND RESHAPE IN NUMPY

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a.shape)

# b = np.array([[1,2,3],[1,2,3]])
# print(b.shape)

# #RESHAPING ARRAY
# np3 = a.reshape(2,6)
# print(np3)
# print(np3.shape)

# np4 = a.reshape(2,2,3)
# print(np4)
# print(np4.shape)

# #Flatten to 1-d (COnversion of 3D -> 1D)
# np5 = np4.reshape(-1)
# print(np5)
# print(np5.size)
# print(a.size)

# print(a.dtype)
# b = np.array(['Hello','Hi','Tata'])
# print(b.dtype)
# c = np.array([2.0,3.1,4.2])
# print(c.dtype)

# # np.zeros()
# d = np.zeros(2,dtype=int)
# print(d)

# e = np.zeros((2,3),dtype=int)
# print(e)

# e = np.zeros((3,2,1),dtype=int)
# print(e)

# #np.ones
# d = np.ones(2,dtype=int)
# print(d)

# e = np.ones((2,3),dtype=int)
# print(e)

# e = np.ones((3,2,1),dtype=int)
# print(e)

#np full 1D Array
# f1 = np.full(5,79)
# print(f1)
# print(f1.shape)
# print(f1.dtype)

# f2 = np.full(5,80,dtype=float)
# print(f2)
# print(f2.shape)
# print(f2.dtype)


#np full 2D Array

# f1 = np.full((2,3),50.9,dtype=int)
# print(f1)
# print(f1.dtype)


# f2 = np.full((2,3),'a')
# print(f2)
# print(f2.dtype)

# f2 = np.full((2,3),'a')
# print(f2)
# print(f2.dtype)

#np full 3D array

# f1 = np.full((2,5,2),'Python')
# print(f1)
# print(f1.size)

# np.arrange()

# print(np.arange(1,20,2))
# print(np.arange(20))

# print(np.arange(1,100,5,dtype=float))

#ArrrayIndexing

#1D Array

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a.shape)
# print(a[1]) #Positive Indexing
# print(a[-2]) #Negative Indexing

# print(a[7])

# #2D Array

# b = np.array([[1,2,3],
#              [4,5,6],
#              [7,8,9]])

# print(b[2,2])

# c = np.array([[[1,2,3],[1,5,6],[1,1,1],[4,2,4]]])
# print(c)
# print(c[0,2,2])

# #3D array with multiple layer
# import numpy as np

# a = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],

#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# print(a)
# print(a.shape)
# # print(a[1,1,1])

# #Slicing in Array

# #1D Array
# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a[2:5])
# print(a[2:])
# print(a[:5])
# print(a[1:5:2])
# print(a[::2])

# b = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12],
#               [13,14,15,16]])

# print(b[0:2,0:3])
# print(b[0])
# print(b[1,1:3])

# a = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])

# #Accessing Elements-------------------------------------------------------------------------
# # 1. Access the value 10.

# print(a[0,0])

# # 2. Access the value 80.
# print(a[1,3])

# # 3. Access the value 110.
# print(a[2,2])

# # 4. Access the value 150.
# print(a[3,2])

# #Accessing Entire Row-----------------------------------------------------------------------

# # 5. Access the entire first row.

# print(a[0])

# # 6. Access the entire third row.
# print(a[2])

# # 7. Access the entire fourth row.
# print(a[3])

# #Accessing Entire Columns-----------------------------------------------------------------------

# # 8. Access the entire first column.

# print(a[0:4,0])

# # 9. Access the entire third column.

# print(a[0:4,2])

# # 10. Access the entire fourth column.
# print(a[0:4,3])

# # 11. Access rows 0 and 1, with all columns.
# print(a[0:2,0:4])

# # 12. Access rows 1 and 2, with all columns.
# print(a[1:3,0:4])

# # 13. Access rows 0, 1 and 2, with all columns.
# print(a[0:3,0:4])

# # 14. Access:

# # 20  30
# # 60  70

# print(a)
# print(a[0:2,1:3])

# # 15. Access:

# # 60   70   80
# # 100  110  120
# print(a)
# print(a[1:3,1:4])

# # 16. Access:

# # 90   100
# # 130  140

# print(a[2:4,0:2])
# print(a)

# #a(2,3) = 120
# #a[1:] = [ 50  60  70  80]
# # a[:, 2] = [30 70 110 15]
# #a[0:2, 1:3] = [[20,30],[60,70]]

# Vector Arithmetic ⭐
# Vector addition
# Vector subtraction
# Scalar multiplication
# Scalar division
# Component-wise multiplication
# Component-wise operations
