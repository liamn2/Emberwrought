import pandas as pd 
from sklearn.preprocessing import MinMaxScaler  
# Load data 
data = pd.read_csv(r'C:\Users\liamn\Downloads\sample_data.csv') 
# Preprocessing 
data1 = data.dropna()  # Drop rows with missing values 
#sqft = [data['Depth'] * data['Front_ft']]
X = data1[['Water_acc_bldg1', 'Gar_spaces']]
y = data1['Front_ft']  
# Encode categorical variables (if applicable)  
# Scale numerical features 
scaler = MinMaxScaler() 
X_scaled = scaler.fit_transform(X) 
#X_scaled = scaler.fit_transform(X)  
# Rest of the machine learning pipeline... 
