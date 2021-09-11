# coding=utf-8

def print_hi(name):
    print("Hi, {0}".format(name))


def scrape_product_detail_page(product_detail_url):
    pass


def real_python_exercise_beautiful_soup(base_url):
    from urllib import urlopen
    from bs4 import BeautifulSoup

    html_page = urlopen(base_url + "/profiles")
    html_text = html_page.read().decode("utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    for link in soup.find_all("a"):
        link_url = base_url + link["href"]
        print(link_url)


def real_python_exercise_mechanical_soup(url):
    import mechanicalsoup as ms
    browser = ms.Browser()
    login_page = browser.get(url)
    login_html = login_page.soup

    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    profiles_page = browser.submit(form, login_page.url)
    links = profiles_page.soup.select("a")
    for link in links:
        address = link["href"]
        text = link.text
        print(f"{text}: {address}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #real_python_exercise_beautiful_soup("http://olympus.realpython.org")
    real_python_exercise_mechanical_soup("http://olympus.realpython.org/login")
