import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check API response
print("Status Code:", response.status_code)

# Convert JSON response to Python data
data = response.json()

# Convert JSON data to DataFrame
df = pd.DataFrame(data)

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Save data as CSV
df.to_csv("api_data.csv", index=False)

print("\nCSV file created successfully: api_data.csv")