Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {"name":"Aman","age":39,"sal":35999,"dept":"IT"}
>>> type(data)
<class 'dict'>
>>> data.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> data['dept']
'IT'
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['address'] = 'Delhi'
>>> data
{'name': 'Aman', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
>>> data['name'] = 'Aman Sharma'
>>> data
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
>>> data.values()
dict_values(['Aman Sharma', 39, 35999, 'IT', 'Delhi'])
>>> data.items()
dict_items([('name', 'Aman Sharma'), ('age', 39), ('sal', 35999), ('dept', 'IT'), ('address', 'Delhi')])
>>> for item in data:
	print(item)

	
name
age
sal
dept
address
>>> for item in data:
	print(data[item])

	
Aman Sharma
39
35999
IT
Delhi
>>> for item in data:
	print(item,data[item])

	
name Aman Sharma
age 39
sal 35999
dept IT
address Delhi
>>> for item in data:
	print(data)

	
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
{'name': 'Aman Sharma', 'age': 39, 'sal': 35999, 'dept': 'IT', 'address': 'Delhi'}
>>> data.get('name')
'Aman Sharma'
>>> data.get('location')
>>> data['location']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data['location']
KeyError: 'location'
>>> data.get('location','Key Not Available')
'Key Not Available'
>>> 
