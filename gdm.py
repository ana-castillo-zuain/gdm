import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import display
import seaborn as sns
plt.style.use('ggplot')

data = pd.read_csv(r"C:\Users\anapa\Downloads\pryt20.csv")
print(data.head(15))
display.display(data.describe())
print(data.info(verbose=True, show_counts=True))
print(data.columns)
print(data['env'].value_counts())
print(data['env'].nunique())
print(data['block'].nunique())
print(data['trial'].nunique())
print(data.groupby('block')['gtyp_id'].nunique())
plt.show()
checks = data[data['check']==1]
print(checks.head(15))
plt.figure(figsize=(18, 8))
sns.boxplot(data=checks, x='env', y='Ys', palette='viridis')
plt.xticks(rotation=90)
plt.title('Boxplot de Yield (Ys) por Ambiente')
plt.xlabel('Ambiente')
plt.ylabel('Yield (Ys)')
plt.show()
for env, env_group in checks.groupby('env'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=env_group, x='gtyp', y='Ys')
    plt.xlabel('gtyp')
    plt.ylabel('Ys')
    plt.title(f'Comparison of Ys for each gtyp in {env}')
    plt.show()
    
checks.groupby('env').boxplot(column='Ys', by='gtyp', sharey=False)
plt.show()
#prueben estos 3 renglones en un archivo aparte y vean si anda (copien tmb la parte en donde definimos data y checks obvio)
env_3 = checks[checks['env']=='Env_3']
env_3.groupby('trial').boxplot(column='Ys',by='gtyp',sharey=False)
plt.show()