
# Tried scraping using selenium but got errors instead 
# Try checking it out

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


object = requests.Session()

url = "https://onlineservices.miami-dadeclerk.com/officialrecords/StandardSearch.aspx"
driver = webdriver.Chrome("C:\Windows\chromedriver")
get_obj = driver.get(url)


def selenium_func():
    try:
        driver.find_element(By.ID, "li-tab1default-tab")
    except NoSuchElementException:
        pass

    date_from = driver.find_element(
        By.ID, "prec_date_from").send_keys("22/05/2022")
    date_to = driver.find_element(By.ID, "prec_date_to").send_keys("22/07/2022")
    select = Select(driver.find_element(By.ID, "pdoc_type"))
    select.select_by_index(44)
    # print(select)
    button = driver.find_element(By.ID, "btnNameSearch").click()
    # print(date_to)
    wait = WebDriverWait(driver, 40)
    wait.until(lambda driver: driver.find_element(
        By.ID, 'tableSearchResults').is_displayed() == False)
    s = BeautifulSoup(driver.page_source, "lxml")
    table = s.find_all(id="tableSearchResults")
    for info in table:
        data = [item.text for item in info]
    print(table)
