Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	return x + y

>>> add(4,5)
9
>>> def calc(x):
	return x

>>> calc(add(4,5))
9
>>> def calc(x,y):
	return lambda x,y : x + y

>>> calc(4,5)
<function calc.<locals>.<lambda> at 0x000001536389C268>
>>> def calc():
	return lambda x,y : x + y

>>> calc()
<function calc.<locals>.<lambda> at 0x00000153643B87B8>
>>> add = calc()
>>> add(4,5)
9
>>> def calc():
	def add(x,y):
		return x + y
	return add

>>> calc()
<function calc.<locals>.add at 0x00000153643B8840>
>>> add = calc()
>>> add(4,5)
9
>>> string = "[1,2,4,6]"
>>> list(string)
['[', '1', ',', '2', ',', '4', ',', '6', ']']
>>> import string
>>> string.split(",")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    string.split(",")
AttributeError: module 'string' has no attribute 'split'
>>> text = "[1,2,4,6]"
>>> text.split(",")
['[1', '2', '4', '6]']
>>> import re
>>> text = "Hello Ram, Your salary is 25000 and your id is ram122@gmail.com"
>>> re.match('/[A-Z]\w+/', text)
>>> re.match('[A-Z]\w+', text)
<re.Match object; span=(0, 5), match='Hello'>
>>> re.findall('[A-Z]\w+',text)
['Hello', 'Ram', 'Your']
>>> re.findall('[0-9]\d+',text)
['25000', '122']
>>> re.findall('[0-9]\d{5}',text)
[]
>>> re.findall('[0-9]\d{4}',text)
['25000']
>>> text = "Hello Ram, Your salary is 25000rs and your id is ram122@gmail.com"
>>> re.findall('[0-9]\d{4}+[a-z]\w+',text)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    re.findall('[0-9]\d{4}+[a-z]\w+',text)
  File "C:\Python37\lib\re.py", line 223, in findall
    return _compile(pattern, flags).findall(string)
  File "C:\Python37\lib\re.py", line 286, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Python37\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Python37\lib\sre_parse.py", line 930, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "C:\Python37\lib\sre_parse.py", line 426, in _parse_sub
    not nested and not items))
  File "C:\Python37\lib\sre_parse.py", line 654, in _parse
    source.tell() - here + len(this))
re.error: multiple repeat at position 10
>>> re.findall('([0-9]\d{4})+([a-z]\w+)',text)
[('25000', 'rs')]
>>> re.findall('[a-z|0-9]\w+[@]\w+[.]\w{2,3}',text)
['ram122@gmail.com']
>>> re.search('[a-z|0-9]\w+[@]\w+[.]\w{2,3}',text)
<re.Match object; span=(49, 65), match='ram122@gmail.com'>
>>> re.search('[A-Z]\w+', text)
<re.Match object; span=(0, 5), match='Hello'>
>>> re.match('[A-Z]\w+', text)
<re.Match object; span=(0, 5), match='Hello'>
>>> text
'Hello Ram, Your salary is 25000rs and your id is ram122@gmail.com'
>>> re.match('[a-z]\w+', text)
>>> re.match('[a-z]', text)
>>> re.search('[a-z]', text)
<re.Match object; span=(1, 2), match='e'>
>>> re.search('[a-z]\w+', text)
<re.Match object; span=(1, 5), match='ello'>
>>> 
