import time
from re import search
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service= Service("../resources/msedgedriver.exe"))

# driver.get("https://www.google.com")

# search_input = driver.find_element(By.ID, "APjFqb")
# search_input.send_keys("selenium")
# time.sleep(3)
# search_input.clear()

# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys("locators")
# time.sleep(3)

# googlesearch_button = driver.find_element(By.NAME, "btnK")
# googlesearch_button.click()
# time.sleep(30)

# imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
# imfl_button.click()
# time.sleep(3)

# href_elements = driver.find_elements(By.TAG_NAME, "a")
# for elmt in href_elements:
#     print(f'{elmt.text} - {elmt.get_attribute("href")}')

# images_link = driver.find_element(By.LINK_TEXT, "Images")
# images_link.click()
# time,sleep(10)

# images_link = driver.find_element(By.PARTIAL_LINK_TEXT, "ma")
# images_link.click()
# time,sleep(10)

# search_input = driver.find_element(By.CSS_SELECTOR, 'div > textarea')
# search_input.send_keys('selenium')
# time.sleep(5)

# settings_text = driver.find_element(By.XPATH,
#                                     "/html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div")
# print(settings_text.text)
# time.sleep(3)

# driver.get("https://the-internet.herokuapp.com/tables")

# and_example = driver.find_element(By.XPATH, "//td[text()='Tim' and @class='first-name']")
# print(f'AND EXAMPLE -> Found with both conditions: {and_example.text}')
#
# or_example = driver.find_element(By.XPATH, "//td[text()='Tim' or text()='Frank']")
# print(f'OR EXAMPLE -> Found with or conditions: {or_example.text}')
#
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
# print(f"Child Example -> Found {len(rows)} columns in the first table.")
#
# email_cell = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']")
# parent_row = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
# print(f"Parent Example -> Email '{email_cell.text}' "
#       f"belongs to row with first name: "
#       f"{parent_row.find_element(By.XPATH, './td[2]').text}")

# ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table")
# print(f'Ancestor example -> Table ID: {ancestor_table.get_attribute('id')}')
#
# descendants = driver.find_elements(By.XPATH, "//table[@id='table1']/descendant::td")
# print(f'Descendants Example -> Found {len(descendants)} descendant cells.')


driver.get("https://www.saucedemo.com/")
time.sleep(2)

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

elmt_above_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").above(password_field)
)

print(f"Above example -> Text above the password: "
      f"{elmt_above_password.get_attribute('placeholder')}")
elmt_above_password.send_keys('standard_user')
time.sleep(5)

field_below_username = driver.find_element(
    locate_with(By.TAG_NAME, 'input').below(username_field)
)

print(f'Below Example -> placeholder below username: '
      f'{field_below_username.get_attribute('placeholder')}')
field_below_username.send_keys('secret_sauce')
time.sleep(2)

login_button.click()
time.sleep(2)


twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME, 'a').to_right_of(twitter_icon))
print(f'toRightOf Example -> Element to the right of twitter icon'
      f'has href: {facebook_icon.get_attribute('href')}')

left_icon = driver.find_element(locate_with( By.TAG_NAME, 'a').to_left_of(facebook_icon))
print(f'toLeftOf Example -> Element to the Left of Facebook icon'
      f'has href: {left_icon.get_attribute('href')}')

near_fb = driver.find_elements(locate_with(By.TAG_NAME, 'a').near(facebook_icon))
for element in near_fb:
    print(f"Near example -> element near Facebook has href: "
          f"{element.get_attribute('href')}")
time.sleep(3)
driver.quit()