
# DevelopersHub - Data Science & Analytics Internship

## Task 1: Exploring and Visualizing the Iris Dataset

### Objective:
Understand how to read, summarize, and visualize a dataset using the Iris Dataset.

### Approach:
- Loaded the Iris dataset using seaborn
- Explored dataset structure using .shape, .columns, and .head()
- Created visualizations: Scatter Plots, Histograms, Box Plots, Pair Plot, Heatmap

### Key Results:
- Setosa species is clearly separable from others
- Petal features are more useful for classification
- Strong correlation (0.96) between petal length and petal width
- Some outliers detected in sepal width

### Tools Used:
Python 3.10, pandas, matplotlib, seaborn

## Task 2: Credit Risk Prediction

### Objective:
Predict whether a loan applicant is likely to default using Logistic Regression and Decision Tree.

### Approach:
- Loaded and explored the Loan Prediction Dataset
- Handled missing values (mode for categorical, median for numerical)
- Visualized key features: income, education, credit history, loan amount
- Trained Logistic Regression and Decision Tree classifiers
- Evaluated using accuracy and confusion matrix

### Key Results:
- Credit History is the #1 factor for loan approval
- Married applicants and graduates have higher approval rates
- Both models achieved good accuracy

### Tools Used:
Python 3.10, pandas, matplotlib, seaborn, scikit-learn

## Task 3: Customer Churn Prediction (Bank Customers)

### Objective:
Identify customers who are likely to leave the bank based on their profile and banking behavior.

### Dataset:
Churn Modelling Dataset (Kaggle) - 10,000 bank customers with 11 features.

### Approach:
- Loaded and explored the Churn Modelling Dataset
- Cleaned data by removing unnecessary columns (RowNumber, CustomerId, Surname)
- Encoded categorical features (Geography using One-Hot Encoding, Gender using Label Encoding)
- Visualized churn patterns by Geography, Gender, Age, Balance, Products, and Active Status
- Trained three models: Logistic Regression, Decision Tree, and Random Forest
- Compared all models using accuracy and confusion matrix
- Analyzed feature importance to understand what influences churn

### Key Results:
- Germany has the highest churn rate among all countries
- Female customers churn more than male customers
- Older customers (age 40-60) are more likely to churn
- Inactive members have higher churn rates
- Age is the most important predictor of churn
- Random Forest achieved the best accuracy among all models

### Tools Used:
Python 3.10, pandas, numpy, matplotlib, seaborn, scikit-learn

## Task 4: Predicting Insurance Claim Amounts

### Objective:
Estimate medical insurance charges based on personal data using Linear Regression.

### Approach:
- Loaded and explored the Medical Cost Personal Dataset
- Visualized impact of age, BMI, smoking on charges
- Encoded categorical variables
- Trained Linear Regression model
- Evaluated using MAE and RMSE

### Key Results:
- Smoking is the #1 factor affecting insurance charges
- Smokers pay ~$23,000 more than non-smokers
- Age and BMI also significantly impact charges
- Model R² Score: ~0.75-0.78

### Tools Used:
Python 3.10, pandas, matplotlib, seaborn, scikit-learn

## Task 5: Personal Loan Acceptance Prediction

### Objective:
Predict which customers are likely to accept a personal loan offer based on their demographic and financial profile.

### Dataset:
Bank Marketing Dataset (UCI Machine Learning Repository / Kaggle)

### Approach:
- Loaded and explored the Bank Marketing Dataset
- Performed basic data exploration on features such as age, job, marital status, education, and balance
- Visualized acceptance patterns by Age, Job Type, Marital Status, Education, and Balance
- Encoded all categorical variables using Label Encoding
- Trained Logistic Regression and Decision Tree classifiers
- Compared both models using accuracy and confusion matrix
- Analyzed feature importance to identify key predictors
- Extracted business insights to identify which customer groups are more likely to accept the offer

### Key Results:
- Students and retired customers have the highest acceptance rates
- Younger (18-30) and senior (60+) age groups show higher acceptance
- Single customers accept more than married ones
- Customers with higher bank balance are more likely to accept
- Duration of last contact is the most important feature for prediction

### Business Recommendations:
- Focus marketing campaigns on students and retired individuals
- Target younger and senior age demographics
- Prioritize customers with higher bank balances
- Consider special offers for single customers

### Tools Used:
Python 3.10, pandas, numpy, matplotlib, seaborn, scikit-learn
