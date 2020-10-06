from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def instagram(username, password, target_user):
    driver = webdriver.Chrome()
    driver.get("http://www.instagram.com")
    try:
        username_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_elem.send_keys(username)
        username_elem.click()
    except:
        driver.quit()

    try:
        password_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.RETURN)
    except:
        driver.quit()

    try:
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'))
        )
        search_bar.send_keys(target_user)
        time.sleep(2)
        search_bar.send_keys(Keys.RETURN)
        search_bar.send_keys(Keys.RETURN)

    except:
        driver.quit()
    
    try:
        photo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME , "_9AhH0"))
        )
        photo.click()
    except:
        driver.quit()
    
    while True:
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span"))
            )
            like_button.click()
        except:
            driver.quit()

        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME , "coreSpriteRightPaginationArrow"))
            )
            next_button.click()
        except:
            driver.quit()


if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Password: ")
    target_user = input("Enter the username of target: ")
    try:
        instagram(username, password, target_user)
    except Exception as e:
        print(e)