from scipy.interpolate import make_interp_spline
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import numpy as np


y_dfs = np.array([0,3.21,3.75,5.21,6.32,7.43,9.11,11.5,13.339])
x_dfs = np.array([0, 10, 20, 30, 40, 50, 60, 70,80])
X_Y_dfs = make_interp_spline(x_dfs, y_dfs)
Xdfs_new= np.linspace(x_dfs.min(), y_dfs.max(), 100)
Ydfs_new = X_Y_dfs(Xdfs_new)
 

y_bfs =np.array([0,3.4,5.2,6.77,7.54,9.46,10.9,12.77,15.32])
x_bfs = np.array([0, 10, 20, 30, 40, 50, 60, 70,80])
X_Y_bfs = make_interp_spline(x_bfs, y_bfs)
Xbfs_new= np.linspace(x_bfs.min(), y_bfs.max(), 100)
Ybfs_new = X_Y_bfs(Xbfs_new)


y_astar = np.array([0,3.2,4.77,5.42,7.45,7.99,8.7,10.99,14.8])
x_astar = np.array([0,10,20,30,40,50,60,70,80])
X_Y_astar = make_interp_spline(x_astar, y_astar)
Xastar_new= np.linspace(x_astar.min(), y_astar.max(), 100)
Yastar_new = X_Y_astar(Xastar_new)


y_djkistra = np.array([0,3.8,5.7,6.9,7.9,9.99,11.2,13.45,16.03])
x_djkistra = np.array([0,10,20,30,40,50,60,70,80])
X_Y_djekstra = make_interp_spline(x_djkistra, y_djkistra)
Xdjekstra_new= np.linspace(x_djkistra.min(), y_djkistra.max(), 100)
Ydjekstra_new = X_Y_djekstra(Xdjekstra_new)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(Xdfs_new, Ydfs_new,color='tab:blue' ,label='depth_first' ,linewidth = 3)
plt.plot(Xbfs_new,Ybfs_new,color='tab:orange' ,label='breadth_first' ,linewidth = 3)
plt.plot(Xastar_new,Yastar_new,color='tab:red',label= "A-star" ,linewidth = 3)
plt.plot(Xdjekstra_new,Ydjekstra_new, color='tab:green',label= "djekstra" , linewidth = 3)

y = np.array([0,2,4,6,8,10])
x = np.array([0,5,10,15])

my_xticks = ['1X:(20)','2X:(40)','3X:(60)','4X:(80)']
my_yticks = [0,7,13,20,25,30]
plt.xticks(x, my_xticks)
plt.yticks(y, my_yticks)

plt.plot(1,2)
ax.legend('depth-first','breadth-first')
ax.legend('djekstra','A-star')
leg = ax.legend()
ax.legend(loc='upper right', frameon=True)


plt.xlabel('No of random nodes from the original ')
plt.ylabel('average time to find solution in microsecond')
ax.set_title('benchmark analysis Based On average time ')
plt.show()