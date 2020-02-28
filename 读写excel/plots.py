import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel('任务统计.xlsx',sheet_name='耗时统计')
print(df.head())

# 直方图
sns.distplot(df['耗时'])
plt.show()



