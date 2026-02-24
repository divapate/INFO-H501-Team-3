import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

plt.rcParams.update({
    "figure.figsize": (10,6),
    "axes.titlesize": 18,
    "axes.labelsize": 15,
    "xtick.labelsize": 13,
    "ytick.labelsize": 13,
    "legend.fontsize": 13
})

plt.plot(x, y, linewidth=3)

ax.set_title("Sales Over Time")
ax.set_xlabel("Date")
ax.ylabel("Revenue ($)")

plt.tight_layout()
plt.savefig("docs/sales_over_time.png", dpi=300)
plt.close()
