from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tabulate import tabulate

# Path to your ChromeDriver
chrome_driver_path = "chromedriver.exe"

# Initialize Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the OpenAI Pricing page
driver.get("https://openai.com/api/pricing/")

driver.implicitly_wait(10)  # Waits up to 10 seconds

# Define the models and their XPaths
models = [
    {
        "model": 'gpt-4o',
        "inputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[2]/div[2]/div',
        "outputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[3]/div[2]/div'
    },
    {
        "model": 'gpt-4o-2024-08-06',
        "inputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[4]/div[2]/div',
        "outputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[5]/div[2]/div'
    },
    {
        "model": 'gpt-4o-2024-05-13',
        "inputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[6]/div[2]/div',
        "outputPriceXPath": '//*[@id="3NVJSNqBOl7IxF8wHwFl8x"]/div/div[2]/div[7]/div[2]/div'
    },
    {
        "model": 'gpt-4o-mini',
        "inputPriceXPath": '//*[@id="MKm0TAT0sEESKMml2k65u"]/div/div[2]/div[2]/div[2]/div',
        "outputPriceXPath": '//*[@id="MKm0TAT0sEESKMml2k65u"]/div/div[2]/div[3]/div[2]/div'
    },
    {
        "model": 'gpt-4o-mini-2024-07-18',
        "inputPriceXPath": '//*[@id="MKm0TAT0sEESKMml2k65u"]/div/div[2]/div[4]/div[2]/div',
        "outputPriceXPath": '//*[@id="MKm0TAT0sEESKMml2k65u"]/div/div[2]/div[5]/div[2]/div'
    },
    {
        "model": 'gpt-3.5-turbo',
        "inputPriceXPath": '//*[@id="44znWxxoUVfvXZxhz2ZibK"]/div/div[2]/div[5]/div[2]/div',
        "outputPriceXPath": '//*[@id="44znWxxoUVfvXZxhz2ZibK"]/div/div[2]/div[6]/div[2]/div'
    },
    {
        "model": 'gpt-4-turbo',
        "inputPriceXPath": '//*[@id="5xnebq2BIlTUisMXUllDlm"]/div/div[2]/div[3]/div[2]/div',
        "outputPriceXPath": '//*[@id="5xnebq2BIlTUisMXUllDlm"]/div/div[2]/div[3]/div[3]/div'
    },
    {
        "model": 'gpt-4',
        "inputPriceXPath": '//*[@id="5xnebq2BIlTUisMXUllDlm"]/div/div[2]/div[5]/div[2]/div',
        "outputPriceXPath": '//*[@id="5xnebq2BIlTUisMXUllDlm"]/div/div[2]/div[5]/div[3]/div'
    }
]

pricing_data = []

# Extract pricing for each model
for model_info in models:
    model_name = model_info["model"]
    input_price_xpath = model_info["inputPriceXPath"]
    output_price_xpath = model_info["outputPriceXPath"]

    try:
        # Locate the input and output price elements using XPath
        input_price_element = driver.find_element(By.XPATH, input_price_xpath)
        output_price_element = driver.find_element(
            By.XPATH, output_price_xpath)

        # Extract and store the pricing information
        input_price = input_price_element.text.strip()
        output_price = output_price_element.text.strip()

        pricing_data.append({
            "Model": model_name,
            "Input Price": input_price,
            "Output Price": output_price
        })

    except Exception as e:
        print(f"Could not find pricing for {model_name}: {e}")

driver.quit()

print(tabulate(pricing_data, headers="keys", tablefmt="grid"))
