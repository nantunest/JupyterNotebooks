import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

#sns.set_style('whitegrid')

filename = 'stats.csv'
data = pd.read_csv(filename)

period = data.values[0][0]
mean_error = data.values[1][0]
variance = data.values[2][0]
min_error = data.values[3][0]
max_error = data.values[4][0]

print(period, mean_error, variance, min_error, max_error)

dataper = (data[5:])/(period/1000.0) * 100

#dataper.plot.hist(bins=100, ylim=(0,10))
dataper.plot.hist(bins=100, log=True)

#x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
#plt.plot(x_axis, norm.pdf(data=dataper))
#plt.show()

#sns.distplot(dataper)

#plt.xlim(-2, 3)