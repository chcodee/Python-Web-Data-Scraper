import pandas as pd
import requests
from bs4 import BeautifulSoup

# Ask the user to enter the URL to scrape
url = input("Enter the URL to scrape: ")

# Send a GET request to the webpage and parse the HTML content using Beautiful Soup
soup = BeautifulSoup(requests.get(url).content, "html.parser")

# Extract all h1, h2, h3, h4 and p tags on the webpage
h1_tags = [tag.text.strip() for tag in soup.select("h1")]
h2_tags = [tag.text.strip() for tag in soup.select("h2")]
h3_tags = [tag.text.strip() for tag in soup.select("h3")]
h4_tags = [tag.text.strip() for tag in soup.select("h4")]
p_tags = [tag.text.strip() for tag in soup.select("p")]

# Concatenate all the tags into a single list
all_tags =  ["H1 TAGS"] + h1_tags + ["H2 TAGS"] + h2_tags + ["H3 TAGS"] + h3_tags + ["H4 TAGS"] + h4_tags + ["P TAGS"] + p_tags

# Save the data as CSV and JSON using pandas
df = pd.DataFrame({"tags": all_tags})
df.to_csv("data.csv", index=False)
df.to_json("data.json", orient="records")


