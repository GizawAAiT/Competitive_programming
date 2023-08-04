import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with four columns
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'b': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    'c': [2, 2, 4, 4, 6, 6, 8, 8, 10, 10],
    'd': [1, 4, 2, 6, 4, 2, 7, 1, 9, 12]
})

# Group by column 'b' and plot
# Group by column 'b' and plot
df.groupby('b').plot(x='a', y=['c','d'])

# Display plot using matplotlib.pyplot.show()
plt.show()
