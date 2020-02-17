Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py 
Enter your search : apple
Sort products price wise...

1. Low to High
2. High to Low

Enter your choice : 
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py", line 27, in <module>
    ch = input("Enter your choice : ")
KeyboardInterrupt
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py 
Enter your search : apple
{'p_name': 'Apple Iphone 11', 'brand': 'Apple', 'Category': 'Mobile', 'price': 98000}
{'p_name': 'Macbook Pro', 'brand': 'Apple', 'Category': 'Laptop', 'price': 128000}
Sort products price wise...

1. Low to High
2. High to Low

Enter your choice : 2
>>> sorted(searchResults)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sorted(searchResults)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> data = [4,5,7,8,9,3,2,3,5,79]
>>> sorted(data)
[2, 3, 3, 4, 5, 5, 7, 8, 9, 79]
>>> data = [[4,5,7],[7,9,0],[2,4,6]]
>>> sorted(data)
[[2, 4, 6], [4, 5, 7], [7, 9, 0]]
>>> data = [[4,5,7],[7,9,0],[2,4,6],[1,5,6],[6,3,3]]
>>> sorted(data)
[[1, 5, 6], [2, 4, 6], [4, 5, 7], [6, 3, 3], [7, 9, 0]]
>>> data = [['ram',45],['aman',20],['sumit',19],['anubhav',28]]
>>> sorted(data)
[['aman', 20], ['anubhav', 28], ['ram', 45], ['sumit', 19]]
>>> sorted(data,key=1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sorted(data,key=1)
TypeError: 'int' object is not callable
>>> def show(x):
	return x[1]

>>> sorted(data,key=show)
[['sumit', 19], ['aman', 20], ['anubhav', 28], ['ram', 45]]
>>> for i in range(len(data)):
	print(show(data[i]))

	
45
20
19
28
>>> def show(x):
	return x['price']

>>> sorted(searchResults,key=show)
[{'p_name': 'Apple Iphone 11', 'brand': 'Apple', 'Category': 'Mobile', 'price': 98000}, {'p_name': 'Macbook Pro', 'brand': 'Apple', 'Category': 'Laptop', 'price': 128000}]
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py 
Enter your search : mobile
Sort products price wise...

1. Low to High
2. High to Low

Enter your choice : 
Traceback (most recent call last):
  File "C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py", line 35, in <module>
    ch = input("Enter your choice : ")
KeyboardInterrupt
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py 
Enter your search : mobile
{'p_name': 'Apple Iphone 11', 'brand': 'Apple', 'Category': 'Mobile', 'price': 98000}
{'p_name': 'Redmi Note 6', 'brand': 'Xiaomi', 'Category': 'Mobile', 'price': 15000}
Sort products price wise...

1. Low to High
2. High to Low

Enter your choice : 1
>>> 
 RESTART: C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2020\Jan\PythonEveReg\PythonEveRegJan_2020\DataCollection\dict_exercise_2.py 
Enter your search : shoes
{'p_name': 'Sports Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 3400}
{'p_name': 'Puma Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 2070}
{'p_name': 'Adidas Sports Shoes', 'brand': 'Adidas', 'Category': 'Shoes', 'price': 1900}
Sort products price wise...

1. Low to High
2. High to Low

Enter your choice : 2
[{'p_name': 'Sports Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 3400}, {'p_name': 'Puma Shoes', 'brand': 'Puma', 'Category': 'Shoes', 'price': 2070}, {'p_name': 'Adidas Sports Shoes', 'brand': 'Adidas', 'Category': 'Shoes', 'price': 1900}]
>>> s1 = {3,5,6,8,9,9,2,1,3,4,5,6,7,98,12,23,45,8,3}
>>> s1
{1, 2, 3, 4, 5, 6, 7, 8, 9, 98, 12, 45, 23}
>>> s2 = {4,5,7,9,3,2,4,6,8,9,21,45,8}
>>> s2
{2, 3, 4, 5, 6, 7, 8, 9, 45, 21}
>>> s1 & s2
{2, 3, 4, 5, 6, 7, 8, 9, 45}
>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 21, 23, 98, 45}
>>> s1 - s2
{1, 98, 12, 23}
>>> s1.intersection(s2)
{2, 3, 4, 5, 6, 7, 8, 9, 45}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 21, 23, 98, 45}
>>> 
