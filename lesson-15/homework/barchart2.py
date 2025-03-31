import matplotlib.pyplot as plt

# Data for the stacked bar chart
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = {
    'Category A': [20, 35, 30, 25],
    'Category B': [25, 20, 15, 30],
    'Category C': [10, 20, 15, 25]
}

# Create a stacked bar chart
plt.figure()
bottom = [0] * len(time_periods)
for category in categories:
    plt.bar(time_periods, data[category], label=category, bottom=bottom)
    bottom = [bottom[i] + data[category][i] for i in range(len(time_periods))]

# Add labels and title
plt.xlabel('Time Period')
plt.ylabel('Contribution')
plt.title('Contribution of Categories Over Time Periods')
plt.legend()

plt.show()