import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame 
df = pd.read_csv('data.csv') 
# Plot the DataFrame
sns.lineplot(data=df, x='frame', y='radius', label='pupal size')
# Display the plot
plt.show()