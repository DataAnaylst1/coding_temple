import numpy as np
arr = np.array([1,2,3,4], ndmin=5)
#print(arr)
#print('number of dimension :', arr.ndim)


arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print('The element on the first row, second column is: ', (arr[0, 1]))

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print('The element on the 2nd row, 5th column is: ', (arr[1, 4]))

arr = np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]])
#print(arr[0,1,2])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

#print('The last element from the 2nd dim is: ', (arr[1,-1]))

arr = np.array([1,2,3,4,5,6,7])

#print(arr[1:5])

arr = np.array([1,2,3,4,5,6,7])
#print(arr[4:])

arr = np.array([1,2,3,4,5,6,7])
#print('These are the elements from the beginning until the 4th index: ', arr[:4])

arr = np.array([1,2,3,4,5,6,7])
#print('These are the elements from the 3rd index from the end to index 1 from the end: ', arr[-3:])

arr = np.array([1,2,3,4,5,6,7])
#print('Returning every other element from index 1 to index 5: ', arr[1:5:2])

arr = np.array([1,2,3,4,5,6,7])
#print("Returning every other element from the entire array: ", arr[::2])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print("These are the elements from the second element, starting from index 1 to index 4: ", arr[1, 1:4])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print(arr[0:2, 2])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#print(arr[0:2, 1:4])

arr = np.array([1,2,3,4])
#print(arr.dtype)

arr = np.array(['apple', 'banna', 'cherry'])
#print(arr.dtype)

arr = np.array([1,2,3,4], dtype='S')
#print(arr)
#print(arr.dtype)

arr = np.array([1,2,3,4], dtype='i4')
#print(arr)
#print(arr.dtype)
#arr = np.array(['a', '2', '3'], dtype='i')
#print(arr)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
#print(newarr)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
#print(newarr)

arr = np.array(([1,0,3])) #remember anything other than a 0 is considered True
newarr = arr.astype(bool)
#print(newarr)

arr = np.array([1,2,3,4,5])
x = arr.copy() # copy does not change the original, nor does the original change the copy, only the view changes the original and the original changes the view
arr[0] = 42
#print(arr)
#print(x)

arr = ([1,2,3,4,5])
x = arr
arr[0] = 42
#print(arr)
#print(x)

arr = np.array([[1,2,3,4], [5,6,7,8]])
#print(arr.shape)

arr = np.array([1,2,3,4], ndmin=5)
#print(arr)
#print(arr.shape)
arr = np.array([1,2,3,4,5])
#print(arr.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#newarr = arr.reshape(4,3)
#print(newarr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2) # two groups or "large arrays", three rows of apiece or smaller 'arrays' with two 2 columns each or 'elements
#print(newarr)
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1) #you are allowed to have -1 for a max of one dimension and NumPy will fill out the rest, (2,2-1) is the same as (2,2,2)
#print(newarr)

arr = np.array([[1,2,3], [4,5,6]])
newarr = arr.reshape(-1)
#print(newarr)

arr = np.array([1,2,3])

#for x in arr:
    #print(x)

arr = np.array([[1,2,3], [4,5,6]])
#for x in arr:
 #   print(x)

arr = np.array([[1,2,3], [4,5,6]])

#for x in arr: # this is how to iterate down a two dimensional array to return the actual values, iterate each scalar element
 #   for y in x:
  #      print(y)
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

#for x in np.nditer(arr):
 #   print(x)
#for x in arr:
#    print (x)
#for x in arr:
#    for y in x:
#        for z in y:
#            print(z)  
arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
#for x in np.nditer(arr):
 #   print(x)
arr = np.array([1,2,3])
#for x in np.nditer(arr,flags=['buffered'], op_dtypes=['S']): # you cannot change the data type while the element is in array. you have to ise nditer with the buffered
#    print(x)
