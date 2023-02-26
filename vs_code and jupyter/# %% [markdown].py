# %% [markdown]
# # Jupyte Notebook in VS code
# This is much better than jupyter notebook

# %%
print("My name is mujeeb bagash")

# %%
name=("Bangash")
name

# %%
age=input("what is your age? ")
age=int(age)
age


# %%
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = sns.load_dataset("Iris")

print (data.head(10))
plt.show()


# %%
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")

rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)

# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("full_data.csv")
sns.lineplot(x="Gender",y="Which mobile sim do you use",hue="Age",data=data)
plt.show()

# %%



# %%



