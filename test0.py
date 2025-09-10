from mods import lagrange, Gauss_Seidel  # 很好理解, 从 xxx 中导入 xxx 函数

x0 = 50000
y0 = 0.02
x = [20000, 40000, 60000]
y = [0.002, 0.01, 0.05]
F = [[0.028, 0.025, 0.023],
     [0.041, 0.040, 0.039],
     [0.073, 0.072, 0.072]]

result_lagrange = lagrange(x0, y0, F, x, y)
print(result_lagrange)

A = [[30, 1, -1],
     [1, 20, -1],
     [1, 1, 10]]
B = [29, 38, 33]
# Ax = B 的求解
result_Gauss_Seidel = Gauss_Seidel(3, A, B)  # 期待有人提交实现任意n阶的代码哦
