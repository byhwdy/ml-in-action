import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0.0, 5.0, 50)
y1 = np.sin(x)
y2 = np.exp(x) * np.cos(x)

figures = [plt.figure(1), plt.figure(2)]
plt.figure(1)
axeses = [plt.subplot(221), plt.subplot(224)]

plt.subplot(221)
lines=plt.plot(x, y1, x, y2)
plt.subplot(224)
plt.plot(x)

plt.setp(figures, facecolor = 'c')
plt.setp(axeses, axis_bgcolor = 'w')
plt.setp(lines, linestyle = 'dashdot')

plt.show()