import matplotlib.pyplot as plt
import numpy as np

series_names = ['Cowboy Bebop', 'The Wire', 'Breaking Bad', 'Dark', 'Severance']
ratings = [8.9, 9.3, 9.5, 8.7, 8.7]

bg_color = '#F5F5DC'

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

y_pos = np.arange(len(series_names))
bars = ax.barh(y_pos, ratings, color='#2C3E50', edgecolor='none')

ax.set_yticks(y_pos)
ax.set_yticklabels(series_names, fontsize=12, fontweight='bold', color='#333333')
ax.invert_yaxis()  # Labels read top-to-bottom

ax.set_xlabel('Audience Rating (out of 10)', fontsize=12, color='#333333')
ax.set_title('Top Series: Critical Consensus', fontsize=16, fontweight='bold', pad=20, color='#333333')

for spine in ax.spines.values():
    spine.set_visible(False)

for bar in bars:
    width = bar.get_width()
    ax.text(width - 0.4, bar.get_y() + bar.get_height()/2,
            f'{width}',
            ha='center', va='center', color='white', fontweight='bold')

plt.tight_layout()
plt.show()