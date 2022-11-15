import requests
from bs4 import BeautifulSoup
import pandas as pd
from googletrans import Translator

import pandas as pd

URL = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/TV/2006/1-1000"

response = requests.get(URL)
html_doc = response.content

soup = BeautifulSoup(html_doc, "html.parser")
table = soup.find("table")
words = table.find_all("a", href=lambda href: href and href.startswith("/wiki/"))

dict_words = {}
translator = Translator()

for word in words:
    dict_words[word.text] = translator.translate(word.text, dest="pt").text

df = pd.DataFrame(list(dict_words.items()))
df.to_csv("data/english_words.csv", encoding="utf-8", index=False, header=False)