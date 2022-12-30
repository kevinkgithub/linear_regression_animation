import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 100, 100)
y = x + np.random.normal(-10, 10, 100)

plt.show()
plt.xlim([0,100])
plt.ylim([0,100])

for i in range(len(x)):
    plt.scatter(x[i], y[i])
    plt.pause(0.1)

def gradient_descent():
    alpha = 0.0001
    iteration = 20
    cost = 0

    w = 0
    b = 0
    m = 100

    for i in range(iteration):
        y_pred = w * x + b

        plt.plot(x, y_pred)

        # Calculate cost (not used)
        # cost = (1/(2*m))*sum((y_pred - y)**2)

        # Calculate partial derivatives
        dj_dw = (1 / m) * sum((y_pred - y) * (x))
        dj_db = (1 / m) * sum(y_pred - y)

        # Update parameters
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
        print(f"w = {w}, b = {b} ")

        # Animate using pause function
        plt.pause(0.1)

gradient_descent()

plt.show()