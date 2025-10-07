import numpy as np 

# a = np.array([[1, 2],[3,4]])
# b = np.array([[5,6],[7,8]])

'Normal functions'

# print(a.shape,b.shape) #Tells row and column
# print(len(a),len(b))  #Tells the Length of the array
# print(a.ndim,b.ndim)  #Tells the dimension of the array
# print(a.size,b.size)  #Tells the total number of elements in the array
# print(a.dtype,b.dtype) #Tells the datatype of the array
# print(a.astype(str),b.astype(str)) #Converts the datatype of the array to string
# print(a.itemsize,b.itemsize) #Tells the size of each element in bytes

'Mathematical Funtions'

# print(np.add(a,b)) #Adds two arrays
# print(np.subtract(a,b)) #Subtracts two arrays
# print(np.multiply(a,b)) #Multiplies two arrays
# print(np.divide(a,b)) #Divides two arrays
# print(np.sqrt(a)) #Square root of each element in the array
# print(np.exp(a)) #Exponential of each element in the array
# print(np.power(a,2)) #Raises each element in the array to the power of 2
# print(np.sin(a)) #Sine of each element in the array

'Joining and Splitting in array'

# print(np.concatenate((a,b))) #Joins two arrays vertically
# print(np.vstack((a,b))) #Joins two arrays vertically
# print(np.hstack((a,b))) #Joins two arrays horizontally
# print(np.split(a,2)) #Splits the array into 2 equal parts
# print(np.array_split(a,2)) #Splits the array into 2 parts

'Inserts Functions'

# a = np.array([1,2,3,4])

# print(np.insert(a,2,5)) #Inserts 5 at index 2
# print(np.append(a,5)) #Appends 5 at the end
# print(np.delete(a,2)) #Deletes element at index 2
# print(np.unique([1,2,2,3,4,4,5])) #Returns unique elements in the array

'searching and sorting'

# a = np.array([3,1,2,4])

# print(np.where(a>2)) #Returns indices of elements greater than 2
# print(np.sort(a)) #Sorts the array

'Filtering in array'

# a = np.array([1,2,3,4,5,6,7,8,9,10])

# fa = a[a%2==0] #Filters even numbers
# fa1 = a[a>4] #Filters numbers greater than 4
# print(fa,fa1)

'Aggregate functions'

# price = np.array([12,5,15,7,19])
# quantity = np.array([2,4,1,3,5])

# print(np.sum(price)) #Sum of all elements
# print(np.mean(price)) #Mean/average of all elements
# print(np.min(quantity)) #Minimum element
# print(np.max(quantity)) #Maximum element
# print(np.size(price)) #Total/Count of elements
# print(np.cumsum(price)) #Cumulative sum of elements
# print(np.cumprod(price)) #Cumulative product of elements
# print(np.cumsum([price,quantity], axis=0)) #Cumulative sum of elements
# a = np.cumprod([price,quantity], axis=0) #Cumulative product of elements row-wise
# print(a[1].sum()) #Total sales (sum of price*quantity)

'Statistical functions'
import statistics as stats

# data = np.array([1,2,2,3,4,5,6,2,7,8,9])
# print(np.mean(data)) #Mean/average of all elements
# print(stats.mode(data)) #Mode of all elements
# print(np.median(data)) #Median of all elements
# print(np.std(data)) #Standard deviation of all elements
# print(np.var(data)) #Variance of all elements
# print(np.percentile(data, 50)) #50th percentile (median)
# print(np.corrcoef([1,2,3],[4,5,6])) #Correlation coefficient between two arrays

'Example of Coefficient of correlation'

# prices = np.array([10,20,30,40,50])
# sales = np.array([50,46,39,31,20])
# print(np.corrcoef(prices, sales))

'idhar prices badhe toh sales kam hue, iska matlab negative correlation hai'
'or agar prices badhe aur sales bhi badhe toh iska matlab positive correlation hai'



"Here we complete the learning of numpy functions"