from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptops")

driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, "//span[text()='Dell']").click()

laptop_names = []
laptop_prices = []
laptop_reviews = []

# all items
all_items = driver.find_elements(By.XPATH, ".//div[@data-component-type='s-search-result']")

for item in all_items:
    # name
    try:
        if len(item.find_elements(By.XPATH, ".//h2[@class = 'a-size-medium a-spacing-none a-color-base a-text-normal']/span")) > 0:
            names = item.find_elements(By.XPATH, ".//h2[@class = 'a-size-medium a-spacing-none a-color-base a-text-normal']/span")
            for name in names:
                laptop_names.append(name.text)
        else:
            laptop_names.append("Not available")

    except:
        pass
    

    # price
    try:
        if len(item.find_elements(By.XPATH, ".//span[@class = 'a-price-whole']")) > 0:
            prices = item.find_elements(By.XPATH, ".//span[@class = 'a-price-whole']")
            for price in prices:
                laptop_prices.append(price.text)
        else:
            laptop_prices.append("Not available")
    except:
        pass

    
    # reviews
    try:
        if len(item.find_elements(By.XPATH, ".//span[@class = 'a-size-base s-underline-text']")) > 0:
            reviews = item.find_elements(By.XPATH, ".//span[@class = 'a-size-base s-underline-text']")

            for review in reviews:
                laptop_reviews.append(review.text)
        else:
            laptop_reviews.append("Not available")
    except:
        pass

print("Lengths")  
print("Names ====> ", len(laptop_names))
print("Prices ====> ",len(laptop_prices))
print("Reviews ====> ",len(laptop_reviews))


import pandas as pd

df = pd.DataFrame(zip(laptop_names, laptop_prices, laptop_reviews), columns=['laptop_names','laptop_prices', 'laptop_reviews'])
df.to_csv(r"/home/shruti29/Desktop/Project/web scraping/dell_laptops.csv",index=False)
