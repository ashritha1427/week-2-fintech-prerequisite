# REST API & JSON Data Extraction

## Objective
Call a public REST API, inspect the JSON response, and convert the data into CSV format.

## API Used
JSONPlaceholder API

Endpoint:
https://jsonplaceholder.typicode.com/posts

## HTTP Method
GET

## Process
1. Sent a GET request to the public API.
2. Received the response in JSON format.
3. Converted the JSON response into a Pandas DataFrame.
4. Exported the data to a CSV file.
5. Saved the output as `api_data.csv`.

## Tools Used
- Python
- Requests
- Pandas
- JSON
- VS Code

## Output
The API data was successfully converted from JSON format to CSV format.