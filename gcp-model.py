import requests
from bs4 import BeautifulSoup

url = 'https://ai.google.dev/pricing'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

available_models = soup.find_all(
    "h2", {"class": "gemini-inner__title gemini-type-t1-medium"})
input_pricing = [section.find_all("p") for section in soup.find_all("section", {
    "class": "gemini-section gemini-section--price-input gemini-section--label"})[1:6:2]]
output_pricing = [section.find_all("p") for section in soup.find_all("section", {
    "class": "gemini-section gemini-section--price-output gemini-section--label"})[1:6:2]]


for num in range(3):
    print(available_models[num].get_text())
    print(*[p.get_text() for p in input_pricing[0]])
    print(*[p.get_text() for p in output_pricing[0]])
