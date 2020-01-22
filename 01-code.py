a = 12
b = 21
c = a + b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is",c,sep='-')

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c),end='\n')
print("Sum of {1} and {0} is {2}".format(b,a,c))

# f-string
print(f"Sum of {a} and {b} is {c}")

# Multiline Print
print("""
1. Add
2. Sub
3. Div
4. Mul
""")
