import numpy as np
import matplotlib.pyplot as plt

# функция для вычисления разделённых разностей
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    # первая колонна - это y
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = \
                (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef


def newton_poly(coef, x_data, x):
# Вычисление полинома при x
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

x = np.array([-5, -1, 0, 2]) # вводим интересующие нас точки
y = np.sin(x)  # Вводим любую интересующую нас функцию
# получим коэффициенты разделённых разностей
a_s = divided_diff(x, y)[0, :]

# оцениваем по новым точкам данных
x_new = np.arange(-5, 2.1, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, y_new)
plt.show()