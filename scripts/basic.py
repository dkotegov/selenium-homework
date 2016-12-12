# -*- coding: utf-8 -*-

from selenium import webdriver

if __name__ == '__main__':
    # driver = webdriver.Chrome('./selenium_tools/chromedriver')
    driver = webdriver.Firefox(executable_path='../selenium_tools/geckodriver')
    driver.get("http://google.com/")
    driver.quit()
