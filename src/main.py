import pandas as pd
from visualize import (
    plot_state_distribution,
    plot_star_distribution,
    plot_top_categories,
    plot_dataset_comparison,
    interactive_state_distribution,
    generate_summary_table
)

def load_full_data():
    return pd.read_json("data/yelp_academic_dataset_business.json", lines=True)

def load_filtered_data():
    return pd.read_json("data/yelp_in_pa_business.json", lines=True)

def main():
    try:
        full_df = load_full_data()
        filtered_df = load_filtered_data()

        # Static visualizations
        plot_state_distribution(filtered_df)
        plot_star_distribution(filtered_df)
        plot_top_categories(filtered_df)
        plot_dataset_comparison(full_df, filtered_df)

        # Statistical summary
        summary_df = generate_summary_table(filtered_df)
        print("\nStatistical Summary:")
        print(summary_df)

        # Interactive visualization
        interactive_state_distribution(filtered_df)

        print("\nAll visualizations generated successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
