# Before use it, install selenium via pip - `pip install selenium`
# And download driver for browser that you are going to use (change path to that shit below)
# Usage example - python FindId.py https://www.acer.com/ac/en/GB/search D:\Python\Resources\ids

import sys

from selenium import webdriver


def test_actually(url, file_with_ids):
    # CHANGE PATH BEFORE USE!!!!!!!!!!!!!!!
    driver = webdriver.Chrome('G:\chromedriver.exe')

    output = open('G:\Founded_ids.txt', 'w')

    with open(file_with_ids, 'r') as file:
        for id in file:
            driver.get(url + '?q=' + id)
            element = driver.find_element_by_css_selector("[class*='heading-l']")
            if "No results for" not in element.text:
                output.write(id + "\n")


# 2 args, link and file with IDs
if __name__ == "__main__":
    test_actually(sys.argv[1], sys.argv[2])
