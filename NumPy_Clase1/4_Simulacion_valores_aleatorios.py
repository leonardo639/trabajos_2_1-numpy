# Crear 100 números aleatorios que se aproximen a una recta: y = 3*x+1
import numpy as np
import matplotlib.pyplot as plt

aleatorios = np.random.default_rng()

x = aleatorios.normal(size=(10, 10))
y = 3 * x  + aleatorios.normal(size=(10, 10)) + 1

fig, ax = plt.subplots(figsize=(6,6))
# Diagrama de dispersión

ax.scatter(x, y)

plt.show()