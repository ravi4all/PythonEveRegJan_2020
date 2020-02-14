Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = list()
>>> data = [1 to 100]
SyntaxError: invalid syntax
>>> data = range(1,100)
>>> data
range(1, 100)
>>> data = list(range(1,10))
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> data.append("hello")
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello']
>>> data = []
>>> data.append("hello")
>>> data
['hello']
>>> data.append("hi")
>>> data
['hello', 'hi']
>>> data.append("bye","ok","see you")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data.append("bye","ok","see you")
TypeError: append() takes exactly one argument (3 given)
>>> data.append(["bye","ok","see you"])
>>> data
['hello', 'hi', ['bye', 'ok', 'see you']]
>>> data.pop()
['bye', 'ok', 'see you']
>>> data.extend(["bye","ok","see you"])
>>> data
['hello', 'hi', 'bye', 'ok', 'see you']
>>> data.pop(2)
'bye'
>>> _
'bye'
>>> data.insert(2,_)
>>> data
['hello', 'hi', 'bye', 'ok', 'see you']
>>> data.index("hi")
1
>>> data.remove(2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
>>> data.remove("hi")
>>> data
['hello', 'bye', 'ok', 'see you']
>>> sorted(data)
['bye', 'hello', 'ok', 'see you']
>>> sorted(data,reverse=True)
['see you', 'ok', 'hello', 'bye']
>>> data
['hello', 'bye', 'ok', 'see you']
>>> data.sort()
>>> data
['bye', 'hello', 'ok', 'see you']
>>> data[0]
'bye'
>>> data[0:3]
['bye', 'hello', 'ok']
>>> data[0] = 'hi'
>>> data
['hi', 'hello', 'ok', 'see you']
>>> data[0:2] = ["bye","take care"]
>>> data
['bye', 'take care', 'ok', 'see you']
>>> a = data
>>> a[0] = 'hi'
>>> a
['hi', 'take care', 'ok', 'see you']
>>> data
['hi', 'take care', 'ok', 'see you']
>>> b = data[:]
>>> data[]
SyntaxError: invalid syntax
>>> b = data[:]
>>> b
['hi', 'take care', 'ok', 'see you']
>>> data
['hi', 'take care', 'ok', 'see you']
>>> a
['hi', 'take care', 'ok', 'see you']
>>> a == b
True
>>> a == data
True
>>> a is data
True
>>> a == b
True
>>> a is b
False
>>> b[0] = "bye"
>>> b
['bye', 'take care', 'ok', 'see you']
>>> a
['hi', 'take care', 'ok', 'see you']
>>> data
['hi', 'take care', 'ok', 'see you']
>>> data.append([5,6,7,8,2])
>>> data
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> a
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> b
['bye', 'take care', 'ok', 'see you']
>>> c = data[:]
>>> c
['hi', 'take care', 'ok', 'see you', [5, 6, 7, 8, 2]]
>>> c[-1]
[5, 6, 7, 8, 2]
>>> c[-1][0] = 100
>>> c
['hi', 'take care', 'ok', 'see you', [100, 6, 7, 8, 2]]
>>> data
['hi', 'take care', 'ok', 'see you', [100, 6, 7, 8, 2]]
>>> c[0] = 'bye'
>>> c
['bye', 'take care', 'ok', 'see you', [100, 6, 7, 8, 2]]
>>> data
['hi', 'take care', 'ok', 'see you', [100, 6, 7, 8, 2]]
>>> data[:[:]]
SyntaxError: invalid syntax
>>> 
