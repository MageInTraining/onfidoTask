# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib as ul

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def scrape_product_detail_page(product_detail_url):
    pass

def real_python_exercise(url):
    page = ul.urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    real_python_exercise("http://olympus.realpython.org/profiles")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
