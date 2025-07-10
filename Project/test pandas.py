import pandas as pd
import matplotlib.pyplot as plt

# Create a Series
data = pd.Series([26, 10, 15, 49], index=['spring', 'summer', 'fall', "winter"])

# Plotting the pie chart
data.plot.pie(autopct='%.1f%%', figsize=(7, 7), startangle=90, explode=(0.0, 0, 0, 0))

plt.title('Fruit Distribution')
plt.ylabel('') # Hides the default y-axis label
plt.show()