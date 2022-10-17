#Packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
from matplotlib.pyplot import figure


plt.style.use('ggplot')
from matplotlib.pyplot import figure
matplotlib.rcParams['figure.figsize'] = (12,8)

#pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)

df = pd.read_csv(r'C:\Users\Relef\OneDrive\Desktop\Data Analyst Projects\Movie Dataset\movies.csv')
df = df.dropna()

#create new table with correct matching year (based on 'released' year)

df['yearcorrect'] = df['released'].str.extract(pat = '([0-9]{4})').astype(int)

#Budget vs Gross Earnings Correlation

plt.scatter(x=df['budget'], y=df['gross'], alpha=0.5)
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')
plt.show()

#regplot with correlation line

sns.regplot(x="gross", y="budget", data=df, scatter_kws={'color': 'red'}, line_kws={'color':'blue'})
plt.show()

#Correlation matrix heatmap

correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

#Adding unique ID's to object type column values to create full heatmap

df_full = df

for col in df_full.columns:
    if(df_full[col].dtype == 'object'):
        df_full[col] = df_full[col].astype('category')
        df_full[col] = df_full[col].cat.codes

full_correlation_matrix = df_full.corr(numeric_only=True)
sns.heatmap(full_correlation_matrix, annot=True)
plt.title('Full Correlation Matrix')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')
plt.show()

print(df.head)


