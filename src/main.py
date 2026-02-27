import pandas as pd
from visualize import plot_state_distribution

def load_data():
    try:
        df = pd.read_json("data/yelp_in_pa_business.json", lines=True)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None

def main():
    df = load_data()
    
    if df is not None:
        plot_state_distribution(df)
        print("Visualization saved to assets/images/")
    else:
        print("Data could not be loaded.")

if __name__ == "__main__":
    main()
