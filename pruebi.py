import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import display
import seaborn as sns
plt.style.use('ggplot')

data = pd.read_csv(r"C:\Users\anapa\Downloads\pryt20.csv")
checks = data[data['check']==1]
'''
env_25 = checks[checks['env']=='Env_25']
env_25.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show() 
'''
'''
env_37 = checks[checks['env']=='Env_37']
env_37.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show() 
'''
'''
env_8 = checks[checks['env']=='Env_8']
env_8.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show() 
'''
'''
env_32 = checks[checks['env']=='Env_32']
env_32.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show()
'''
'''
env_31 = checks[checks['env']=='Env_31']
env_31.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show()
'''

env_38 = checks[checks['env']=='Env_38']
env_38.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show()