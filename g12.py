import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.rugplot(data=df,
    x='total_bill')
plt.show()
