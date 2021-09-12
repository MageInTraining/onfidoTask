# coding=utf-8

def scrape_product_detail_page(product_detail_url):
    import urllib.request
    from bs4 import BeautifulSoup
    import pandas as pd

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

    html_page = urllib.request.urlopen(product_detail_url)
    html_text = html_page.read().decode("utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    product_detail["model"] = soup.title.string
    product_detail["url"] = product_detail_url
    product_detail["main_photo_path"] = soup.find("img", id="nahled")["src"]
    try:
        pohledy = soup.find("div", class_="pohledy")
        children = pohledy.findChildren("img")
        for child in children:
            product_detail["additional_photo_paths"].add(child["src"])
    except:
        product_detail["additional_photo_paths"].add(None)

    price = soup.find("div", class_="cena")
    children = price.find("span")
    product_detail["price"] = int(''.join(i for i in children.string if i.isdigit()))

    dfs = pd.read_html(product_detail_url)
    df = pd.concat(dfs)
    product_detail["model_year"] = (df[df[1] == "Ročník"][2].item())
    product_detail["parameters"]["weight"] = (df[df[1] == "Hmotnost"][2].item())
    product_detail["parameters"]["frame"] = df[df[1] == "Rám"][2].item()

    return product_detail


if __name__ == '__main__':
    # scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/spicy-cf-69/5943")
    print(scrape_product_detail_page("https://www.lapierre-bike.cz/produkt/overvolt-glp-team-b500/5957"))
