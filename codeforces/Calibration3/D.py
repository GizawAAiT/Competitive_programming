import pandas as pd

# Create a DataFrame with three columns
df = pd.DataFrame(
    data={
        'x': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        'y': [2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
        'group': ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C']
    }
)

# Create a line plot, grouping the data by the 'group' column
ax = df.groupby('group').plot(x='x', y='y', kind='line')


import matplotlib.pyplot as plt

# Show the plot
plt.show()