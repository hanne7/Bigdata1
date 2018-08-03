import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
index_value = np.random.random_integers(low=0, high=N-1, size=N)
normal_sample = normal[index_value]
lognormal_sample = lognormal[index_value]
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]

fig = plt.figure()
axl = fig.add_subplot(1,1,1)

box_labels = ['normal', 'normal_sample', 'lognormal', 'lognormal_sample']
axl.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')
axl.set_title('Box Plots: Resampling of Two Distributions')
axl.set_xlabel('Distribution')
axl.set_ylabel('Value')

plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
plt.show()