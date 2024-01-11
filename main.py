import matplotlib.pyplot as plt

# Data
years = [2021, 2022, 2023, 2024, 2025, 2026, 2027]

# Line 1: Chat and voice contribute by %
line1_data = [98.59, 70.16, 48.50, 45.15, 39.16, 32.18, 30.04]

# Line 2: Chat + voice contributes by number
line2_data = [3655, 13260, 12901, 15351, 16055, 15446, 16221]

# Line 3: Chat + voice condition to save server (from 2024) by Makoto expected
line3_data = [3243, 12482, 17526, 20523, 23425, 26414, 30425]

# Create figure and axis for subplot 1
fig, ax1 = plt.subplots(figsize=(10, 6))

# Adjusting the shade of blue for Line 1 and changing hatch pattern
# Solid bars for 2021 to 2023
ax1.bar(years[:3], line1_data[:3], label='Chat and voice contribute by %', color='#87CEEB', edgecolor='#87CEEB')

# Hatched bars for 2024 and onwards
ax1.bar(years[2:], line1_data[2:], label='_nolegend_', color='none', hatch='/', edgecolor='#87CEEB')  # Hatched bars from 2024

# Adding labels and title for subplot 1
ax1.set_xlabel('Years')
ax1.set_ylabel('Total Contribute by %')

# Modify the title for better appearance
ax1.set_title('Summary of Key Points\nInteractive and Projected Future of Xứ sở Wibu | [WBW] - Wibu Wonderland\nDiscord: discord.gg/wbw', fontsize=14, fontweight='bold')

# Create figure and axis for subplot 2
ax2 = ax1.twinx()

# Plotting Line 2
ax2.plot(years[:3], line2_data[:3], marker='o', label='Chat + voice contributes by number of members', color='orange')
ax2.plot(years[2:], line2_data[2:], marker='o', linestyle='dashed', color='orange', label='_nolegend_')  # Dashed line from 2024

# Plotting Line 3 with dots in the middle for the projection period
ax2.plot(years[:3], line3_data[:3], marker='o', label='Chat + voice MINIMUM condition to SAVE THE SERVER', color='green')
ax2.plot(years[2:], line3_data[2:], marker='o', linestyle='dashed', color='green')

# Adding labels and title for subplot 2
ax2.set_ylabel('Number of members')
ax2.tick_params('y')

# Move the legend for subplot 1 to a common position with subplot 2
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, -0.15))

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the plot
plt.show()
