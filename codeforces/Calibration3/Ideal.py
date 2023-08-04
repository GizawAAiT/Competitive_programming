import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with four columns
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'b': ['G1', 'G2', 'G1', 'G2', 'G1', 'G2', 'G1', 'G2', 'G1', 'G2'],
    'c': [2, 3, 4, 6, 2, 3, 4, 6, 2, 3],
    'd': [10, 7, 5, 8, 10, 7, 5, 8, 10, 7]
})

# Group by column 'b' and plot
for title, group in df.groupby('b'):
    group.plot(x='a', y=['c','d'], title=title)

# Display plot using matplotlib.pyplot.show()
plt.show()