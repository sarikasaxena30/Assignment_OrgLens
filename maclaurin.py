import numpy as np
import matplotlib.pyplot as plt
import mymath

# Values of x from -2π to 2π
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calculate cos(x) using Maclaurin series
y_values = [mymath.cos(x, terms=10) for x in x_values]

# Plot the Maclaurin series approximation of cos(x)
plt.plot(x_values, y_values, label='Maclaurin Series Approximation', color='b')

# Plot the actual cos(x) for comparison
plt.plot(x_values, np.cos(x_values), label='Actual cos(x)', linestyle='dashed', color='r')

plt.title("Cos(x) using Maclaurin Series vs Actual Cos(x)")
plt.xlabel("x")
plt.ylabel("Cos(x)")
plt.legend()
plt.grid(True)
plt.show()
