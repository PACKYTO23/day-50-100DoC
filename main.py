import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "zmssmzx@gmail.com"
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

# homepage = driver.current_window_handle

time.sleep(3)
cookies = driver.find_element(By.XPATH, value='//*[@id="t1755874407"]/div/div[2]/div/div/div[1]/div[2]/'
                                              'button/div[2]/div[2]/div')
cookies.click()

time.sleep(3)
log_in = driver.find_element(By.LINK_TEXT, value="Iniciar sesión")
log_in.click()

time.sleep(3)
google_login = driver.find_element(By.LINK_TEXT, value="Continuar con Google")
google_login.click()

time.sleep(5)
pages = driver.window_handles
tinder_login = pages[0]
google_login = pages[1]

driver.switch_to.window(google_login)

google_email_phone = driver.find_element(By.ID, value="identifierId")
google_email_phone.send_keys(EMAIL)

google_next = driver.find_element(By.LINK_TEXT, value="Siguiente")
google_next.click()

# Google didn't permit to continue as it considered the site "not safe".
