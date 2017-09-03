from pylab import *

figure(figsize=(10,6), dpi=80)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X, C, color='red', linewidth=1.5, linestyle='-', label="cosine")
plot(X, S, color='blue', linewidth=2.0, linestyle='-', label="sine")

# 图例
legend(loc='upper left')

# 图片边界
xmin ,xmax = X.min(), X.max()
ymin, ymax = C.min(), C.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)

# 记号，标签
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1, +1],
       [r'$-1$',r'$+1$'])

# 移动脊柱
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

t = 2*np.pi/3
plot([t,t], [0,np.cos(t)], color='red', linewidth=2.5, linestyle="--")  # 虚线
scatter([t,], [np.cos(t),], 50, color="red")  # 点
annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))   # 注释

plot([t,t],[0,np.sin(t)], color ='blue', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='blue')

annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 半透明
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

...

show()