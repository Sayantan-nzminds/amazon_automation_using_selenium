import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.signinPage import SignInPage
from credentials import email,true_email,password,search_text




class Test_signup:
    baseURL = "https://www.amazon.in/"

    def test_hover(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        signIn_page = SignInPage(self.driver)

        signIn_page.mouseHover()
        signIn_page.clickSignIn()
        signIn_page.setEmail(email)

        signIn_page.ClickContinueButton()

        signIn_page.error()

        signIn_page.setEmailAgain(true_email)
        signIn_page.ClickContinueButtonAgain()

        signIn_page.setPassword(password)
        signIn_page.clickAccSignIn()

        signIn_page.setsearchbox(search_text)

        signIn_page.clickSearch()


        signIn_page.selectIPhone()



        signIn_page.printproductTitle()
        signIn_page.printproductPrice()
        signIn_page.addToCart()
        signIn_page.checkOut()




