# write a program to add two square matrix by numpy
a = [[1,2],[4,5]]
b = [[1,2],[4,5]]
c = [[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]
for i in range (len(c)):
    print(c[i])



