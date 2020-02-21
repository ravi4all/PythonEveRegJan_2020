def find_max(x,y,z):
    return x if x > y and x > z else y if y > x and y > z else z

m = find_max(4,7,2)
print(m)