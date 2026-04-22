import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.kdeplot(data=df,
    x='total_bill')
plt.show()
