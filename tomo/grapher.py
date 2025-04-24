import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from adjustText import adjust_text

@dataclass
class Language:
    name: str
    readability: float
    performance: float
    convenience: float
    safety: float
    color: str = "blue"

languages = [
    Language("C",           3,     9,     2,     1),
    Language("C++",         1,   9.1,     4,     2),
    Language("Java",        5,     7,     5,     7),
    Language("Lua",        10,     5,     6,     5),
    Language("Python",      9,     4,    10,     5),
    Language("Rust",        4,   9.1,     3,     9),
    Language("Go",        8.7,     8,     8,     8),
    Language("Javascript",  8,     5,     7,     2),
    Language("Tomo",        9,   8.2,     9,   8.5, color="red"),
]

# # Example languages with ratings (0-10 scale)
# languages = [
#     Language("Python", 9.0, 5.0, 6.0, 9.0),
#     Language("C++", 4.0, 9.0, 5.0, 3.0),
#     Language("Rust", 7.5, 8.5, 9.5, 5.0),
#     Language("Java", 6.0, 7.0, 7.5, 6.0),
#     Language("Go", 8.0, 8.0, 7.0, 8.5),
#     Language("JavaScript", 6.5, 6.0, 3.0, 6.0),
#     Language("Haskell", 7.0, 7.0, 8.0, 4.0),
#     Language("C", 3.0, 10.0, 2.0, 7.0),
#     Language("Swift", 8.0, 7.5, 8.0, 7.0),
#     Language("TypeScript", 8.0, 6.0, 7.0, 5.5)
# ]

# Extract attributes for comparison
attributes = ["readability", "performance", "convenience", "safety"]
n_attrs = len(attributes)

# Create a grid of plots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Populate the grid with scatter plots
n = 0
for i, attr1 in enumerate(attributes):
    for j in range(i+1, len(attributes)):
        ax = axs[n % 3, n // 3]
        n += 1
        attr2 = attributes[j]

        # if i == j:
        #     ax.set_visible(False)
        #     continue
        
        # Extract the values for the current attributes
        x = [getattr(lang, attr1) for lang in languages]
        y = [getattr(lang, attr2) for lang in languages]

        # Create scatter plot
        colors = [l.color for l in languages]
        ax.scatter(x, y, s=80, alpha=0.7, c=colors)

        coef = np.polyfit(x,y,1)
        poly1d_fn = np.poly1d(coef) 
        line_xs = [min(x)-0.5, max(x)+0.5]
        ax.plot(line_xs, poly1d_fn(line_xs), color='gray', linestyle='dashed')

        texts = []
        for k, lang in enumerate(languages):
            texts.append(ax.text(x[k], y[k], lang.name, 
                                fontsize=8, color='black',
                                ha='center', va='bottom'))
            
        # # Use adjust_text to avoid overlaps
        # adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle='->', color='gray', lw=1),
        #             expand_points=(1.5,1.5),
        #             force_points=(0.1, 0.1), force_text=(0.5, 0.5))
        adjust_text(texts, 
           ax=ax,  # Specify the current axes
           expand_points=(1.5, 1.5),  # Expand area around points
           expand_text=(1.5, 1.5),    # Expand area around text
           #arrowprops=dict(arrowstyle='->', color='gray', lw=0.5),
           force_points=(0.5, 1.0),   # Stronger repulsion from points
           force_text=(0.5, 0.5),     # Moderate text-to-text repulsion
           only_move={'texts':'xy'},  # Allow movement in both directions
           autoalign=False,           # Don't try to align text
           avoid_self=True,           # Avoid self-collisions
           lim=5)                     # Limit iterations for faster processing
        # adjust_text(texts, ax=ax)

        # # Add language labels
        # for k, lang in enumerate(languages):
        #     ax.annotate(lang.name, (x[k], y[k]), fontsize=8, 
        #                xytext=(5, 5), textcoords='offset points')
        
        # Only add axis labels for the edge plots
        #if i == n_attrs-1:  # Bottom row
        ax.set_xlabel(attr1.replace('_', ' ').capitalize(), fontsize=10)
        #if j == 0:  # Leftmost column
        ax.set_ylabel(attr2.replace('_', ' ').capitalize(), fontsize=10)
            
        # Remove ticks and numbers
        ax.tick_params(axis='both', which='both', bottom=False, top=False, 
                      labelbottom=False, left=False, right=False, labelleft=False)
        
        # Set consistent axis limits
        ax.set_xlim(min(x)-0.5, max(x)+.5)
        ax.set_ylim(min(y)-0.5, max(y)+.5)
        
        # Clean look without grid lines or quadrants
        ax.set_frame_on(True)
        ax.grid(False)

# Adjust spacing between subplots
plt.tight_layout()

# Save the figure
plt.savefig('languages.png', dpi=100)
# plt.show()  # Uncomment to display in interactive environment
