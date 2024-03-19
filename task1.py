import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Визначення функцій для апроксимації
def exponential_demand(x, a, b):
    return a * np.exp(b * x)

def logarithmic_supply(x, c, d):
    return c * np.log(d * x + 1)

# Дані
price = np.array([0.1, 0.3, 0.45, 0.7, 0.8, 1.05, 1.2, 1.25, 1.31, 1.4, 1.47, 1.55])
demand = np.array([100, 69, 58, 40, 35, 20, 18, 17, 19, 21, 18, 15])
supply = np.array([10, 25, 39, 52, 60, 84, 91, 95, 97, 100, 105, 108])

# Підгонка моделей
popt_demand, _ = curve_fit(exponential_demand, price, demand, maxfev=10000)
popt_supply, _ = curve_fit(logarithmic_supply, price, supply, maxfev=10000)

# Параметри моделей
a_demand, b_demand = popt_demand
c_supply, d_supply = popt_supply

# Побудова графіків з апроксимованими функціями
prices_fine = np.linspace(price.min(), price.max(), 100)
demand_fitted = exponential_demand(prices_fine, *popt_demand)
supply_fitted = logarithmic_supply(prices_fine, *popt_supply)

plt.figure(figsize=(10, 6))
plt.scatter(price, demand, color='blue', label='Demand Data')
plt.plot(prices_fine, demand_fitted, 'b--', label='Fitted Demand')
plt.scatter(price, supply, color='red', label='Supply Data')
plt.plot(prices_fine, supply_fitted, 'r--', label='Fitted Supply')
plt.title('Fitted Demand and Supply vs. Price')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()

# Вивід параметрів моделей
print(f'Demand function parameters: a={a_demand}, b={b_demand}')
print(f'Supply function parameters: c={c_supply}, d={d_supply}')