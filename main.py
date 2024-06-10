import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

EMAIL = "zmssmzx@gmail.com"
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

homepage = driver.current_window_handle

time.sleep(3)
cookies = driver.find_element(By.XPATH, value='//*[@id="t1755874407"]/div/div[2]/div/div/div[1]/div[2]/'
                                              'button/div[2]/div[2]/div')
cookies.click()

time.sleep(3)
log_in = driver.find_element(By.LINK_TEXT, value="Iniciar sesión")
log_in.click()

for window_handle in driver.window_handles:
    if window_handle != homepage:
        driver.switch_to.window(window_handle)

time.sleep(3)
continue_Google = driver.find_element(By.LINK_TEXT, value="Continuar con Google")
continue_Google.click()
