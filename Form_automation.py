from selenium import webdriver
from selenium.webdriver.common.by import By
import time

form_url = "https://forms.gle/WT68aV5UnPajeoSc8"

driver = webdriver.Chrome()
driver.get(form_url)
time.sleep(3)

driver.find_element(By.XPATH, '//input[@aria-label="Full Name"]').send_keys("Deepanshu Chauhan")
driver.find_element(By.XPATH, '//input[@aria-label="Contact Number"]').send_keys("6395862556")
driver.find_element(By.XPATH, '//input[@aria-label="Email ID"]').send_keys("deepanshueng16@gmail.com")
driver.find_element(By.XPATH, '//textarea[@aria-label="Full Address"]').send_keys("Mataur daurala meerut")
driver.find_element(By.XPATH, '//input[@aria-label="Pin Code"]').send_keys("250221")
driver.find_element(By.XPATH, '//input[@type="date" or contains(@aria-label,"Date of Birth")]').send_keys("01/16/2005")
driver.find_element(By.XPATH, '//div[@role="radio" and @aria-label="Male"]').click()
driver.find_element(By.XPATH, '//input[contains(@aria-label,"verify") or contains(@aria-label,"code")]').send_keys("GNFPYC")
driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]').click()

time.sleep(3)

driver.quit()
