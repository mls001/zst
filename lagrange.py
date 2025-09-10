x0 = 50000
y0 = 0.02
Fxy = 0
M = [0, 0, 0]
x = [20000, 40000, 60000]
y = [0.002, 0.01, 0.05]
F = [[0.028, 0.025, 0.023],
     [0.041, 0.040, 0.039],
     [0.073, 0.072, 0.072]]
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

print('%f' % Fxy)
