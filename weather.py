# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Weather(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.de/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_weather(self):
        driver = self.driver
        driver.get(self.base_url + "/?gfe_rd=cr&dcr=0&ei=GY0FWpqPLNyChgPj5pjwCA")
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("hong kong weather")
        driver.find_element_by_name("btnK").click()
        try: self.assertTrue(self.is_element_present(By.ID, "wob_tm"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("kyoto weather")
        driver.find_element_by_id("btnK").click()
        try: self.assertTrue(self.is_element_present(By.ID, "wob_tm"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("seoul weather")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
