import pandas as pd

# Create a DataFrame with five columns
df = pd.DataFrame(
    data={
        'a': [1, 2, 3, 4, 5],
        'b': [1, 2, 1, 2, 1],
        'c': [2, 3, 4, 5, 6],
        'd': [3, 4, 5, 6, 7],
        'e': [4, 5, 6, 7, 8]
    }
)

# Create the first plot, using column 'a' as the x values and column 'b' as the grouping
ax1 = df.plot(x='a', y=['c', 'd', 'e'], kind='line', style='.-', groupby='b')

# Create the second plot, using column 'a' as the x values and column 'b' as the grouping
ax2 = df.plot(x='a', y=['c', 'd', 'e'], kind='bar', groupby='b')

# Create the third plot, using column 'a' as the x values and column 'b' as the grouping
ax3 = df.plot(x='a', y=['c', 'd', 'e'], kind='scatter', groupby='b')


import matplotlib.pyplot as plt

# Show the plots
plt.show()
