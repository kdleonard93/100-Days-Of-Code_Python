# import selenium 
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from firecrawl import FirecrawlApp
from os import environ
from dotenv import load_dotenv

load_dotenv()

FC_API_KEY = environ.get("FC_API_KEY")

app = FirecrawlApp(api_key=FC_API_KEY)

scrape_results = app.scrape_url("https://digitaldopamine.dev", formats=['markdown', 'html'])

print(scrape_results)

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://digitaldopamine.dev")
# driver_header_3 = driver.find_element(By.TAG_NAME, "h3")
# print(driver_header_3.text)

# driver.quit()