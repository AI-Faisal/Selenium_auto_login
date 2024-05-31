from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the ChromeDriver path
profile_path = 'C:/Users/Faisal El-Muhammady/AppData/Roaming/Mozilla/Firefox/Profiles/gmmsn0a8.faisal_automation'  # Firefox profile path
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)

options.add_argument('--headless')

# Initialize the Chrome WebDriver
driver = webdriver.Firefox(options=options)

# Open the target website
driver.get('https://cas.iium.edu.my:8448/cas/login?service=https%3a%2f%2fimaluum.iium.edu.my%2fhome')

# Find the username field and enter the username
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys('G2112217')

# Find the password field and enter the password
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('Cha961224')

# Find the login button and click it
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/section[4]/input[4]')
login_button.click()

# Wait for the next page to load and verify the login is successful
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/header/a/span[2]/img[1]'))
    )
    print("Login successful")
except Exception as e:
    print("Login failed", e)

# Close the browser
driver.quit()
