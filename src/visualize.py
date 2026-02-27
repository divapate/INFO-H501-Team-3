import os
import matplotlib.pyplot as plt
import pandas as pd

def ensure_output_directory():
    os.makedirs("assets/images", exist_ok=True)

def plot_state_distribution(df):
    ensure_output_directory()

    state_counts = df["state"].value_counts()

    plt.figure(figsize=(10, 6))
    state_counts.plot(kind="bar")

    plt.title("Distribution of Yelp Businesses by State", fontsize=14)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Number of Businesses", fontsize=12)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("assets/images/state_distribution.png")
    plt.close()
