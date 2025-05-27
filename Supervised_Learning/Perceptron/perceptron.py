import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset (make sure the CSV is in the same folder)
df = pd.read_csv("General Social Survey_2018.csv")

# Keep only "Very happy" (1) and "Not too happy" (3)
df = df[df['HAPPY'].isin([1, 3])]

# Map to binary: 1 = Very happy, 0 = Not too happy
df['HAPPY'] = df['HAPPY'].map({3: 0, 1: 1})

# Select and clean relevant columns
df = df[['HAPPY', 'AGE', 'SEX', 'DEGREE']].dropna()

# Encode categorical variables
label_encoders = {}
for col in ['SEX', 'DEGREE']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features (X) and target (y)
X = df[['AGE', 'SEX', 'DEGREE']]
y = df['HAPPY']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Perceptron
model = Perceptron()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


