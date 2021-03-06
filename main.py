# coding=utf-8

def scrape_product_detail_page(product_detail_url):
    import urllib.request
    from bs4 import BeautifulSoup
    import pandas as pd

    # return vale, a dictionary
    product_detail = {
        "model": None
        , "url": None
        , "main_photo_path": None
        , "additional_photo_paths": []
        , "price": None
        , "model_year": None
        , "parameters": {
            "weight": None
            , "frame": None
        }
    }

    # use BeautifulSoup to extract page html
    html_page = urllib.request.urlopen(product_detail_url)
    html_text = html_page.read().decode("utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    # this is pretty straightforward...
    product_detail["model"] = soup.title.string
    product_detail["url"] = product_detail_url
    product_detail["main_photo_path"] = soup.find("img", id="nahled")["src"]

    # only one of the products tried has additional pictures,
    # method returns NoneType error if not surrounded with try...except
    try:
        pohledy = soup.find("div", class_="pohledy")
        children = pohledy.findChildren("img")
        for child in children:
            product_detail["additional_photo_paths"].append(child["src"])
    except:
        product_detail["additional_photo_paths"].append(None)

    # actual price is child of 'cena' element
    price = soup.find("div", class_="cena")
    children = price.find("span")
    product_detail["price"] = int(''.join(i for i in children.string if i.isdigit()))

    # except for regex, pandas seems to be the only way (but it is slow), at least as far as Google is concerned
    dfs = pd.read_html(product_detail_url)
    df = pd.concat(dfs)
    product_detail["model_year"] = (df[df[1] == "Ročník"][2].item())

    # several products dont list weight and then I would get NoneType err
    try:
        product_detail["parameters"]["weight"] = (df[df[1] == "Hmotnost"][2].item())
    except:
        product_detail["parameters"]["weight"] = None
    product_detail["parameters"]["frame"] = df[df[1] == "Rám"][2].item()

    return product_detail


if __name__ == '__main__':
    import json

    results = [scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/spicy-cf-69/5943"),
               scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/overvolt-glp-team-b500/5957"),
               scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/esensium-32-m250/5947"),
               scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/lapierre-shaper-30-disc/6021"),
               scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/lapierre-overvolt-ht-24/5958")]

    with open('top-5-bikes.json', 'w') as outfile:
        json.dump(results, outfile)
