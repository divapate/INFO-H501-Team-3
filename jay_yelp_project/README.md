# Yelp IN & PA Business Database  
**INFO-H501 Team 3 – Jay Branch**

---

## 📌 Project Overview

This project filters the Yelp Open Dataset to include only businesses located in:

- Indiana (IN)
- Pennsylvania (PA)

The filtered dataset is stored in a structured SQLite database and analyzed using Python. Visualizations summarize business distribution across states and top cities.

This project demonstrates:

- Data filtering and preprocessing
- SQLite database creation
- SQL querying
- Data visualization
- Git version control workflow

---

## 📊 Dataset Source

Yelp Open Dataset  
https://www.yelp.com/dataset

Note:  
The full raw dataset is not included in this repository due to GitHub’s 100MB file size limit.

---

## 🗂 Project Structure

```
jay_yelp_project/
├── data/
│   ├── yelp_IN_PA.db
│   ├── state_distribution.png
│   └── top_10_cities.png
├── src/
│   ├── filter_data.py
│   ├── create_database.py
│   └── visualize.py
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Filter Dataset

```
python3 src/filter_data.py
```

### 2️⃣ Create Database

```
python3 src/create_database.py
```

### 3️⃣ Generate Visualizations

```
python3 src/visualize.py
```

---

## 🗃 Database Verification

To confirm only IN and PA are included:

```
sqlite3 data/yelp_IN_PA.db
```

Inside SQLite:

```
SELECT DISTINCT state FROM businesses;
```

Expected output:

```
IN
PA
```

---

## 📈 Key Results

- 45,286 businesses analyzed
- Only Indiana and Pennsylvania included
- SQLite relational database created
- State-level and city-level visualizations generated

---

## 🛠 Technologies Used

- Python 3
- SQLite
- Matplotlib
- Git & GitHub
- Terminal (zsh)

---

## 👤 Author

Jay Kelley  
INFO-H501 Team 3 – Jay Branch

