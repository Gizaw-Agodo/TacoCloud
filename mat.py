from scipy.interpolate import make_interp_spline
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import numpy as np


y_dfs = np.array([0,5,12,16,21,25,35,40,44])
x_dfs = np.array([0, 10, 20, 30, 40, 50, 60, 70,80])
X_Y_dfs = make_interp_spline(x_dfs, y_dfs)
Xdfs_new= np.linspace(x_dfs.min(), y_dfs.max(), 100)
Ydfs_new = X_Y_dfs(Xdfs_new)
 


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(Xdfs_new, Ydfs_new,color='tab:blue' ,label='depth_first' ,linewidth = 3)

y = np.array([0,5,10,15,20,25])
x = np.array([0,15,30,45])

my_xticks = ['1X:(20)','2X:(40)','3X:(60)','4X:(80)']
my_yticks = [0,10,20,30,45,45]
plt.xticks(x, my_xticks)
plt.yticks(y, my_yticks)

plt.plot(1,2)
ax.legend('depth-first','breadth-first')
ax.legend('djekstra','A-star')
leg = ax.legend()
ax.legend(loc='upper right', frameon=True)


plt.xlabel('No of random nodes from the original ')
plt.ylabel('average solution length')
ax.set_title('benchmark analysis Based On solution length ')
plt.show()