from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import os
import logging

# Setup firefox options
firefox_options = Options()
firefox_options.headless = True

# Silent download of drivers
logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = 'False'

try:
    # Create service
    webdriver_service = Service(GeckoDriverManager().install())

    # Create driver
    driver = webdriver.Firefox(service=webdriver_service, options=firefox_options)

    # Define the URL and visit the page
    page_url = "https://super.walmart.com.mx/all-departments"
    driver.get(page_url)

    departmentWrapper = driver.find_element(
        By.CSS_SELECTOR, "#maincontent > main > div > div > div > div > section > div.w_RqoD.w_TmT8.mh2.ph2.ph1-xl.mb4.pb3")

    departments = departmentWrapper.find_elements("tag name", "div")
    departmentsArray = []
    processed_departments = set()

    for department in departments:
        departmentTitles = department.find_elements(By.TAG_NAME, "h2")
        for title in departmentTitles:
            soup = BeautifulSoup(title.get_attribute("innerHTML"), 'html.parser')
            name = soup.get_text()
            url = title.find_element(By.TAG_NAME, 'a').get_attribute("href")

            if name in processed_departments:
                continue

            processed_departments.add(name)

            subdepartments = []
            subdepartmentElements = department.find_elements(
                By.CSS_SELECTOR, "ul a")
            for subdepartmentElement in subdepartmentElements:
                subdepartment_name = subdepartmentElement.text
                subdepartment_url = subdepartmentElement.get_attribute("href")
                subdepartment = {"name": subdepartment_name,
                                 "url": subdepartment_url}
                subdepartments.append(subdepartment)

            department = {"name": name, "url": url,
                          "subdepartments": subdepartments}
            departmentsArray.append(department)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    if 'driver' in locals():
        driver.quit()
