from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import math
import re

# initial settings
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")
score = driver.find_element(By.ID, "money")
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]
upgrade_list = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal",
                "buyTime machine"]
upgrade_list.reverse()

start = time.time()
while True:
    cookie_button.click()  # auto cookie clicker
    elapsed = (time.time() - start)

    # buy most expensive upgrade every 5 seconds
    if math.isclose(elapsed % 5, 0, abs_tol=0.05):
        for upgrade in upgrade_list:
            price = driver.find_element(By.ID, upgrade)
            price_text = price.text
            new_string = re.sub(",", "", price_text)  # remove commas
            price_list = [int(s) for s in new_string.split() if s.isdigit()]
            new_score = re.sub(",", "", score.text)  # remove commas
            if int(new_score) >= price_list[0]:
                price.click()
                break
