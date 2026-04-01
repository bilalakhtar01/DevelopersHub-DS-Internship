
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
