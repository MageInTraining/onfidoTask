# coding=utf-8

def print_hi(name):
    print("Hi, {0}".format(name))


def scrape_product_detail_page(product_detail_url):
    pass


def real_python_exercise_beautiful_soup(base_url):
    import urllib as ul
    from bs4 import BeautifulSoup

    html_page = ul.urlopen(base_url + "/profiles")
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
    title = profiles_page.soup.title
    print(title)

def real_python_exercise_mechanical_soup2():
    import mechanicalsoup as ms
    import time
    browser = ms.Browser()

    for i in range(4):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select("#result")[0]
        result = tag.text
        print(f"The result of your dice roll is: {result}")
        if i < 3:
            time.sleep(2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #real_python_exercise_beautiful_soup("http://olympus.realpython.org")
    #real_python_exercise_mechanical_soup("http://olympus.realpython.org/login")
    #real_python_exercise_mechanical_soup2()
    scrape_product_detail_page()
