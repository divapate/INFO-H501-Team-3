# Yelp Review Sentiment Analysis
INFO-H501 – Team 3
Author: Jay Kelley

## Project Overview
This project analyzes Yelp review data to classify customer sentiment using machine learning techniques. The objective is to determine whether a review expresses positive or negative sentiment based solely on textual content.

Using natural language processing (NLP) methods and supervised learning models, this project demonstrates the complete data science workflow: data cleaning, feature engineering, model training, evaluation, and visualization.

## Dataset
The dataset consists of Yelp business reviews from selected U.S. states (Indiana and Pennsylvania). Each review includes review text, star rating, and location metadata.

For modeling purposes:
- High star ratings were labeled as positive
- Low star ratings were labeled as negative

## Methods & Approach

1. Data Cleaning
- Removed null and duplicate entries
- Standardized text formatting
- Filtered selected geographic regions

2. Text Preprocessing
- Tokenization
- Stopword removal
- Lowercasing
- TF-IDF vectorization

3. Model Training
- Logistic Regression classifier
- Train/test split evaluation
- Performance measured using accuracy and confusion matrix

## Results
- Achieved strong classification accuracy on test data
- Clear separation between positive and negative sentiment
- Created visualizations for top cities and state-level review distribution

## Project Structure
jay_yelp_project/
├── data/
├── src/
├── README.md
└── .gitignore

## How to Run

Clone the repository:
git clone https://github.com/divapate/INFO-H501-Team-3.git

Switch to Jay branch:
git checkout Jay

Install dependencies:
pip install -r requirements.txt

Run the main script:
python src/your_main_script.py

## Key Takeaways
- NLP techniques effectively classify sentiment from text
- Logistic Regression performs well for binary classification
- A structured pipeline improves reproducibility and clarity

## Future Improvements
- Test additional models (SVM, Random Forest, Neural Networks)
- Implement cross-validation
- Expand dataset coverage
- Deploy as a simple web application

