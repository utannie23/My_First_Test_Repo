import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
E = 50 
r = 10  
def R(I):
    return 100 * np.exp(-0.025 * I**2)
U_diode_data = np.array([0, 0.9, 1.1, 1.3])  # U, В
I_diode_data = np.array([0, 1.2, 2.7, 5.6])  # I, А
from scipy.interpolate import interp1d
U_diode = interp1d(I_diode_data, U_diode_data, kind='linear', fill_value="extrapolate")

def equation(I):
    return E - I * (r + R(I)) - U_diode(I)
I_range = np.linspace(0, 6, 100)
y = equation(I_range)
plt.figure(figsize=(10, 6))
plt.plot(I_range, y, label='E - I·(r + R(I)) - U(I)')
plt.axhline(y=0, color='r', linestyle='--', label='0 (корень)')
plt.xlabel('Ток I, А')
plt.ylabel('Значение уравнения')
plt.title('Графическое отделение корней')
plt.legend()
plt.grid(True)
plt.show()
I_initial_guess = 2 
I_solution = fsolve(equation, I_initial_guess)

print(f"Рассчитанный ток в цепи: {I_solution:.3f} А")
