import numpy as np
incomes = np.random.normal(27000, 15000, 10000)
np.mean(incomes) 
%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()  

np.median(incomes)
