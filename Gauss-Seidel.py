from math import fabs

n = 3
m = 0
A = [[30, 1, -1],
     [1, 20, -1],
     [1, 1, 10]]
B = [29, 38, 33]
x0 = [0.0, 0.0, 0.0]
x1 = [0.0, 0.0, 0.0]
e = 0.0001

while 1:
    e_max = 0.0
    for i in range(n):
        x0[i] = x1[i]
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s += A[i][j] * x1[j]
        x1[i] = (B[i] - s) / A[i][i]
        m += 1
        if fabs(x1[i] - x0[i]) > e_max:
            e_max = fabs(x1[i] - x0[i])
        print("e_max=%f" % e_max)
        print("\nX[%d]=%.5f\n " % (i, x1[i]))
    if e_max < e:
        break
print("迭代次数是：%d次\n" % (m / n))
for i in range(n):
    print('X%d = %.5f' % (i+1, x1[i]))
