# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class WikiSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://forum.hkgolden.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_comments(self):
        driver = self.driver
        driver.get(self.base_url + "/view.aspx?type=AN&message=6967255")
        comments = []
        id_list = []
        trs = driver.find_element_by_xpath(".//tr")
        print(trs.text)
        c = driver.find_element_by_xpath(".//*[@class='ContentGrid']")
        comments.append(c)
        id_list.append(1)
        print(driver.find_element_by_xpath('.//*[@id="RcHVN"]'))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

