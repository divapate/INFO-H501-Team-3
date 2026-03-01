import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("indy_philly_restaurant_aggregated.json", lines=True)

# Split categories
df["categories"] = df["categories"].str.split(",")

# Explode into rows
df_exploded = df.explode("categories")

# Clean spaces
df_exploded["categories"] = df_exploded["categories"].str.strip()

# Remove generic category
df_exploded = df_exploded[df_exploded["categories"] != "Restaurants"]

# Count cuisines by city
cuisine_counts = (
    df_exploded.groupby(["city", "categories"])
    .size()
    .reset_index(name="count")
)

# Filter for Philly
philly = cuisine_counts[cuisine_counts["city"] == "Philadelphia"]
philly = philly.sort_values("count", ascending=False).head(10)

plt.figure()
plt.bar(philly["categories"], philly["count"])
plt.xticks(rotation=45)
plt.title("Top 10 Cuisines in Philadelphia")
plt.show()