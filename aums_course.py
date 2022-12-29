from re import S, sub
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
driver = webdriver.Chrome(options=options, executable_path="/opt/homebrew/bin/chromedriver")
# driver = webdriver.Edge()
# driver = webdriver.Firefox()
driver.maximize_window()

username = "<YOUR ROLL NO HERE>"
password = "<YOUR PASSWORD HERE>"

#authentication part:
driver.get("https://aumscb.amrita.edu/cas/login?service=https%3A%2F%2Faumscb.amrita.edu%2Faums%2FJsp%2FCommon%2Findex.jsp")
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/section[1]/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/section[2]/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/section[3]/input[3]").click()

#Note: Switch iframe thrice to get access to the dropdown
#/html/body/div[2]/div[1]/div[2]/nav/div[2]/ul/li[1]/a[2] - drop down
#sakaiframe - iframe
#Iframe1 - iframe

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"maincontentframe")))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"Iframe1")))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"sakaiframeId")))
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/nav/div[2]/ul/li[1]/a[2]").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/nav/div[2]/ul/li[1]/ul/li[4]/a").click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME,"portletMainIframe")))

eval_table = driver.find_elements(By.XPATH, "/html/body/div/div[1]/div/table/tbody/tr")
print("Total number of table rows: ", len(eval_table))

tag_list = []

for i in range(1, len(eval_table) + 1):

    print("Try to click on table row: ", i)
    link_path = "/html/body/div/div[1]/div/table/tbody/tr[{}]/td[1]/a".format(i)
    print(link_path)

    try:
        a_tag = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, link_path)))
        tag_list.append(a_tag.get_attribute("href"))

    except WebDriverException as e:
        print(e)
        print("WebDriverException")
        continue

print(tag_list)
for x in tag_list:
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    driver.get(x)
    try:
        for i in range(2, 17):
            try:
                driver.find_element(By.XPATH, "/html/body/div/div[8]/form/div[1]/fieldset/ol/li[{}]/div/div/div/div/div/table/tbody/tr/td[{}]/span/input".format(i, random.randint(1,4))).click()
            except WebDriverException as e:
                try:
                    driver.find_element(By.XPATH, "/html/body/div/div[7]/form/div[1]/fieldset/ol/li[{}]/div/div/div/div/div/table/tbody/tr/td[{}]/span/input".format(i, random.randint(1,4))).click()
                except WebDriverException as e:
                    print(e)
                    print("WebDriverException")
                    continue

        for i in range(19, 27):
            try:
                driver.find_element(By.XPATH, "/html/body/div/div[8]/form/div[1]/fieldset/ol/li[{}]/div/div/div/div/div/table/tbody/tr/td[{}]/span/input".format(i, random.randint(1,4))).click()
            except WebDriverException as e:
                try:
                    driver.find_element(By.XPATH, "/html/body/div/div[7]/form/div[1]/fieldset/ol/li[{}]/div/div/div/div/div/table/tbody/tr/td[{}]/span/input".format(i, random.randint(1,4))).click()
                except WebDriverException as e:
                    print(e)
                    print("WebDriverException")
                    continue
        driver.find_element(By.XPATH, "/html/body/div/div[8]/form/div[2]/input").click()

    except WebDriverException as e:
        print(e)
        print("Element is not clickable")
        continue

    



