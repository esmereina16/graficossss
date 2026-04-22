import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.countplot(data=df,
    x='day')
plt.show()
