import pandas as pd
import seaborn as sns

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
diabetes = pd.read_csv('diabetes.csv')

print(diabetes.columns)
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.columns)

diabetes.head()
print("dimension of diabetes data: {}".format(diabetes.shape))

print(diabetes.groupby('Outcome').size())
sns.countplot(diabetes['Outcome'],label="Count")