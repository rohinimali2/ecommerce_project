
signin ="//a[@id='signin2']"
username =  "//input[@id='sign-username']"
signin_password = "(//input[@id='sign-password'])[1]"

signup =  "//button[normalize-space()='Sign up']"
# Negative scenario: Needs to be identified
sign_in = "//a[@id='signin2']"
signin_username = "//input[@id='sign-username']"

signin_password =  "(//input[@id='sign-password'])[1]"
signin_login = "//button[normalize-space()='Sign up']"


# user_login: Positive scenario: Log in with valid credential

valid_login =  "//a[@id='login2']"
valid_username =  "//input[@id='loginusername']"
valid_login_password =  "(//input[@id='loginpassword'])[1]"
valid_click =  "//button[normalize-space()='Log in']"


 # Negative scenario: Attempt to log in with invalid credentials.
login_byxpath =  "(//a[normalize-space()='Log in'])[1]"
login_username_byxpath =  "//input[@id='loginusername']"
login_password_byxpath =  "(//input[@id='loginpassword'])[1]"
login_click_byxpath =  "//button[normalize-space()='Log in']"

# Product browsing:1. Verify that products are displayed correctly on the homepage
#                   2.Verify that product categories can be navigated successfully.


display_byxpath =  "(//a[@class='nav-link'])[1]"
phones_byxpath =  "(//a[normalize-space()='Phones'])[1]"
phone_byxpath =  "//a[@class='hrefch']"
laptops_byxpath =  "(//a[normalize-space()='Laptops'])[1]"
laptop_byxpath = "//a[@class='hrefch']"
monitors_byxpath = "(//a[normalize-space()='Monitors'])[1]"
monitor_byxpath = "//a[@class='hrefch']"


# Adding products to the shopping cart:
# Navigate to the last page by clicking next
# select the last product and add the product to the cart

next_byxpath =  "(//button[normalize-space()='Next'])[1]"

mac_book_byxpath = "(//a[normalize-space()='MacBook Pro'])[1]"

addingtocart_byxpath =  "(//a[normalize-space()='Add to cart'])[1]"


# Checkout process:1.Positive scenario: Successfully check the items added to the cart //tbody/tr/td[2].

next_positive =  "(//button[normalize-space()='Next'])[1]"

mac_book_positive = "(//a[normalize-space()='MacBook Pro'])[1]"

cart_byxpath =  "(//a[normalize-space()='Cart'])[1]"

no_of_rows_xpath = "//table//tr"


#Negative scenario: Attempt to checkout without adding any products to the cart.

next_chekout =  "(//button[normalize-space()='Next'])[1]"

apple_monitor_chekout = "(//a[normalize-space()='Apple monitor 24'])[1]"

cart_chekout = "(//a[normalize-space()='Cart'])[1]"

order_chekout = "(//button[normalize-space()='Place Order'])[1]"

name_chekout = "(//input[@id='name']"
    
country_chekout = "(//input[@id='country'])[1]"

city_chekout =  "//input[@id='city']"

credit_card_chekout =  "//input[@id='card']"

month_chekout =  "//input[@id='month']"

year_chekout =  "//input[@id='year']"

purchase_chekout = "//button[normalize-space()='Purchase']"
logout_byxpath= "(//a[normalize-space()='Log out'])[1]"
welcome_byid = "nameofuser"


