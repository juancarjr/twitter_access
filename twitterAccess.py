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
# Logging in
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

SCROLL_PAUSE_TIME = 5
NUMBER_OF_sCROLLS = 3
tweets_found = []
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

print('SAVING TWEETS...')
tweets = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='tweetText'] span")))]
tweets_found += tweets

for a in range(NUMBER_OF_sCROLLS):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # find tweets
    print('SAVING TWEETS...')
    try:
        tweets = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='tweetText'] span")))]
        tweets_found += tweets
    except Exception:
        pass

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

for t in tweets_found:
    print('-'*50 + 'NEW TWEET' + '-'*50)
    print(t)
driver.save_screenshot('screenie.png')

#TODO: fix broken tweets after scroll
#TODO: fixt timeout after scroll