#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URL przykładowej strony z opiniami
url = "https://www.ceneo.pl/91184998#tab=reviews_scroll"

#pobranie kodu HTML strony z podanego URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wydobycie z kodu HTML strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych dla pojedynczej opinii
opinion = opinions.pop()


opinion_id = opinion["data-entry-id"]
author = opinion.find("div", "reviewer-name-line").string
recomendation = opinion.find("div", "product-review-summary").find("em").string
stars = opinion.find("span", "review-score-count")
purchased = opinion.find("div", "product-review-pz")
useful = opinion.find("button", "vote-yes").find("span").string
useless = opinion.find("button", "vote-no").find("span").string
content = opinion.find("p", "product-review-body").get_text()

print(opinion_id, author, recomendation, useful, useless, content, stars, purchased)