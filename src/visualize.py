import os
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn-v0_8-whitegrid")

def ensure_output_directory():
    os.makedirs("assets/images", exist_ok=True)

def plot_state_distribution(df):
    ensure_output_directory()

    state_counts = df["state"].value_counts().sort_index()
    total = state_counts.sum()

    plt.figure(figsize=(8, 5))
    ax = state_counts.plot(kind="bar")

    plt.title("Business Distribution by State (IN & PA)", fontsize=14, weight="bold")
    plt.xlabel("State")
    plt.ylabel("Number of Businesses")

    # Add percentage annotations
    for i, value in enumerate(state_counts):
        percentage = (value / total) * 100
        ax.text(i, value, f"{percentage:.1f}%", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig("assets/images/state_distribution.png", dpi=300)
    plt.close()

def plot_star_distribution(df):
    ensure_output_directory()

    plt.figure(figsize=(8, 5))
    df["stars"].plot(kind="hist", bins=9)

    plt.title("Star Rating Distribution (IN & PA)")
    plt.xlabel("Star Rating")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("assets/images/star_distribution.png")
    plt.close()

def plot_top_categories(df):
    ensure_output_directory()

    categories = df["categories"].dropna().str.split(", ")
    exploded = categories.explode()

    top_categories = exploded.value_counts().head(10)
    total = top_categories.sum()

    plt.figure(figsize=(10, 6))
    ax = top_categories.sort_values().plot(kind="barh")

    for i, value in enumerate(top_categories.sort_values()):
        percentage = (value / total) * 100
        ax.text(value, i, f"{percentage:.1f}%", va="center")

    plt.title("Top 10 Business Categories (IN & PA)", fontsize=14, weight="bold")
    plt.xlabel("Count")
    plt.ylabel("Category")

    plt.tight_layout()
    plt.savefig("assets/images/top_categories.png", dpi=300)
    plt.close()

def plot_dataset_comparison(full_df, filtered_df):
    ensure_output_directory()

    sizes = [len(full_df), len(filtered_df)]
    labels = ["Full Dataset", "IN & PA Filtered"]

    plt.figure(figsize=(6, 5))
    ax = plt.bar(labels, sizes)

    total = sizes[0]

    for i, value in enumerate(sizes):
        percentage = (value / total) * 100
        plt.text(i, value, f"{percentage:.1f}%", ha="center", va="bottom")

    plt.title("Dataset Size Comparison", fontsize=14, weight="bold")
    plt.ylabel("Number of Businesses")

    plt.tight_layout()
    plt.savefig("assets/images/dataset_comparison.png", dpi=300)
    plt.close()

def generate_summary_table(df):
    ensure_output_directory()

    summary = {
        "Total Businesses": len(df),
        "Mean Star Rating": round(df["stars"].mean(), 2),
        "Median Star Rating": round(df["stars"].median(), 2),
        "Star Rating Std Dev": round(df["stars"].std(), 2),
        "Indiana Businesses": len(df[df["state"] == "IN"]),
        "Pennsylvania Businesses": len(df[df["state"] == "PA"])
    }

    summary_df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])
    summary_df.to_csv("assets/images/statistical_summary.csv", index=False)

    return summary_df
