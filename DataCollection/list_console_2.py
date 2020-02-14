Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = ['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> c = data[:]
>>> import copy
>>> d = copy.deepcopy(data)
>>> d
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> c
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> data
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> d == data
True
>>> d is data
False
>>> d[-1]
[5, 6, 7, 8, 2]
>>> d[-1][0] = 50
>>> d
['hi', 'take care', 'ok', 'see you', [50, 6, 7, 8, 2]]
>>> data
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> import numpy as np
>>> data = [[4,5,7],[1,2,4],[8,7,4]]
>>> data
[[4, 5, 7], [1, 2, 4], [8, 7, 4]]
>>> np.array(data)
array([[4, 5, 7],
       [1, 2, 4],
       [8, 7, 4]])
>>> x = np.array(data)
>>> x
array([[4, 5, 7],
       [1, 2, 4],
       [8, 7, 4]])
>>> list(x)
[array([4, 5, 7]), array([1, 2, 4]), array([8, 7, 4])]
>>> y = list(x)
>>> y[0]
array([4, 5, 7])
>>> print(y)
[array([4, 5, 7]), array([1, 2, 4]), array([8, 7, 4])]
>>> print(y[0])
[4 5 7]
>>> list_1 = []
>>> for i in range(len(y)):
	list_1.append(y[i])

	
>>> list_1
[array([4, 5, 7]), array([1, 2, 4]), array([8, 7, 4])]
>>> x.flatten()
array([4, 5, 7, 1, 2, 4, 8, 7, 4])
>>> data
[[4, 5, 7], [1, 2, 4], [8, 7, 4]]
>>> data = [4,65,87,98,8,23,12,1,4,6]
>>> data.index(12)
6
>>> data = [4,65,87,98,8,23,12,1,4,6,12,4,4,6,12]
>>> data.index(12,7)
10
>>> data.count(4)
4
>>> d = [i for i in range(1,10)]
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> i
2
>>> d = [i for j in range(1,10)]
>>> d
[2, 2, 2, 2, 2, 2, 2, 2, 2]
>>> d = []
>>> for i in range(1,10):
	d.append(i)

	
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d = [j for j in range(1,10)]
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> j
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> d = [j for j in range(1,10)]
>>> d
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d = [j for j in range(1,10) if j % 2 == 0]
>>> d
[2, 4, 6, 8]
>>> d = []
>>> 7 in d
False
>>> dir(d)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> x = 12
>>> x = 12,
>>> type(x)
<class 'tuple'>
>>> x
(12,)
>>> x = 12,4,7,11,5,8
>>> 
>>> x
(12, 4, 7, 11, 5, 8)
>>> x[0]
12
>>> x[0:3]
(12, 4, 7)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
