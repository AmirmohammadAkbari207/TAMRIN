import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


alpha = 0.1   
beta = 0.02   
delta = 0.01  
gamma = 0.1   


H0 = int(input("تعداد اولیه آهوها: "))  
W0 = int(input("تعداد اولیه گرگ‌ها: "))  
t = np.linspace(0, 500, 1000)


def lotka_volterra(y, t, alpha, beta, delta, gamma):
    H, W = y
    dHdt = alpha * H - beta * H * W
    dWdt = delta * H * W - gamma * W
    return [dHdt, dWdt]


sol = odeint(lotka_volterra, [H0, W0], t, args=(alpha, beta, delta, gamma))


plt.figure(figsize=(8, 5))
plt.plot(t, sol[:, 0], label="آهوها (H)", color="green")
plt.plot(t, sol[:, 1], label="گرگ‌ها (W)", color="red")
plt.axhline(y=gamma/delta, color='blue', linestyle="--", label="تعادل گرگ‌ها")
plt.axhline(y=alpha/beta, color='orange', linestyle="--", label="تعادل آهوها")
plt.xlabel("زمان")
plt.ylabel("جمعیت")
plt.title("تعادل جمعیت شکار و شکارچی")
plt.legend()
plt.grid()
plt.show()
