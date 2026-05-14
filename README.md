# ☕ Starbucks Calorie Prediction

> Predicting calorie content of Starbucks menu items using Machine Learning — with a surprising result: **Linear Regression outperformed Random Forest**.

---

## 📌 Overview

This project explores the nutritional data of Starbucks menu items and builds machine learning models to accurately predict calorie content. Through careful feature engineering and model comparison, the project reveals that calorie prediction is driven by strong linear relationships between nutritional features — making Linear Regression the winning model.

---

## 🎯 Objective

To predict the calorie content of Starbucks drinks and food items based on nutritional attributes such as fat, sugar, and protein — and identify which ML model best captures these relationships.

---

## 📂 Dataset

The dataset contains nutritional information of Starbucks menu items:

| Feature | Description |
|---|---|
| Calories | Target variable |
| Total Fat (g) | Fat content |
| Sugars (g) | Sugar content |
| Protein (g) | Protein content |
| Other attributes | Additional nutritional data |

---

## ⚙️ Workflow

```
Raw Data → Cleaning → EDA → Feature Engineering → Model Training → Evaluation → Insights
```

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training — Linear Regression & Random Forest
5. Model Evaluation — MSE & R² Score
6. Insights & Conclusion

---

## 🧪 Feature Engineering

Three custom features were engineered to capture relative nutrient contributions:

| Feature | Formula | Purpose |
|---|---|---|
| `calorie_per_fat` | Calories / (Total Fat + 1) | Calorie density relative to fat |
| `sugar_to_calorie_ratio` | Sugars / (Calories + 1) | Sugar's share of total calories |
| `protein_density` | Protein / (Calories + 1) | Protein efficiency per calorie |

These engineered features significantly improved model performance by helping the algorithm understand nutrient relationships rather than raw values alone.

---

## 🤖 Models Used

### Linear Regression
- Baseline model to capture linear relationships
- Examines direct proportional relationships between nutritional features and calories
- Interpretable and fast

### Random Forest Regressor
- Ensemble model using multiple decision trees
- Designed to capture non-linear patterns
- Generally stronger on complex datasets

---

## 📊 Results

| Model | MSE | R² Score |
|---|---|---|
| ✅ **Linear Regression** | **89.61** | **0.9878** |
| Random Forest | — | 0.9604 |

---

## 🏆 Best Model: Linear Regression

**Linear Regression outperformed Random Forest** — achieving an R² score of **0.9878** vs **0.9604**.

This is a meaningful finding. Despite Random Forest's ability to model complex non-linear patterns, the simpler Linear Regression model won — which tells us something important about the data:

> **Calorie content in Starbucks items is primarily determined by strong, direct linear relationships between fat, sugar, and protein.** The data doesn't hide complex interactions — it follows predictable nutritional science. More fat + more sugar = more calories, in a near-perfectly linear way.

This is a great example of why blindly choosing complex models is not always the right approach. **Understanding your data matters more than model complexity.**

---

## 📊 Visualizations

### Calories Distribution
![Histogram](images/histogram.png)

### Sugar vs Calories
![Scatter](images/scatter.png)

### Calories Outliers
![Box Plot](images/box.png)

### Calories by Beverage Category
![Bar Chart](images/barh.png)

### Actual vs Predicted (Linear Regression)
![Linear Regression](images/LinearRegression.png)

### Feature Importance
![Feature Importance](images/Feature_Imp.png)

---

## 🧠 Key Insights

- **Fat and sugar are the strongest predictors** of calorie content
- **Linear Regression (R² = 0.9878) outperformed Random Forest (R² = 0.9604)** — proving the relationships in this dataset are fundamentally linear
- **Engineered features** like `calorie_per_fat` and `sugar_to_calorie_ratio` added meaningful signal beyond raw values
- **Model simplicity won** — a reminder that the best model is the one that fits the data, not the most complex one

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Lochank52/starbucks-calorie-prediction.git
cd starbucks-calorie-prediction

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook
```

---

## 🗂️ Project Structure

```
starbucks-calorie-prediction/
│
├── data/                   # Raw dataset
├── images/                 # Visualizations
├── notebook/               # Jupyter notebooks
├── src/                    # Python scripts
├── README.md
└── requirements.txt
```

---

## 🔮 Future Improvements

- [ ] Hyperparameter tuning for Random Forest
- [ ] Try XGBoost and Gradient Boosting models
- [ ] Add cross-validation for more robust evaluation
- [ ] Deploy as an interactive web app using Streamlit
- [ ] Extend dataset with more menu items

---

## 💬 Interview Summary

*"I built a calorie prediction model on Starbucks nutritional data. After comparing Linear Regression and Random Forest, Linear Regression won with an R² of 0.9878 vs 0.9604 — which shows the calorie content is driven by direct linear relationships between fat, sugar, and protein. I also engineered three custom features to improve model performance. The key takeaway: always let the data guide your model choice, not assumptions about complexity."*

---

## 👤 Author

**Lochan Kumar Yamala**  
📧 lochank1998@gmail.com  
🔗 [GitHub](https://github.com/Lochank52) | [LinkedIn](#)

---

*⭐ If you found this project useful, consider giving it a star!*