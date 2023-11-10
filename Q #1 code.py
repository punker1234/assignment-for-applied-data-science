import pandas as pd
import matplotlib.pyplot as plt

# This function reads data from an Excel file into a pandas DataFrame
# and is useful for importing Excel data into Python for analysis.
df = pd.read_excel("C:\\Users\\usman satti\\Documents\\WHO MANII .xlsx")

# Melt function in pandas is used to transform a DataFrame from wide format to long format
#essentially reshaping the data
df_melted = pd.melt(df, id_vars=['Country / Region', 'Disease'], var_name='Year', value_name='Cases')

# Filter data for the desired diseases
diseases = ['Mumps', 'Measles', 'Yellow fever', 'Rubella']
df_filtered = df_melted[df_melted['Disease'].isin(diseases)]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Defining different line styles for the plot
# Solid, Dahed, dash-dot, dotted
line_styles = ['-', '--', '-.', ':']
#Defining different colors for plot
colors = ['b', 'r', 'g', 'm']

# Create a multiple-line plot
for idx, disease in enumerate(diseases):
    df_temp = df_filtered[df_filtered['Disease'] == disease]
    ax.plot(df_temp['Year'], df_temp['Cases'], linestyle=line_styles[idx % len(line_styles)], color=colors[idx % len(colors)], label=disease)

# Adding a title and labels for better visualization 
ax.set_title('Global Disease Cases Over Time')
ax.set_xlabel('Years')
ax.set_ylabel('Number of Cases')
ax.legend()
ax.grid(True)
plt.show()
