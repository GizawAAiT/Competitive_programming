import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'b': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A'],
    'c': [5, 4, 3, 2, 1, 4, 3, 2, 1, 5],
    'd': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'e': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Group the data by the 'b' column
grouped = df.groupby('b')

# Create a plot for each group
for name, group in grouped:
    ax = group.plot(x='a', y='c', kind='line', label=name)
    ax.set_title(f'Group {name}')
    plt.show()
    