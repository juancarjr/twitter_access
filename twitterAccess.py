import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless")
# switched to firefox because of chrome hadshake erros
driver = webdriver.Firefox(options=options)
url = "https://twitter.com/i/flow/login"
driver.get(url)
time.sleep(5)
print('LOGGING IN...')
username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username.send_keys("regisrejunior")
username.send_keys(Keys.ENTER)

password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password.send_keys("funygooo")
password.send_keys(Keys.ENTER)

time.sleep(5)

url = "https://x.com/Kizzie_Kay"
driver.get(url)
print('MOVED TO TARGET URL...')
time.sleep(5)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

print('SAVING TWEETS...')
tweets = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='tweetText'] span")))]
driver.save_screenshot('screenie.png')
for t in tweets:
    print('-'*50)
    print(t)
