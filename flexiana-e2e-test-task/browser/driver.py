from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver

def closeBrowser(driver):
    if(driver):
        driver.quit()