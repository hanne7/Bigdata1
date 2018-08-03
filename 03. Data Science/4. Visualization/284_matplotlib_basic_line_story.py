from numpy.random import randn
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plot_data1 = randn(12).cumsum()
plot_data2 = randn(12).cumsum()
plot_data3 = randn(12).cumsum()
plot_data4 = randn(12).cumsum()

fig = plt.figure()
axl = fig.add_subplot(1,1,1)
axl.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='LGE')
axl.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Samsung E')
axl.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='KB')
axl.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Hyundai H')
axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')

axl.set_title('Line Plots: Markers, Colors, and Linestyles')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.legend(loc='best')

plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
plt.show()