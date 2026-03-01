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

    plt.figure(figsize=(8, 5))

    colors = {"IN": "blue", "PA": "red"}

    for state in df["state"].unique():
        subset = df[df["state"] == state]
        plt.hist(
            subset["total_reviews"],
            bins=30,
            alpha=0.5,
            label=state,
            color=colors.get(state, "gray")
        )

    plt.title("Review Count Distribution (IN vs PA)")
    plt.xlabel("Total Reviews")
    plt.ylabel("Number of Restaurants")
    plt.legend()

    plt.tight_layout()
    plt.savefig("assets/images/review_count_distribution.png", dpi=300)
    plt.close()

def plot_top_reviewed_restaurants(df):
    ensure_output_directory()

    plt.figure(figsize=(10, 6))

    colors = {"IN": "blue", "PA": "red"}

    for state in ["IN", "PA"]:
        top = (
            df[df["state"] == state]
            .sort_values("total_reviews", ascending=False)
            .head(5)
        )

        plt.barh(
            top["name"],
            top["total_reviews"],
            color=colors[state],
            alpha=0.7,
            label=state
        )

    plt.title("Top Reviewed Restaurants by State")
    plt.xlabel("Total Reviews")
    plt.legend()

    plt.tight_layout()
    plt.savefig("assets/images/top_reviewed_restaurants.png", dpi=300)
    plt.close()

def plot_rating_vs_reviews(df):
    ensure_output_directory()

    plt.figure(figsize=(8, 5))

    colors = {"IN": "blue", "PA": "red"}

    for state in df["state"].unique():
        subset = df[df["state"] == state]
        plt.scatter(
            subset["total_reviews"],
            subset["avg_stars"],
            alpha=0.5,
            label=state,
            color=colors.get(state, "gray")
        )

    plt.title("Average Rating vs Total Reviews (IN vs PA)")
    plt.xlabel("Total Reviews")
    plt.ylabel("Average Star Rating")
    plt.legend()

    plt.tight_layout()
    plt.savefig("assets/images/rating_vs_reviews.png", dpi=300)
    plt.close()
