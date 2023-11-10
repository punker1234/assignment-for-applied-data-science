import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file
df = pd.read_excel("C:\\Users\\usman satti\\Desktop\\Manii's assignment\\Q#1 (Data).xlsx")
# Extract relevant data for plotting
years = df.columns[2:]
mumps_data = df.loc[0, years]
measles_data = df.loc[1, years]
yellow_fever_data = df.loc[2, years]
rubella_data = df.loc[3, years]

# Plotting
plt.figure(figsize=(12, 8))

# Scatter plot for each disease
plt.scatter(years, mumps_data, label='Mumps', marker='o')
plt.scatter(years, measles_data, label='Measles', marker='o')
plt.scatter(years, yellow_fever_data, label='Yellow Fever', marker='o')
plt.scatter(years, rubella_data, label='Rubella', marker='o')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.title('Disease Comparison Over Years')
plt.legend()

# Show plot
plt.show()







