# Before use it, install selenium via pip - `pip install selenium`
# And download driver for browser that you are going to use (change path to that shit below)
# Usage example - `python FindId.py https://www.acer.com/ac/en/GB/search D:\Python\Resources\ids`
import os
import platform
import sys

from selenium import webdriver


def find_ids(url, file_with_ids):
    # parent dir for this project
    dirname = os.path.dirname(os.path.dirname(__file__))
    os_type = platform.system()
    if 'windows' in os_type.lower():
        driver_path = os.path.join(dirname, 'Resources/chromedriver.exe')
    elif 'linux' in os_type.lower():
        driver_path = os.path.join(dirname, 'Resources/chromedriver')
    else:
        print('Cant detect what kind of driver should be used. OS - ' + os_type)
        exit(1)

    driver = webdriver.Chrome(driver_path)
    founded_ids = open(os.path.join(dirname, 'Resources/Founded_ids.txt'), 'w')
    not_founded_ids = open(os.path.join(dirname, 'Resources/Not_founded_ids.txt'), 'w')

    with open(file_with_ids, 'r') as file:
        for id in file:
            driver.get(url + '?q=' + id)
            element = driver.find_element_by_css_selector("[class*='heading-l']")
            if "No results" not in element.text:
                founded_ids.write(id + "\n")
            else:
                not_founded_ids.write(id + "\n")


# 2 args, link and file with IDs
if __name__ == "__main__":
    find_ids(sys.argv[1], sys.argv[2])
