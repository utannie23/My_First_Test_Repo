import numpy as np
import matplotlib.pyplot as plt
e = 50        
r = 10        
i0= np.array([0, 1.2, 2.7, 5.6])
u0= np.array([0, 0.9, 1.1, 1.3])
i = np.linspace(0, 5, 1000)
u = e - i * r
u1 = np.interp(i, i0, u0)
u2 = i*(100 * np.exp(-0.025 * i**2))
jk = u1 + u2
jm = np.argmin(np.abs(u- jk))
res= i[jm]
print(f"Приблизительное значение тока: {res:.3f} А")
plt.figure()
plt.plot(i,u, 'r', label='Линия нагрузки')
plt.plot(i, jk, 'b', label='ВАХ нагрузки')
plt.plot(res, jk[jm], 'ko') 
plt.annotate('i ≈ {res:.3f} А', (res, jk[jm]),textcoords="offset points", xytext=(10,10))
plt.title('Графическое отделение корня (расчет тока)')
plt.xlabel('Ток I, А')
plt.ylabel('Напряжение U, В')
plt.grid(True, linestyle=':')
plt.legend()
plt.show()
