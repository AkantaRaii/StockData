from sklearn.preprocessing import StandardScaler,Normalizer
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel
import pandas as pd

# Load the stock data
stock_data = pd.read_csv('data_with_indicator/iADBL.csv')

# Prepare feature matrix X and target vector y
X = stock_data.drop(columns=['Y_close', 'date'])  # Drop 'Y_close' and 'date' columns
y = stock_data['Y_close']  # Target variable

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize and fit the Lasso model
lasso = Lasso(alpha=0.3, max_iter=10000, tol=0.0001)
lasso.fit(X_scaled, y)

# Select important features using SelectFromModel
model = SelectFromModel(lasso, prefit=True)
selected_features = X.columns[model.get_support()]

# Convert selected features to list and print them
feature = selected_features.to_list()
print(feature)
print(len(feature))

# Create a new DataFrame with selected features
df_filtered = stock_data[feature].copy()  # Explicitly make a copy to avoid SettingWithCopyWarning

# Add the 'Y_close' column to the filtered DataFrame
df_filtered['Y_close'] = stock_data['Y_close']

# Save the filtered DataFrame to a CSV file
df_filtered.to_csv('lasso_data/rADBL.csv', index=False)
