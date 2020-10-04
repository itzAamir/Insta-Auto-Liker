from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def instagram(username, password, target_user):
    driver = webdriver.Chrome()
    driver.get("http://www.instagram.com")
    time.sleep(1)
    elem = driver.find_element_by_name("username")
    elem.clear()
    elem.send_keys(username)
    elem.click()

    elem1 = driver.find_element_by_name("password")
    elem1.clear()
    elem1.send_keys(password)
    elem1.send_keys(Keys.RETURN)

    time.sleep(3)
    elem2 = driver.find_element_by_xpath(r"//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
    elem2.send_keys(target_user)
    time.sleep(2)
    elem2.send_keys(Keys.RETURN)
    time.sleep(2)
    elem2.send_keys(Keys.RETURN)
    time.sleep(2)

    photo = driver.find_element_by_class_name("_9AhH0")
    photo.click()
    time.sleep(2)
    
    while True:
        like_button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span")
        like_button.click()

        next_button = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
        next_button.click()
        time.sleep(2)


if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Password: ")
    target_user = input("Enter the username of target: ")
    try:
        instagram(username, password, target_user)
    except NoSuchElementException:
        print(f"\n{'-'*5} All Pictures Liked Succesfully XD {'-'*5}")
    except Exception as e:
        print("\n",e)
        print("\n\nSorry there is some issue, you have to rerun the script")
    
    