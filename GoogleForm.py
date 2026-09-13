import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleForm:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    def open(self):
        self.driver.get(self.url)
        time.sleep(2)

    def fill_field(self, question, value):

        field = self.driver.find_element(
            By.XPATH,
            f"//*[contains(normalize-space(.), '{question}')]"
            f"/ancestor::div[@role='listitem'][1]//input"
        )

        field.clear()
        field.send_keys(value)

        time.sleep(1)

    def fill_form(self, address, price, url):

        self.fill_field(
            "What is the address of the property?",
            address
        )

        self.fill_field(
            "What is the price per month?",
            price
        )

        self.fill_field(
            "What is the link to the property?",
            url
        )

    def submit(self):

        submit_button = self.driver.find_element(
            By.XPATH,
            "//span[contains(text(), 'Trimite')]"
        )

        submit_button.click()

        time.sleep(2)

    def next_form(self):
        self.driver.get(self.url)
        time.sleep(2)

    def close(self):
        self.driver.quit()