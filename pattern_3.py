'''
a
ab
abc
abcd
abcde
'''
'''
for i in range(5):
    for j in range(i+1):
        print(chr(ord('a')+j),end='')
    print()
'''

for i in range(5):
    num = 96
    for j in range(i+1):
        num += 1
        print(chr(num),end='')
    print()
print("="*20)

num = 96
for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i+1):
        num += 1
        print(chr(num),end=' ')
    print()
