import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# تعریف پارامترهای سیستم
a2, a1, a0 = 1, 5, 6  # ضرایب معادله دیفرانسیل
b1, b0 = 0, 1  # ضرایب ورودی

# معادله دیفرانسیل برای سیستم LTI
def system(y, t, x_t):
    y1, y2 = y
    dy1dt = y2
    dy2dt = (b0 * x_t - a1 * y2 - a0 * y1) / a2
    return [dy1dt, dy2dt]

# دامنه زمانی
t = np.linspace(0, 10, 1000)

# تعریف ورودی‌ها
x_step = np.heaviside(t, 1)  # ورودی پله
x_impulse = np.zeros_like(t)  # ورودی ضربه
x_impulse[0] = 1  # ضربه در t=0
x_sin = np.cos(2 * np.pi * t)  # ورودی سینوسی

# حل سیستم برای ورودی پله
y0 = [0, 0]  # شرایط اولیه
sol_step = odeint(system, y0, t, args=(x_step[0],))

# رسم پاسخ سیستم به ورودی پله
plt.plot(t, sol_step[:, 0], label='Response to Step Input')
plt.xlabel('Time')
plt.ylabel('Output y(t)')
plt.title('System Response to Step Input')
plt.grid(True)
plt.legend()
plt.show()
