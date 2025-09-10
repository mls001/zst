def double_your_money(r):
    """
    :param r: 你的幻想利率
    :return: 你幻想某年本金翻倍
    """
    year = 0
    money = 1
    if money < 2:
        money *= 1.0 + r
        year += 1
    return year


def difference_methods(n, X, Y):
    """
    :param n: dx
    :param X: X矩阵
    :param Y: Y矩阵
    """
    Y1 = []
    for i in range(len(Y) - 1):
        Y1.append(Y[i + 1] - Y[i])
    Y2 = []
    for i in range(len(Y1) - 1):
        Y2.append(Y1[i + 1] - Y1[i])
    a0 = []
    a1 = []
    a2 = []
    for i in range(len(Y2)):
        a0.append(Y[i] - Y1[i] / n * X[i] + Y2[i] / n / n / 2 * X[i] * X[i + 1])
        a1.append(Y1[i] / n - Y2[i] / n / n / 2 * (X[i] + X[i + 1]))
        a2.append(Y2[i] / n / n / 2)
    A = [sum(a0) / 4, sum(a1) / 4, sum(a2) / 4]
    print('y = %f + %.3e * x + %.3e * x^2' % (A[0], A[1], A[2]))


def dixon(d0, X):
    X.sort()
    print(X)
    X.sort(reverse=True)
    print(X)
    if (X[0] - X[1]) > (X[-2] - X[-1]):
        p = X[0] - X[1]
        m = X[0]
    else:
        p = (X[-2] - X[-1])
        m = X[-1]
    d = p / (X[0] - X[-1])
    print(d)
    if d > d0:
        print("有离群值，为%f" % m)
    else:
        print("无离群值")
