from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

# Fetch the webpage
url = "https://aws.amazon.com/bedrock/pricing/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Models of interest
models_of_interest = [
    "Claude 3 Haiku",
    "Claude 3.5 Sonnet",
    "Claude 3 Sonnet",
    "Claude 2.1",
    "Claude 3 Opus*",
    "Command-Light",
    "Command",
]

# Function to extract pricing from the table rows


def extract_from_table(rows):
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 2:
            model_name = columns[0].get_text(strip=True)
            price = columns[1].get_text(strip=True)
            if model_name in models_of_interest:
                pricing_data[model_name] = price


# Initialize the pricing data list
pricing_data = []

# Extract data from the tables in the webpage
for table in soup.find_all("table"):
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 3:
            model_name = columns[0].get_text(strip=True)
            input_price = columns[1].get_text(
                strip=True)[1:]  # Extract input price
            output_price = columns[2].get_text(
                strip=True)[1:]  # Extract output price

            if model_name in models_of_interest:
                models_of_interest.remove(model_name)
                # Append the model name and pricing to the pricing_data list
                pricing_data.append(
                    [model_name, f"${(float(input_price)) * 1000:.2f}", f"${(float(output_price)) * 1000:.2f}"])

# Display the table using tabulate
print(tabulate(pricing_data, headers=[
      "Model Name", "$ Per 1M Input Token", "$ Per 1M Output Token"], tablefmt="grid"))
