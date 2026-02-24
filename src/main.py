top_categories = (
    df.groupby("category")["stars"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

ax = top_categories.plot(kind="bar", color="#145A32")

ax.set_title("Top 10 Categories by Average Rating")
ax.set_xlabel("Business Category")
ax.set_ylabel("Average Rating")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("docs/top_categories.png", dpi=300)
plt.close()
