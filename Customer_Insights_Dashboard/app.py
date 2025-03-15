import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample customer data
data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Age': [25, 34, 45, 23, 35, 40, 50, 29, 31, 42],
    'Purchases': [5, 10, 3, 8, 15, 7, 12, 6, 9, 11],
    'Revenue': [500, 1200, 300, 900, 2200, 850, 1800, 750, 1100, 1450],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)

# Customer segmentation based on revenue
df['Customer_Segment'] = pd.cut(df['Revenue'], bins=[0, 800, 1500, 2500], labels=['Low', 'Medium', 'High'])

# Data visualization - Revenue distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Revenue'], bins=5, kde=True, color='blue')
plt.xlabel('Revenue ($)')
plt.ylabel('Customer Count')
plt.title('Revenue Distribution of Customers')
plt.show()

# Save processed data
df.to_csv('customer_insights.csv', index=False)

print("Customer Insights Dashboard Data Processed Successfully!")
