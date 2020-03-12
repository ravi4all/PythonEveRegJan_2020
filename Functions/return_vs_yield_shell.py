Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		return x
		print("hello")

		
>>> counter()
1
>>> x = 0
>>> def counter():
	x += 1
	return x

>>> def counter():
	x = x + 1
	return x

>>> counter()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    counter()
  File "<pyshell#20>", line 2, in counter
    x = x + 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	print("X is",x)
	x = x + 1
	return x

>>> counter()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    counter()
  File "<pyshell#23>", line 2, in counter
    print("X is",x)
UnboundLocalError: local variable 'x' referenced before assignment
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonEveReg/PythonEveRegJan_2020/Functions/return_vs_yield.py 
X is 0
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonEveReg/PythonEveRegJan_2020/Functions/return_vs_yield.py 
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonEveReg/PythonEveRegJan_2020/Functions/return_vs_yield.py", line 7, in <module>
    counter()
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2020/Jan/PythonEveReg/PythonEveRegJan_2020/Functions/return_vs_yield.py", line 3, in counter
    print("X is",x)
UnboundLocalError: local variable 'x' referenced before assignment
>>> def counter():
	x = 0
	while x < 10:
		x += 1
		yield x
		print("Updating X...")

		
>>> counter()
<generator object counter at 0x000002FC88913B88>
>>> c = counter()
>>> next(c)
1
>>> next(c)
Updating X...
2
>>> next(c)
Updating X...
3
>>> next(c)
Updating X...
4
>>> next(c)
Updating X...
5
>>> for i in counter():
	print(i)

	
1
Updating X...
2
Updating X...
3
Updating X...
4
Updating X...
5
Updating X...
6
Updating X...
7
Updating X...
8
Updating X...
9
Updating X...
10
Updating X...
>>> 
