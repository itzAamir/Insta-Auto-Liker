"""
InstaLiker

A tool that serves the feature of liking each and every instagram posts of a specified instagram profile. This tool is written in Python3 programming language. This tool is made for testing and fun purposes, there are no ways or means for this tool to be used for any illegal purposes or on any unauthorized services / properties. The tool has certain dependencies and also the usage of the tool is provided below. The tool is available at the github mirror of this repository with url https://github.com/itzAamir/Insta-Auto-Liker/.
Dependencies :
1. selenium - An external python3 library used for manipulating web browser action.
For the proper usage of the tool, check out the README.md file of this project.

Author : Aamir Khan (https://github.com/itzAamir/)
Created on : October 6, 2020

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 11, 2021

Changes made in the last modification :
1. Changed the entire code structure. Changed the names of the variables, changed the structure of the code. Added main function to the script + renamed the function named 'instagram' to 'autoLike'.
2. Added user inputs validation before calling the autoLike function.
3. Added the feature to hide the user's input on the console when entering the password.
4. Added commented docs and some in-code comments to make sure the source file looks professional and easily readable to other coders / programmers.

Authors contributed to this script (Add your name below if you have contributed) :
1. Amir Khan (github:https://github.com/itzAamir/, email:aamirkhan190320@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
    from time import sleep
    from getpass import getpass
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except Exception as e:
     # If there are any errors encountered during the importing of the required modules, then we display the error on the console screen and exit the script

    input(f'[ Error : {e} ]\nPress enter key to continue...')
    exit()

def autoLike(username = '', password = '', targetUsername = ''):
    """ The function to login to the specified instagram account and like all the posts of the requested instagram user. The function requires several dependencies, one of them being selenium library for python3. The functions defined in the selenium library are required to execute all the tasks defined under this function. The function uses the chrome driver for the process. """

    # Declaring the Chrome driver and opening the instagram home page
    driver = webdriver.Chrome()
    driver.get('http://www.instagram.com')

    # Filling up the username on the instagram login form
    try:
        username_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_elem.send_keys(username)
        username_elem.click()
    except Exception as e:
        # If there are any errors in the process of filling the username, then we quit the driver and print the error on the console screen

        driver.quit()
        input(f'[ Error : {e} ]\nPress enter key to continue...')
        return 0

    # Filling up the password on the instagram login form
    try:
        password_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_elem.send_keys(password)
        password_elem.send_keys(Keys.RETURN)
    except:
        # If there are any errors in the process of filling the password, then we quit the driver and print the error on the console screen

        driver.quit()
        input(f'[ Error : {e} ]\nPress enter key to continue...')
        return 0

    # Searching the target user and loading its profile
    try:
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'))
        )
        search_bar.send_keys(targetUsername)
        sleep(2)
        search_bar.send_keys(Keys.RETURN)
        search_bar.send_keys(Keys.RETURN)

    except:
        # If there are any errors in the process of loading the profile of the target user as per specified, then we quit the driver and print the error on the console screen

        driver.quit()
        input(f'[ Error : {e} ]\nPress enter key to continue...')
        return 0
    
    # Loading the first photo of the user's profile
    try:
        photo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME , '_9AhH0'))
        )
        photo.click()
    except:
        # If there are any errors in the process of loading a photo, then we quit the driver and print the error on the console screen

        driver.quit()
        input(f'[ Error : {e} ]\nPress enter key to continue...')
        return

    # Using a while..true loop to keep the likes process running till all the posts on the user's profile are liked
    while True:

        # Clicking the like button on each of the post
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span'))
            )
            like_button.click()
        except:
            # If there are any errors in the process of clicking the like button, then we quit the driver and print the error on the console screen

            driver.quit()
            input(f'[ Error : {e} ]\nPress enter key to continue...')
            return 0

        # Clicking on the next post in order to load the next post
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME , 'coreSpriteRightPaginationArrow'))
            )
            next_button.click()
        except:
            # If there are any errors in the process of clicking next button, then we quit the driver and print the error on the console screen

            driver.quit()
            input(f'[ Error : {e} ]\nPress enter key to continue...')
            return 0

def main():
    # Asking the user to enter the account credentials
    username = input('Enter your instagram username : ')
    password = getpass('Enter your instagram password : ')

    # Validating the user entered inputs
    if len(username) < 4 or username.isalnum() == False:
        # If the user entered username is either less than 4 characters or is not alphanumeric, then we display the error message on the console screen

        input(f'[ Error : Please enter a valid instagram username ]\nPress enter key to continue...')
    else:
        # If the user entered username is neither less than 4 characters nor non-alphanumeric, then we continue

        if len(password) < 5:
            # If the user entered password is less than 5 characters, then we display the error message on the console screen

            input(f'[ Error : Please enter a valid password ]\nPress enter key to continue...')
        else:
            # If the user entered password is valid, then we continue

            # Asking the user for the username of the target
            targetUsername = input('Enter the username of the target : ')

            # Validating the user input
            if len(targetUsername) < 4 or targetUsername.isalnum() == False:
                # If the user entered target username is either less than 4 or is not alphanumeric, then we display the error message on the console screen

                input(f'[ Error : Please enter a valid username for the target account ]\nPress enter key to continue...')
            else:
                # If the user entered target username is valid, then we proceed

                # Calling the autoLike function
                autoLike(username, password, targetUsername)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script

        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error on the console screen

        input(f'[ Error : {e} ]\nPress enter key to continue...')
        exit()