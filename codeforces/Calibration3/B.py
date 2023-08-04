import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with sample data
data = {
    'a': [1, 2, 3, 4, 1, 2, 3, 4],
    'b': ['G1', 'G1', 'G1', 'G1', 'G2', 'G2', 'G2', 'G2'],
    'c': [2, 4, 6, 8, 3, 6, 9, 12]
}
df = pd.DataFrame(data)

# Group the DataFrame by column 'b' and plot the result
df.groupby('b').plot(x='a', y='c', kind='line')

plt.show()