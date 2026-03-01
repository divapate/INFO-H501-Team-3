import pandas as pd

from visualize import (
    plot_state_distribution,
    plot_star_distribution,
    plot_top_categories,
    plot_dataset_comparison,
    interactive_state_distribution,
    generate_summary_table
)

from restaurant_analysis import (
    load_restaurant_data,
    plot_review_count_distribution,
    plot_top_reviewed_restaurants,
    plot_rating_vs_reviews,
    plot_average_reviews_by_state,
    plot_rating_boxplot_by_state
)

def load_full_data():
    return pd.read_json("data/yelp_academic_dataset_business.json", lines=True)

def load_filtered_data():
    return pd.read_json("data/yelp_in_pa_business.json", lines=True)

def main():
    try:
        # Load datasets
        full_df = load_full_data()
        filtered_df = load_filtered_data()

        # Business-level visualizations
        plot_state_distribution(filtered_df)
        plot_star_distribution(filtered_df)
        plot_top_categories(filtered_df)
        plot_dataset_comparison(full_df, filtered_df)

        summary_df = generate_summary_table(filtered_df)
        print("\nStatistical Summary:")
        print(summary_df)

        interactive_state_distribution(filtered_df)

        # Restaurant-level analysis
        restaurant_df = load_restaurant_data()

        plot_review_count_distribution(restaurant_df)
        plot_top_reviewed_restaurants(restaurant_df)
        plot_rating_vs_reviews(restaurant_df)
        plot_average_reviews_by_state(restaurant_df)
        plot_rating_boxplot_by_state(restaurant_df)

        print("\nAll visualizations generated successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
