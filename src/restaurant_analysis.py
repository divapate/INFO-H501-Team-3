import os
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")

def ensure_output_directory():
    os.makedirs("assets/images", exist_ok=True)

def load_restaurant_data():
    return pd.read_json(
        "data/processed/indy_philly_restaurant_aggregated.json",
        lines=True
    )

def plot_review_count_distribution(df):
    ensure_output_directory()

    plt.figure(figsize=(8,5))
    df["total_reviews"].plot(kind="hist", bins=30)

    plt.title("Distribution of Restaurant Review Counts")
    plt.xlabel("Total Reviews")
    plt.ylabel("Number of Restaurants")

    plt.tight_layout()
    plt.savefig("assets/images/review_count_distribution.png", dpi=300)
    plt.close()

def plot_top_reviewed_restaurants(df):
    ensure_output_directory()

    top10 = df.sort_values("total_reviews", ascending=False).head(10)

    plt.figure(figsize=(10,6))
    plt.barh(top10["name"], top10["total_reviews"])

    plt.title("Top 10 Most Reviewed Restaurants")
    plt.xlabel("Total Reviews")

    plt.tight_layout()
    plt.savefig("assets/images/top_reviewed_restaurants.png", dpi=300)
    plt.close()

def plot_rating_vs_reviews(df):
    ensure_output_directory()

    plt.figure(figsize=(8,5))
    plt.scatter(df["total_reviews"], df["avg_stars"], alpha=0.5)

    plt.title("Average Rating vs Total Reviews")
    plt.xlabel("Total Reviews")
    plt.ylabel("Average Star Rating")

    plt.tight_layout()
    plt.savefig("assets/images/rating_vs_reviews.png", dpi=300)
    plt.close()
