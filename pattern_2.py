'''
    *
   ***
  *****
 *******
*********
'''
for i in range(7):
    print(' ' * (7 - i) + '*' * (2*i + 1))
print("="*10)
# Alternative
n = 7
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for k in range(2*i + 1):
        print('*',end='')
    print()
print("="*10)
'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
a = 0
for i in range(1,5):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        a += 1
        print(a,end=' ')
    print()
print("="*10)














