from math import fabs


def lagrange(x0, y0, F, x, y):
    """
    :param x0: 待插点x0
    :param y0: 待插点y0
    :param F: F矩阵
    :param x: x矩阵
    :param y: y矩阵
    :return: 插值
    """
    M = [0, 0, 0]
    Fxy = 0
    for i in range(3):
        Fy = 0
        for j in range(3):
            a = 1.0
            for n in range(3):
                if j == n:
                    continue
                a *= (x0 - x[n]) / (x[j] - x[n])
            Fy += a * F[i][j]
        M[i] = Fy
        print('%f' % M[i])
    for i in range(3):
        a = 1.0
        for n in range(3):
            if i == n:
                continue
            a *= (y0 - y[n]) / (y[i] - y[n])
        Fxy += a * M[i]
    return Fxy


def Gauss_Seidel(n, A, B):
    """
    :param n: 行列式阶数
    :param A: 系数矩阵
    :param B: 常数向量
    """
    x0 = [0.0, 0.0, 0.0]
    x1 = [0.0, 0.0, 0.0]
    e = 0.0001
    m = 0
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
        print('X%d = %.5f' % (i + 1, x1[i]))
