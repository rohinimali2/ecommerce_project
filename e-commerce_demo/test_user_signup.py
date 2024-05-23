from locators import *
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def common(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    time.sleep(2)


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 60)
    return wait


# user signup:Positive scenario: Signup with valid details
def test_Valid_signup(driver, wait):
    common(driver)
    driver.find_element(By.XPATH, signin).click()

    user_val = wait.until(EC.visibility_of_element_located((By.XPATH, username)))
    user_val.send_keys("xya")

    element = wait.until(EC.visibility_of_element_located((By.XPATH, signin_password)))

    element.send_keys("123")

    driver.find_element(By.XPATH, signup).click()


#  Negative scenario: Needs to be identified
def test_invalid_signup(driver, wait):
    common(driver)
    driver.find_element(By.XPATH, sign_in).click()

    invalid_ele = wait.until(EC.visibility_of_element_located((By.XPATH, signin_username)))
    invalid_ele.send_keys("xya")

    element = wait.until(EC.element_to_be_clickable((By.XPATH, signin_password)))
    element.send_keys("")
    time.sleep(5)

    driver.find_element(By.XPATH, signin_login).click()
    alert = driver.switch_to.alert
    msg = "Please fill out Username and Password."
    assert alert.text == msg, "signed in with invalid credentials"
    print(alert.text)
    alert.accept()


# user_login: Positive scenario: Log in with valid credential

def test_user_login_valid(driver, wait):
    common(driver)
    driver.find_element(By.XPATH, valid_login).click()

    user_name = wait.until(EC.element_to_be_clickable((By.XPATH, valid_username)))

    user_name.send_keys("xya")

    password = wait.until(EC.element_to_be_clickable((By.XPATH, valid_login_password)))

    password.send_keys("123")

    driver.find_element(By.XPATH, valid_click).click()


# Negative scenario: Attempt to log in with invalid credentials.

def test_user_login_invalid(driver, wait):
    common(driver)
    driver.find_element(By.XPATH, login_byxpath).click()

    user_name = wait.until(EC.element_to_be_clickable((By.XPATH, login_username_byxpath)))

    user_name.send_keys("rohini")

    password = wait.until(EC.element_to_be_clickable((By.XPATH, login_password_byxpath)))

    password.send_keys("")

    driver.find_element(By.XPATH, login_click_byxpath).click()
    alert = driver.switch_to.alert
    msg = "Please fill out Username and Password."
    assert alert.text == msg, "signed in with invalid credentials"

    alert.accept()


# Product browsing:1. Verify that products are displayed correctly on the homepage
#                   2.Verify that product categories can be navigated successfully.

def test_product_displayed(driver, wait):
    common(driver)
    driver.find_element(By.XPATH, display_byxpath).click()

    phones = wait.until(EC.element_to_be_clickable((By.XPATH, phones_byxpath)))
    phones.click()

    phone = driver.find_elements(By.XPATH, phone_byxpath)
    print(len(phone))

    for phon in phone:
        print(phon.text)

    laptops = wait.until(EC.element_to_be_clickable((By.XPATH, laptops_byxpath)))
    laptops.click()

    laptop = wait.until(EC.presence_of_all_elements_located((By.XPATH, laptop_byxpath)))
    print(len(laptop))

    for lap in laptop:
        print(lap.text)

    monitors = wait.until(EC.element_to_be_clickable((By.XPATH, monitors_byxpath)))
    monitors.click()

    monitor = driver.find_elements(By.XPATH, monitor_byxpath)
    print(len(monitor))

    for mon in monitor:
        print(mon.text)


# Adding products to the shopping cart:
# Navigate to the last page by clicking next
# select the last product and add the product to the cart

def test_add_to_shoppingcart(driver, wait):
    common(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    next = driver.find_element(By.XPATH, next_byxpath)
    next.click()

    mac_book = wait.until(EC.element_to_be_clickable((By.XPATH, mac_book_byxpath)))
    mac_book.click()

    addingtocart = wait.until(EC.presence_of_element_located((By.XPATH, addingtocart_byxpath)))
    addingtocart.click()
    time.sleep(4)

    alert = driver.switch_to.alert
    msg = "Product added"
    assert alert.text == msg, "Product not added"
    print(alert.text)
    alert.accept()


# Checkout process:1.Positive scenario: Successfully check the items added to the cart
def test_add_to_cart(driver, wait):
    common(driver)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    next = driver.find_element(By.XPATH, next_positive)
    next.click()

    mac_book = wait.until(EC.element_to_be_clickable((By.XPATH, mac_book_positive)))
    mac_book.click()

    addingtocart = wait.until(EC.element_to_be_clickable((By.XPATH, addingtocart_byxpath)))
    addingtocart.click()
    time.sleep(4)

    alert = driver.switch_to.alert
    msg = "Product added"
    assert alert.text == msg, "Product not added"
    print(alert.text)
    alert.accept()

    cart = wait.until(EC.element_to_be_clickable((By.XPATH, cart_byxpath)))
    cart.click()

    no_of_rows = driver.find_elements(By.XPATH, no_of_rows_xpath)

    row = len(no_of_rows)
    if row > 1:
        print("product added successfully")

    print(row)


# Logout process:
# Positive scenario: Successfully log out.

def test_logout_process(driver, wait):
    common(driver)

    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, valid_login)))
    login_button.click()

    user_name = wait.until(EC.visibility_of_element_located((By.XPATH, valid_username)))
    user = "xya"

    user_name.send_keys(user)

    password = wait.until(EC.presence_of_element_located((By.XPATH, valid_login_password)))

    password.send_keys("123")

    login_in = wait.until(EC.element_to_be_clickable((By.XPATH, valid_click)))
    login_in.click()

    welcome = wait.until(EC.presence_of_element_located((By.ID, welcome_byid)))
    welcome_value = welcome.text

    print(welcome_value)
    if welcome_value == f'Welcome {user}':
        print("login successful")

    logout = wait.until(EC.element_to_be_clickable((By.XPATH, logout_byxpath)))
    logout.click()

    signupin = driver.find_element(By.XPATH, signin)
    signupin_value = signupin.text
    print(signupin_value)

    if signupin_value == f'Sign up':
        print("logout successfully")
