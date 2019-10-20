# Before use it, install selenium via pip - `pip install selenium`
# And download driver for browser that you are going to use (change path to that shit below)
# Usage example - python FindId.py https://www.acer.com/ac/en/GB/search D:\Python\Resources\ids

import sys

from selenium import webdriver


def test_actually(url, file_with_ids):
    # CHANGE PATH BEFORE USE!!!!!!!!!!!!!!!
    driver = webdriver.Chrome('D:\Python\pythonFirst\Resources\chromedriver.exe')

    with open(file_with_ids, 'r') as file:
        for line in file:
            driver.get(url + '?q=' + line)
            # TODO if id has been found - write it to separate file
            cont = input('Continue?\n')
            if cont.lower() == 'no' or cont.lower() == 'n':
                break


# 2 args, link and file with IDs
if __name__ == "__main__":
    test_actually(sys.argv[1], sys.argv[2])
