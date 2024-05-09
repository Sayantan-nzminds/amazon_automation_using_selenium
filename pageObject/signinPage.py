import select

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SignInPage:
    hello_icon= "//span[@id='nav-link-accountList-nav-line-1']"
    sign_In_Button = "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner'][normalize-space()='Sign in']"
    email_input = "//input[@id='ap_email']"
    continue_button= "//input[@id='continue']"
    error_msg= "//div[@id='auth-error-message-box']"
    password_input = "//input[@id='ap_password']"
    account_sign_In_Button= "(//input[@id='signInSubmit'])[1]"
    search_input = "//input[@id='twotabsearchtextbox']"
    enter_search_button ="//input[@id='nav-search-submit-button']"
    selected_iphone = "(//div[@class='aok-relative'])[5]"
    product_title = "(//span[@id='productTitle'])[1]"
    product_price = "//span[normalize-space()='1,48,900']"
    add_to_cart = "(//input[@id='add-to-cart-button'])[2]"
    proced_to_checkout_button ="//input[@aria-labelledby='attach-sidesheet-checkout-button-announce']"

    def __init__(self,driver):
        self.driver = driver



    def mouseHover(self):
        hover= self.driver.find_element(By.XPATH,self.hello_icon)
        achains = ActionChains(self.driver)
        achains.move_to_element(hover).perform()

    def clickSignIn(self):
        wait = WebDriverWait(self.driver, 10)
        signInButton = wait.until(EC.element_to_be_clickable((By.XPATH,self.sign_In_Button)))
        signInButton.click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.email_input).send_keys(email)

    def ClickContinueButton(self):
        self.driver.find_element(By.XPATH,self.continue_button).click()

    def error(self):
        error_message =self.driver.find_element(By.XPATH,self.error_msg).text
        if "There was a problem" in error_message:
            print(error_message)
        else:
            print("error msg does not have the mentioned part")

    def setEmailAgain(self,true_email):

        email_input_field = self.driver.find_element(By.XPATH,self.email_input)
        email_input_field.clear()
        email_input_field.send_keys(true_email)

    def ClickContinueButtonAgain(self):
        self.driver.find_element(By.XPATH,self.continue_button).click()

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_input).send_keys(password)

    def clickAccSignIn(self):
        self.driver.find_element(By.XPATH,self.account_sign_In_Button).click()

    def setsearchbox(self,search_text):
        self.driver.find_element(By.XPATH,self.search_input).send_keys(search_text)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.enter_search_button).click()

    def selectIPhone(self):
        self.driver.find_element(By.XPATH,self.selected_iphone).click()
        parent_window_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                break


    def printproductTitle(self):
        title= self.driver.find_element(By.XPATH,self.product_title).text
        if "Apple iPhone 15 Pro Max (256 GB) - Black Titanium" in title:
            print(title)

    def printproductPrice(self):
        price= self.driver.find_element(By.XPATH,self.product_price).text
        if "1,48,900" in price:
            print(price)

    def addToCart(self):
        self.driver.find_element(By.XPATH,self.add_to_cart).click()
        print("item added to cart")

    def checkOut(self):
        wait = WebDriverWait(self.driver, 10)
        CheckoutButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.proced_to_checkout_button)))
        CheckoutButton.click()


