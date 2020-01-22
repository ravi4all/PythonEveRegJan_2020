'''
Loops
- for
- while
'''
# for i in range(5):print(i)
# Indentation -> 4 spaces (python standard)
'''
range(stop)
range(5)
start -> 0
stop  -> 5-1 = 4
step  -> 1
'''
for i in range(5):
    print(i)

print("="*10)
'''
range(start,stop)
range(2,21)
start -> 2
stop  -> 21-1 = 20
step  -> 1
'''
for i in range(2,21,1):
    print(i)
print("="*10)


'''
range(start,stop,step)
range(2,21,2)
start -> 2
stop  -> 21-1 = 20
step  -> 2
'''
for i in range(2,21,2):
    print(i)

print("="*10)

# Reverse Loop
for i in range(10,0,-1):
    print(i)
