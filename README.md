# Yelp Business Analysis: Indiana & Pennsylvania

## Overview

This project analyzes Yelp business data with a focused academic scope on **Indiana (IN)** and **Pennsylvania (PA)**.  

The goal is to:
- Filter the full Yelp dataset
- Analyze business distributions
- Visualize rating trends
- Identify dominant business categories
- Compare filtered data to the full dataset

---

## Dataset

Source: Yelp Academic Dataset

We:
1. Loaded the full business dataset
2. Filtered businesses located in Indiana and Pennsylvania
3. Stored the filtered dataset
4. Generated statistical visualizations

---

## Methodology

1. Load full dataset
2. Filter for IN and PA
3. Perform exploratory data analysis
4. Generate visualizations using Matplotlib
5. Save outputs to `assets/images/`

All visualizations are reproducible by running:

```bash
python3 src/main.py
```

---

## Visualizations

### 1. Dataset Size Comparison

Compares total businesses in full dataset vs IN & PA subset.

![Dataset Comparison](assets/images/dataset_comparison.png)

---

### 2. Business Distribution by State

Shows relative business density between Indiana and Pennsylvania.

![State Distribution](assets/images/state_distribution.png)

---

### 3. Star Rating Distribution

Displays frequency of Yelp star ratings in IN & PA.

![Star Distribution](assets/images/star_distribution.png)

---

### 4. Top 10 Business Categories

Identifies the most common industries within the filtered dataset.

![Top Categories](assets/images/top_categories.png)

---

## Project Structure

```
INFO-H501-Team-3/
│
├── data/                 # Raw datasets (ignored in Git)
├── src/                  # Processing and visualization scripts
├── assets/images/        # Generated visual outputs
├── requirements.txt
└── README.md
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/divapate/INFO-H501-Team-3.git
cd INFO-H501-Team-3
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run analysis:

```bash
python3 src/main.py
```

---

## Academic Focus

This project emphasizes:

- Reproducible analysis
- Clear data filtering methodology
- Structured visualization
- Clean repository organization
- Separation of raw data and generated outputs

---

## Contributors

- Jay Kelley, Yamini Hariharan and Divya Patel
- INFO-H501 Team 3
