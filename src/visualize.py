import os
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn-v0_8-whitegrid")

def ensure_output_directory():
    os.makedirs("assets/images", exist_ok=True)

def plot_state_distribution(df):
    ensure_output_directory()

    state_counts = df["state"].value_counts()

    plt.figure(figsize=(8, 5))
    state_counts.plot(kind="bar")

    plt.title("Distribution of Yelp Businesses (IN & PA)")
    plt.xlabel("State")
    plt.ylabel("Number of Businesses")
    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.savefig("assets/images/state_distribution.png")
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

    # Categories are comma-separated strings
    categories = df["categories"].dropna().str.split(", ")
    exploded = categories.explode()

    top_categories = exploded.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    top_categories.plot(kind="bar")

    plt.title("Top 10 Business Categories (IN & PA)")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.savefig("assets/images/top_categories.png")
    plt.close()

def plot_dataset_comparison(full_df, filtered_df):
    ensure_output_directory()

    sizes = [len(full_df), len(filtered_df)]
    labels = ["Full Dataset", "IN & PA Filtered"]

    plt.figure(figsize=(6, 5))
    plt.bar(labels, sizes)

    plt.title("Dataset Size Comparison")
    plt.ylabel("Number of Businesses")

    plt.tight_layout()
    plt.savefig("assets/images/dataset_comparison.png")
    plt.close()
